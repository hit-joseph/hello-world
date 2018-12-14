# -*- coding: utf-8 -*-

import os
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from gensim.models import word2vec
import gensim

if __name__ == "__main__":
    phrase_file = "/users4/xyan/experiment/phrase/phrase_vec_embedding/str2vec-master/demo-data/str2vec-demo_fre5-node01-core5/str2vec-demo_fre5-core10/str2vec-demo_fre5/str2vec-demo/input/sample-training-file.txt"
    vec_file = "/users4/xyan/experiment/phrase/phrase_vec_embedding/str2vec-master/demo-data/str2vec-demo_fre5-node01-core5/str2vec-demo_fre5-core10/str2vec-demo_fre5/str2vec-demo/output/sample-training-file.vec.txt"
    out_file = "phrase2vec.file"
    file_w = open(out_file, "w", 0)
    file_w.write("3323193 100\n")
    with open(phrase_file, "r")as phrase_in, open(vec_file, "r")as vec_in:
        for phrase, vec in zip(phrase_in, vec_in):
            phrase = "".join(phrase.strip().split())
            file_w.write(phrase + " " + vec)
    print "Done!"
