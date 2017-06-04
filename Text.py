import re
import math
from 分词 import MIM
from 分词 import Dictionary

def pure(f):
    data = f.read()

    pat = re.compile(r'[\s<>\d()/a-zA-Z《》【】〉\-" \'·\[\]“”]')
    data = re.sub(pat, '', data)

    mode = re.compile(r'[，。、! ！?？；∶：: ;]')
    sentences = re.split(mode, data)

    f.close()
    return sentences

def split(txt_list, save_list, dic):
    num = 0
    while (num < len(txt_list)):
        try:
            target_f = open(txt_list[num], encoding='gb18030')
            sentences = pure(target_f)
            target_f.close()
            # 3.对文本列表里的每一句话进行处理,并写入文件
            result_f = open(save_list[num], 'w', encoding='gb18030')
            for sentence in sentences:
                result = MIM.MIM_withoutsingle(sentence, dic, 4)
                if len(result) != 0:
                    a = ''
                    for x in result:
                        a = a + x
                        a = a + ' '
                    result_f.write(a)  # 写入文件处理
                    result_f.write('\n')
            result_f.close()
            print(str(num) + ' is ok')
        except:
            print(str(num) + ' is not ok')
        num = num + 1
def get_words(path):
    try:
        words = []
        target_f = open(path, encoding='gb18030')
        data = target_f.read()
        pat = re.compile(r'\n')
        data = re.sub(pat, ' ', data)
        mode = re.compile(r' ')
        words = re.split(mode, data)
        target_f.close()
        words.remove(' ')
    except:
        pass
    return words
def make_choice(path, all_word, probability, default, txt_percentage, sort_result):

    sum = [0 for i in range(24)]
    for word in all_word:
        num = 0
        for x in probability:
            if word in x:
                sum[num] = sum[num] + math.log(x[word],1/100)
            num = num + 1
    for x in range(24):
        sum[x] = sum[x] + math.log(txt_percentage[x], 1/100)
    index = sum.index(max(sum))
    sort_result[index].append(path)

if __name__ == '__main__':
    make_choice()