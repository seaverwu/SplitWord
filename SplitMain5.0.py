IDF = '/Users/mac/Desktop/实验四 5/dataset_616979/616979/体育领域/体育分类测试文档/IDF值.txt'
root = "/Users/mac/Desktop/实验四 5/dataset_616979/616979/体育领域/体育分类测试文档"
from 分词 import Dictionary
from 分词 import MIM
from 分词 import Text
from 分词 import Findpath
import re
import collections
import math

#首先遍历目标目录，返回文件夹列表和txt列表
#txt_list和save_list中序号相同
txt_list = Findpath.get_path(root)
save_list = []
for x in txt_list:
    path = x.split('/')
    url = ''
    for x in range(10):
        url = url + path[x] + '/'
    save_list.append(url + '分词结果/' + path[-1])
#1.生成字典
dic = Dictionary.dictionary()
index = range(47194)
dic = dict(zip(dic, index))
#2.处理目标文本
num = 0
idf_list = []
while(num < len(txt_list)):

    try:
        target_f = open(txt_list[num], encoding='gb18030')
        sentences = Text.pure(target_f)
        target_f.close()
        #3.对文本列表里的每一句话进行处理,并写入文件
        result_f = open(save_list[num], 'w', encoding='gb18030')
        for sentence in sentences:
            result = []
            result = MIM.MIM(sentence, dic, 4)
            if len(result) != 0:
                a = ''
                for x in result:
                    a = a + x
                    a = a + ' '
                result_f.write(a)#写入文件处理
                result_f.write('\n')
        result_f.close()
        print(str(num) + ' is ok')
    except:
        print(str(num) + ' is not ok')
        print(txt_list[num])

    try:
        target_f = open(save_list[num], encoding='gb18030')
        data = target_f.read()
        pat = re.compile(r'\n')
        data = re.sub(pat, '', data)
        mode = re.compile(r' ')
        all_word = re.split(mode, data)
        word_num = len(all_word)
        target_f.close()
        # 放入set中，去除重复词
        word_list = set(all_word)

        idf_list.extend(list(word_list))

        word_list.remove('')
        # 统计并写入文件
        #target_f = open(save_list[num], 'a', encoding='gb18030')
        #for item in word_list:
        #    a = item + '(TF=' + str(all_word.count(item) / word_num) + ')   '
        #    target_f.write(a)
        #target_f.close()
    except:
        pass

    num = num + 1
#计算idf
m = collections.Counter()
for x in idf_list:
    m[x] = m[x] + 1

target_f = open(IDF, 'w', encoding='gb18030')
for word in set(idf_list):
    a = word + '(IDF=' + str(math.log(4218/m[word])) + ')\n'
    target_f.write(a)
target_f.close()
#在文件中写入idf*tf值
num = 0
while(num < len(txt_list)):
    try:
        target_f = open(save_list[num], encoding='gb18030')
        data = target_f.read()
        pat = re.compile(r'\n')
        data = re.sub(pat, ' ', data)
        mode = re.compile(r' ')
        all_word = re.split(mode, data)
        word_num = len(all_word)
        target_f.close()
        # 放入set中，去除重复词
        word_list = set(all_word)

        word_list.remove('')
        # 统计并写入文件
        target_f = open(save_list[num], 'a', encoding='gb18030')
        for item in word_list:
            a = item + '(TF*IDF=' + str((all_word.count(item) / word_num) * math.log(4218/m[item])) + ')\n'
            target_f.write(a)
        target_f.close()
    except:
        pass
    num = num + 1

