# /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

BASIC_CHINESE_WORD_SCOPE = (0x4e00, 0x9fa5)
ARABIC_NUMERALS_SCOPE = (48, 57)


def tell_chinese_word(unicode_word):
    # 判断该字符是否为基本汉字字符
    if type(unicode_word) != unicode:
        unicode_word = unicode_word.decode("utf-8")
    if BASIC_CHINESE_WORD_SCOPE[0] <= ord(unicode_word) <= BASIC_CHINESE_WORD_SCOPE[1]:
        return True
    else:
        return False


def tell_chinese_word_and_number(unicode_word):
    # 判断该字符是否为基本汉字字符或者阿拉伯数字
    if type(unicode_word != unicode):
        unicode_word = unicode_word.decode("utf-8")
    number = ord(unicode_word)
    if BASIC_CHINESE_WORD_SCOPE[0] <= number <= BASIC_CHINESE_WORD_SCOPE[1] or ARABIC_NUMERALS_SCOPE[0] <= number <= \
            ARABIC_NUMERALS_SCOPE[1]:
        return True
    else:
        return False
