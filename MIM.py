# -*- coding:utf-8 -*-

def MIM(text, dic, maxlen):

    send = []
    while(len(text) > 0):

        switch = 1

        if len(text) < maxlen:
            maxlen = len(text)

        temp = []  # 用来存放切割下的词
        text = list(text)  # 现在text是 列表
        b = ''
        for count in range(maxlen):#核心
            temp = text[len(text) - maxlen + count::]
            a = ''
            for x in range(maxlen - count):#构成已匹配字符
                a = a + temp[x]
            if a in dic:
                send.append(a)
                switch = 0
                break
        if switch == 1:
            send.append(text[-1])

        for x in range(maxlen - count):#去掉已匹配的部分
            text.pop()
        for y in range(len(text)):#构成剩余字符
            b = b + text[y]

        text = b
    return send[::-1]

def MIM_withoutsingle(text, dic, maxlen):

    send = []
    while(len(text) > 0):

        switch = 1

        if len(text) < maxlen:
            maxlen = len(text)

        text = list(text)  # 现在text是 列表
        b = ''
        for count in range(maxlen):#核心
            temp = text[len(text) - maxlen + count::]
            a = ''
            for x in range(maxlen - count):#构成已匹配字符
                a = a + temp[x]
            if a in dic:
                send.append(a)
                switch = 0
                break

        for x in range(maxlen - count):#去掉已匹配的部分
            text.pop()
        for y in range(len(text)):#构成剩余字符
            b = b + text[y]

        text = b
    return send[::-1]

if __name__ == '__main__':
    dic = {'可怕':1,'扣篮':2}
    text = '扣篮太可怕了'
    result = MIM_withoutsingle(text, dic, 4)
    print(result)