# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:49:59 2021

@author: daiki
"""


import json

data = dict()
kane10 = 30
data["Change"] = {
    "10": kane10,
    "50": 20,
    "100": 30,
    "500": 10,
    "1000": 0
}
data["Stock"] = {
    "cola": 20,
    "energy": 20,
    "orange": 20,
    "tea": 20,
    "water": 20
}
data["name"] = {
    "cola": "syohin4.png",
    "energy": "syohin5.png",
    "orange": "syohin3.png",
    "tea": "syohin2.png",
    "water": "syohin1.png"
}
data["Earnings"] = {
    "value": 0
}

with open("mydata.json", mode = "wt", encoding = "utf-8") as f:
    json.dump(data, f, indent = 2)

with open("mydata.json", mode = "rt", encoding = "utf-8") as f:
    data = json.load(f)
    a = data["Change"]
    print(a["10"])
    print(a["100"])