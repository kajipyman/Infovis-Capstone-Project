# encoding: utf-8
import requests
import collections
import re
import csv
import json
import math
import copy
import datetime
import glob
import os
import locale
from pyquery import PyQuery as pq
from google.cloud import translate
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


translate_client = translate.Client.from_service_account_json(
    'MyProject-ff848dab8949.json')
translate_client2 = translate.Client.from_service_account_json(
    'My First Project-2caebe2a423b.json')
sentiment_client = language.LanguageServiceClient.from_service_account_json(
    'MyProject-ff848dab8949.json')

system_language = 'en'


def collect_kw(rss_file, publisher_cache):
    locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
    with open(rss_file, 'r') as f:
        html = f.read().encode(encoding='utf-8')
        query = pq(html, parser='xml')

        src_link = query("rss > channel > link").eq(0).text()
        language = query("rss > channel > language").eq(0).text()
        get_time_raw = query("rss > channel > lastBuildDate").eq(0).text()
        get_time_dt = datetime.datetime.strptime(get_time_raw, '%a, %d %b %Y %H:%M:%S GMT')

        ret_list = []

        for item in query("rss > channel > item"):
            title = pq(item, parser='xml')("title").text()
            if len(title) == 0:
                continue
            link = pq(item, parser='xml')("link").text()
            pub_date_raw = pq(item, parser='xml')("pubDate").text()
            pub_date_dt = datetime.datetime.strptime(pub_date_raw, '%a, %d %b %Y %H:%M:%S GMT')
            if pub_date_dt < get_time_dt - datetime.timedelta(days=7):
                continue
            source = pq(item, parser='xml')("source")
            source_nm = source.text()
            source_url = source.attr("url")
            description = pq(item, parser='xml')("description").text()
            text = pq(description, parser='html')("p").text()
            """
            if len(text) == 0:
                for small_item in pq(description, parser='html')("a"):
                    text2 = pq(small_item, parser='html').text()
                    link2 = pq(small_item, parser='html').attr("href")
                    print(text2, link2)
            """
            """
            if system_language not in language:

                translations = translate_client.translate(
                    [title, source_nm, text],
                    target_language=system_language,
                    source_language=language[0:2]
                )
                title, source_nm, text = [translation['translatedText'] for translation in translations]
            """
            ret_list.append({
                "title": title,  # 翻訳
                "link": link,
                "pub_date": pub_date_dt.__str__() + ' GMT',
                "source_nm": source_nm,  # 翻訳
                "source_url": source_url,
                "desc": text,
                # "sent_score": 0
            })

        if system_language not in language and len(ret_list) != 0:
            titles = []
            source_nms = []
            for i in ret_list:
                titles.append(i["title"])
                if i["source_nm"] not in publisher_cache.keys():
                    source_nms.append(i["source_nm"])
            source_nms = list(set(source_nms))
            try:
                translations = translate_client.translate(
                    titles,
                    target_language=system_language,
                    source_language=language[0:2]
                )
            except:
                translations = translate_client2.translate(
                    titles,
                    target_language=system_language,
                    source_language=language[0:2]
                )
            for i, translation in enumerate(translations):
                ret_list[i]["title"] = translation['translatedText']

            if len(source_nms) != 0:
                translations = translate_client.translate(
                    source_nms,
                    target_language=system_language,
                    source_language=language[0:2]
                )
                for translation in translations:
                    publisher_cache[translation['input']] = translation['translatedText']

            for i in ret_list:
                i["source_nm"] = publisher_cache[i["source_nm"]]

        """
        for i in ret_list:
            document = types.Document(
                content=i['title'],
                type=enums.Document.Type.PLAIN_TEXT)
            sentiment = sentiment_client.analyze_sentiment(document=document).document_sentiment
            i['sent_score'] = sentiment.score
        """
        return {
            "src_link": src_link,
            "language": language,
            "get_time": get_time_dt.__str__() + ' GMT',
            "content": ret_list
        }


publisher_cache = {"": ""}  # publisherが空のとき用
original_rss_list = sorted(glob.glob("storage/rss/*/*.xml"))
for original_rss in original_rss_list:
    name, _ = os.path.splitext(original_rss)
    if os.path.exists('%s.json' % name):
        continue
    a = collect_kw(original_rss, publisher_cache)
    with open('%s.json' % name, 'w') as f:
        json.dump(a, f, indent=4)
