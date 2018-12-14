# /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import torch
from torch import nn, optim
from torch.autograd import Variable
from torch.nn.parameter import Parameter
from torch import functional as F
from torch.nn import Module
from gensim.models import word2vec
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 词向量模型文件
model_path = ur"/users4/xyan/wlj/wlj/yanxin/tmp/sogou.model"
# 同义词文件
synonym_file = ur"/users4/xyan/data/dacilin-kuozhan/synonym.txt"
# 相关词文件
correlate_file = ur"/users4/xyan/data/dacilin-kuozhan/correlate.txt"

# 标记
MARK = u"*" * 20


def change_numpy_to_torch(np_array):
    return torch.from_numpy(np_array)


def extend_torch(a, b, c):
    results = torch.cat((a, b, c), 1).cuda()
    return results


def load_data(data_path, model, flag):
    # data_path 对应的文件路径
    # model     载入的词向量
    # flag      标识1为同义，0为非同义-包括相关以及其他
    with open(data_path, "r") as datainp:
        results = []
        for line in datainp:
            line = line.decode("utf-8")
            sp = line.strip().split()
            sp = sp[1:]
            for i in sp:
                for j in sp:
                    if i != j:
                        results.append((i, j))
    final = torch.FloatTensor().cuda()
    count=0
    for i, j in results:
        try:
            a, b = model[i], model[j]
            a = change_numpy_to_torch(a)
            b = change_numpy_to_torch(b)
            a = a.view(1, 100)
            b = b.view(1, 100)
            temp = torch.cat((a, b), 1).cuda()
            #print type(final)
            #print type(temp)
            final = torch.cat((final, temp), 0)
            count+=1
        except KeyError, e:
            pass
	
    x_train = final
    num_of_x_train = count
    print num_of_x_train
    print x_train.size()
    y_train = torch.FloatTensor().cuda()
    if flag == 1:
        temp = torch.ones((1, 1)).cuda()
        for i in range(num_of_x_train):
            y_train = torch.cat((y_train, temp), 0)
    else:
        temp = torch.zeros((1, 1)).cuda()
        for i in range(num_of_x_train):
            y_train = torch.cat((y_train, temp), 0)
    return x_train, y_train


if __name__ == "__main__":
    final = torch.FloatTensor().cuda()
    print final
    print type(final)
    '''
    word_model = word2vec.Word2Vec.load(model_path)
    x_results_synonym, y_results_synonym = load_data(synonym_file, word_model, 1)
    x_results_correlate, y_results_correlate = load_data(correlate_file, word_model, 0)
    print "before extend"
    x_trains = extend_torch(x_results_synonym, x_results_correlate)
    y_trains = extend_torch(y_results_synonym, y_results_correlate)
    print MARK
    print  "数据预处理完毕"
    print x_trains.size()
    print y_trains.size()

    print type(x_trains)
    print type(y_trains)

    torch.save(x_trains, "inputs.torch ")
    torch.save(y_trains, "targets.torch")
    '''
    print "Done!"
