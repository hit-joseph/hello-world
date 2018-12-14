#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from pyltp import Segmentor
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

LTP_DATA_DIR = '/users4/xyan/package/ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
infile = "sogou_set.txt"
outfile = "/users4/xyan/data_bank/corpus/phrase/before_clean/zh_segment.txt"
if __name__ == "__main__":
    segmentor = Segmentor()  # 初始化实例
    segmentor.load(cws_model_path)  # 加载模型
    with open(infile, "r") as r_file, open(outfile, "w", 0)as w_file:
        for line in r_file:
            line = line.strip()
            words = segmentor.segment(line)  # 分词
            word_list = list(words)
            word_list = [word.strip() for word in word_list]
            w_file.write(" ".join(words) + "\n")
    segmentor.release()  # 释放模型
    sys.exit(0)
