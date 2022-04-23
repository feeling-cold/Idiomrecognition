import difflib

import dimsim

dist = dimsim.get_distance(['yi1', 'zhong4', 'yao4', 'hai4'],['ji1', 'zhong4', 'yao4', 'hai4'], pinyin=True)
#print(dist)
if dist < 15:
    pass
    # sql()


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

#print(string_similar('yongwangzhiqian', 'yongwangzhiqian'))
