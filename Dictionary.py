# -*- coding:utf-8 -*-
def dictionary():
    f = open("dic.txt", encoding='gb18030')
    dic = []
    try:
        for line in f:
            line = line.strip("\n")
            dic.append(str(line))
    finally:
        f.close()
    return dic
def sdictionary():
    f = open("stopwords.txt", encoding='gb18030')
    dic = []
    try:
        for line in f:
            line = line.strip("\n")
            dic.append(str(line))
    finally:
        f.close()
    return dic
def pure():
    dic = dictionary()
    index = range(47194)
    dic = dict(zip(dic, index))
    stop_dic = sdictionary()
    index = range(722)
    temp = []
    stop_dic = dict(zip(stop_dic, index))
    for x, v in dic.items():
        if x in stop_dic:
            temp.append(x)
    for x in temp:
        del dic[x]
    return dic
if __name__ == '__main__':
    dic = dict()
    dic = pure()
    print(len(dic))
