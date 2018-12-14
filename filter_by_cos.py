# /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from gensim.models import word2vec

model_path = "/users4/xyan/data/sougou_data/word_vector/sogou.model"
src_file = "/users4/xyan/experiment/lexical/paraphrase.txt"
dst_file = "/users4/xyan/experiment/lexical/lab1/paraphrase_filter_cos.txt"
THRESHOLD = 0.5
if __name__ == "__main__":
    model = word2vec.Word2Vec.load(model_path)

    with open(src_file, "r")as in_file, open(dst_file, "w", 0)as out_file:
        for line in in_file:
            line = line.decode("utf-8").strip()
            words = line.split(u"\t")
            word = words[0]
            paraphrases = words[1:]
            try:
                paraphrases = [paraphrase for paraphrase in paraphrases if model.similarity(word, paraphrase) > THRESHOLD]
            except:
                print line
                continue
            if len(paraphrases) > 1:
                out_file.write(word + u"\t" + u"\t".join(paraphrases) + u"\n")
    print "Done!"
