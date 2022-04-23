# -*- coding: utf-8 -*-
def cytolist():
    path = "C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\cydict.txt"
    list = []
    for line in open(path):
        if '\n' in line:
            #print("ok")
            line = line.strip('\n')
            #print(line)
        list.append(line)
    return list

#print(cytolist())