# encoding: utf-8
import requests
import collections
import re
import csv
import json
import math
import copy
from pyquery import PyQuery as pq
from google.cloud import translate
from dataset import *
from multiprocessing import Process, Manager


translate_client = translate.Client.from_service_account_json(
    'MyProject-ff848dab8949.json')

system_language = 'en'
id_extract = re.compile("topics/[0-9A-z]+")


def collect_kw(url_query, list_return_all, list_return_json):
    r = requests.get("https://news.google.com/?" + url_query)
    html = r.text
    query = pq(html, parser='html')
    keyword_list = [pq(x).attr("aria-label")
                    for x in query("#yDmH0d > c-wiz > div > div > div > aside > c-wiz > div > div:nth-last-of-type(1) > div").eq(1)("a")]
    id_list = [id_extract.search(pq(x).attr("href")).group()[7:]
                    for x in query("#yDmH0d > c-wiz > div > div > div > aside > c-wiz > div > div:nth-last-of-type(1) > div").eq(1)("a")]
    if len(keyword_list) != 0:
        if url_query[3:5] != system_language:
            translations = translate_client.translate(
                keyword_list,
                target_language=system_language,
                source_language=url_query[3:5]
            )
            english_keyword_list = [translation['translatedText'] for translation in translations]
        else:
            english_keyword_list = keyword_list

        value_of_return_list = [[kw, _id] for kw, _id in zip(keyword_list, id_list)]

        list_return_all.extend(english_keyword_list)

        list_return_json.append(
            {'query': url_query,
             'properties': {
                    'kw': dict(zip(english_keyword_list, value_of_return_list)),
                    'nation': query_list[url_query][0],
                    'region': query_list[url_query][3],
                    'coordinates': query_list[url_query][1:3],
                }
             }
        )
        #print(keyword_list)
        #print(english_keyword_list)


with Manager() as manager:
    l = manager.list()
    l2 = manager.list()
    jobs = [Process(target=collect_kw, args=(q, l, l2)) for q in query_list.keys()]

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    count_keyword = collections.Counter(l)
    from datetime import datetime
    with open('storage/csv/%s.csv' % datetime.now().strftime("%Y%m%d%H"), 'w') as csvfile:

        fieldnames = ['keyword', 'count']
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow(fieldnames)
        for key, value in count_keyword.items():
            writer.writerow([key] + [value])

        features = copy.deepcopy(l2)
        for item in features:
            score_sum = 0
            prop = item['properties']
            for k, v in prop['kw'].items():
                v.append(math.log(count_keyword[k]))
                score_sum += math.log(count_keyword[k])
            prop['score_sum'] = score_sum

    with open('storage/json/%s.json' % datetime.now().strftime("%Y%m%d%H"), 'w') as f:
        json.dump(dict(features=features), f, indent=4)