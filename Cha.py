from 分词 import Findpath
import re
import collections
import math

def character(root):
    txt_list = Findpath.get_path(root)
    save_list = []
    idf_list = []
    for x in txt_list:
        path = x.split('/')
        url = ''
        for x in range(10):
            url = url + path[x] + '/'
        save_list.append(url + '分词结果/' + path[-1])
    character = [0 for i in range(24)]
    num = 0
    while (num < len(save_list)):
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
            统计并写入文件
            target_f = open(save_list[num], 'a', encoding='gb18030')
            for item in word_list:
                a = item + '(TF=' + str(all_word.count(item) / word_num) + ')   '
            target_f.close()
        except:
            pass
        num = num + 1
    # 计算idf
    del idf_list[0]
    m = collections.Counter()
    for x in idf_list:
        m[x] = m[x] + 1
    num = 0
    while (num < len(txt_list)):
        try:
            target_f = open(save_list[num], encoding='gb18030')
            data = target_f.read()
            pat = re.compile(r'\n')
            data = re.sub(pat, ' ', data)
            mode = re.compile(r' ')
            all_word = re.split(mode, data)
            word_num = len(all_word)
            target_f.close()
            word_list = set(all_word)
            word_list.remove('')
            target_f = open(save_list[num], 'a', encoding='gb18030')
            target_f.close()
        except:
            pass
        num = num + 1
if __name__ == '__main__':
    root = "/Users/mac/Desktop/实验四/dataset_616979/616979/体育领域/体育分类训练文档"
    character(root)