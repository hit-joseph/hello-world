# /usr/bin/env python
# -*- coding: utf-8 -*-

# import re
import h5py
import os

# import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')


if __name__ == "__main__":
    file_w = open("record.txt", "w")
    dir = "/users4/xyan/experiment/phrase/phrase_vec_embedding/ELMo/ELMoForManyLangs-master/result"
    count1,count0=0,0
    for i in range(4181):
        main_word = "output_word_split"
        file=""
        if i < 10:
            file = os.path.join(dir, main_word + "000" + str(i))
        elif i<100:
            file = os.path.join(dir, main_word + "00" + str(i))
        elif i < 1000:
            file = os.path.join(dir, main_word + "0" + str(i))
        else:
            file = os.path.join(dir, main_word  + str(i))


        try:
            content = h5py.File(file, "r")
            if len(content) != 5000:
                count1+=1
                file_w.write(file +" "+str(len(content))+ u"\n")
        except:
            count0 += 1
            file_w.write(file + " " + str(0) + u"\n")
    print ("Done")
    print (count0)
    print (count1)
    print (count1+count0)
