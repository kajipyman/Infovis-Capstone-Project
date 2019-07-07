# encoding:utf-8

import requests
import json
import os
import time
from tqdm import tqdm
from datetime import datetime
from glob import glob


for i in tqdm(sorted(glob('storage/json/*.json'))):
    with open(i, 'r') as f:
        df = json.load(f)
        for item in df['features']:
            q = item["query"]
            for a in item["properties"]["kw"].values():
                kw_id = a[1]
                if os.path.exists("storage/rss/%s/%s.xml" % (q, kw_id)):
                    continue
                url = 'https://news.google.com/_/rss/topics/%s?%s' % (kw_id, q)
                r = requests.get(url)
                if r.status_code != requests.codes.ok:
                    print("warning:", url)
                    continue
                os.makedirs("storage/rss/%s" % q, exist_ok=True)
                with open("storage/rss/%s/%s.xml" % (q, kw_id), "w") as tx:
                    tx.write(r.text)
                # print(url)
                time.sleep(0.5)
