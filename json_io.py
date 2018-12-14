# /usr/bin/env python
# -*- coding: utf-8 -*-
import json


def load_json(json_file):
    # 本函数主要用来将json格式的内容load成对应的存储格式
    with open(json_file, "r")as load_f:
        data = json.load(load_f)
        return data


def store(data, outfile):
    # 本函数主要用来将对应的存储格式store成json格式的数据
    with open(outfile, 'w') as json_file:
        json_file.write(json.dumps(data))
