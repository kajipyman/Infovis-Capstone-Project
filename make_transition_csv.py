# encoding: utf-8

import os
import glob
import csv
import json
import urllib.parse

ret_dict = {}

csv_list = sorted(glob.glob("storage/csv/*.csv"))
header = ["name"] + [os.path.basename(csv)[:-4] for csv in csv_list]

for i, csv_file in enumerate(csv_list):
    with open(csv_file, "r") as c:
        r = csv.reader(c)
        next(r)
        for row in r:
            try:
                ret_dict[row[0]][i] = row[1]
            except KeyError:
                ret_dict[row[0]] = [0] * len(csv_list)
                ret_dict[row[0]][i] = row[1]

with open("storage/transition.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for k, v in ret_dict.items():
        writer.writerow([k, *v])
"""
from pprint import pprint


json_list = sorted(glob.glob("storage/json/*.json"))
time_list = [i[13:23] for i in json_list]
region_list = ["Africa", "Asia", "Europe", "North America", "Oceania", "South America"]

for i, time in enumerate(time_list):
    with open("storage/json/" + time + ".json", "r") as j:
        r = json.load(j)
        for nation_block in r["features"]:
            region = nation_block["properties"]["region"]
            for kw in nation_block["properties"]["kw"].keys():
                try:
                    _ = ret_dict[kw]
                except KeyError:
                    new = dict(zip(time_list, [0] * len(time_list)))
                    ret_dict[kw] = {k: new for k in region_list}
                ret_dict[kw][region][time] += 1

for key, dic in ret_dict.items():
    with open("storage/transition/%s.json" % urllib.parse.quote(key.replace("/", "")), "w") as f:
        json.dump(dic, f, indent=4)

"""