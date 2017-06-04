root_test = "/Users/mac/Desktop/实验四 6/dataset_616979/616979/体育领域/体育分类测试文档"
root_train = "/Users/mac/Desktop/实验四 6/dataset_616979/616979/体育领域/体育分类训练文档"
from 分词 import Dictionary
from 分词 import Text
from 分词 import Findpath
from 分词 import Sort

#统计训练文档数占总文档数的比
txt_n = []
txt_percentage = Findpath.get_percentage(root_train)
#首先遍历目标目录，返回文件夹列表和txt列表
#txt_list和save_list中序号相同
txt_list = Findpath.get_path(root_train)
txt_list = list(set(txt_list))
save_list = []
for x in txt_list:
    path = x.split('/')
    url = ''
    for x in range(10):
        url = url + path[x] + '/'
    save_list.append(url + '分词结果/' + path[-1])
#1.生成字典,并去除停止词
pure_dic = dict()
pure_dic = Dictionary.pure()
#2.对训练集进行分词
Text.split(txt_list, save_list, pure_dic)
#创建分类器
probability, default = Sort.machine(Sort.get_path(root_train))
#创建储存分类结果的二维列表
sort_result = [[0 for i in range(0)] for i in range(24)]
#对测试文档分词
txt_list = []
txt_list = Findpath.get_path(root_test)
txt_list = list(set(txt_list))
save_list = []
for x in txt_list:
    path = x.split('/')
    url = ''
    for x in range(10):
        url = url + path[x] + '/'
    save_list.append(url + '分词结果/' + path[-1])
Text.split(txt_list, save_list, pure_dic)
#对save_list中的文件进行分类的计算
for path in save_list:
    all_word = Text.get_words(path)
    Text.make_choice(path, all_word, probability, default, txt_percentage, sort_result)
Sort.corect_rate_output(sort_result)



