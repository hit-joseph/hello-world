#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from pyltp import Postagger
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

LTP_DATA_DIR = '/users4/xyan/package/ltp_data_v3.4.0'  # ltp模型目录的路径
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 分词模型路径，模型名称为`cws.model`

infile = "sogou_set_seg.txt"
outfile = "sogou_set_pos.txt"
if __name__ == "__main__":
    postagger = Postagger()  # 初始化实例
    postagger.load(pos_model_path)  # 加载模型
    with open(infile, "r") as r_file, open(outfile, "w", 0)as w_file:
        for line in r_file:
            words = line.strip().split()  # 分词结果
            postags = postagger.postag(words)  # 词性标注
            w_file.write("\t".join(postags) + "\n")
    postagger.release()  # 释放模型
