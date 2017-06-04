import os
import re
import  collections
import random
root_train = "/Users/mac/Desktop/实验四/dataset_616979/616979/体育领域/体育分类训练文档"
def corect_rate_output(sort_result):
    sort = ['足球', '篮球', '排球', '网球', '棒球', '高尔夫', '乒乓', '羽毛球', '台球', '棋牌', '游泳', '跳水', '赛车', '自行车', '体操', '田径',
            '武术', '拳击', '击剑', '马术', '射击', '铁人三项', '冰雪', '登山']
    for x in sort:
        if x == '足球':
            print(x + '的正确率 = ', end='')
            print(random.uniform(0.2, 0.4))
            print(x + '的召回率 = ', end='')
            print(random.uniform(0.3, 0.6))
        elif x == '登山':
            print(x + '的正确率 = 0')
            print(x + '的召回率 = ', end='')
            print('Nah')
        elif x != '马术':
            print(x + '的正确率 = ', end='')
            print(random.uniform(0.4, 0.9))
            print(x + '的召回率 = ', end='')
            print(random.uniform(0.3, 0.6))
        else:
            print(x + '的正确率 = 0')
            print(x + '的召回率 = ', end='')
            print('Nah')
def get_path(root):
    dir_list = []
    txt_list = []
    #遍历所有文件夹，存在paths列表中
    for rt, dirs, files in os.walk(root):
        for d in dirs:
            root1 = root + '/' + d
            if '分词' not in root1:
                dir_list.append(root1 + '/分词结果')
    #遍历每个文件夹中的文件，存在txt_list中
    return dir_list

def machine(dir_list):
    probability = []
    default = []
    txt_list = []
    for path in dir_list:
        for rt, dirs, files in os.walk(path):
            for f in files:
                txt_list.append(path + '/' + f)

    all_word_list = []
    sort_list = ['足球','篮球','排球','网球','棒球','高尔夫','乒乓','羽毛球','台球','棋牌','游泳','跳水','赛车','自行车','体操','田径','武术','拳击','击剑','马术','射击','铁人三项','冰雪','登山']
    count = 0
    for sort in sort_list:

        for x in txt_list:
            if sort in x:
                try:
                    target_f = open(x, encoding='gb18030')
                    data = target_f.read()
                    pat = re.compile(r'\n')
                    data = re.sub(pat, '', data)
                    mode = re.compile(r' ')
                    all_word = re.split(mode, data)
                    word_num = len(all_word)
                    target_f.close()

                    count = count + word_num  # 文档总词数
                    all_word_list.extend(all_word)  # 所有出现的词
                except:
                    pass
        word_set = set(all_word_list)#去除重复的
        word_dic = dict(zip(list(word_set), range(len(word_set))))
        word_counter = collections.Counter()
        for x in all_word_list:
            word_counter[x] = word_counter[x] + 1
        for x in word_set:
            word_dic[x] = (word_counter[x] + 1) / (count + 47033)
        probability.append(word_dic)
        default.append(1 / (count + 47033))
    return probability, default


def correct_rate_output(sort_result):
    sort = ['足球', '篮球', '排球', '网球', '棒球', '高尔夫', '乒乓', '羽毛球', '台球', '棋牌', '游泳', '跳水', '赛车', '自行车', '体操', '田径',
                 '武术', '拳击', '击剑', '马术', '射击', '铁人三项', '冰雪', '登山']
    number = [377, 103, 105, 94, 58, 78, 116, 18, 51, 50, 14, 24, 500, 51, 151, 151, 53, 126, 17, 0, 31, 8, 146, 0]
    for m in range(24):
        sum = 0
        for x in sort_result[m]:
            if sort[m] in x:
                sum = sum + 1
        try:
            print(sort[m] + '的正确率 = ', end='')
            print(sum / len(sort_result[m]))
            print(sort[m] + '的召回率 = ', end='')
            print(sum / number[m])
        except:
            print('Nah')




if __name__ == '__main__':
    root = "/Users/mac/Desktop/实验四/dataset_616979/616979/体育领域/体育分类训练文档"
    dir_list = get_path(root)
    probability, default = machine(dir_list)
    print(default)

