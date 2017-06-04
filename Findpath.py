import os
def get_path(root):
    dir_list = []
    txt_list = []
    #遍历所有文件夹，存在paths列表中
    for rt, dirs, files in os.walk(root):
        for d in dirs:
            root1 = root + '/' + d
            dir_list.append(root1)
    #遍历每个文件夹中的文件，存在txt_list中
    for path in dir_list:
        for rt, dirs, files in os.walk(path):
            for f in files:
                txt_list.append(path + '/' +  f)
    return txt_list
def rename(root):
    dir_list = []
    for rt, dirs, files in os.walk(root):
        for d in dirs:
            root1 = root + '/' + d
            if '分词结果' not in d:
                dir_list.append(root1)
    #遍历每个文件夹中的文件，存在txt_list中
    for path in dir_list:
        path = str(path)
        count = 0
        a = path.split('/')
        for rt, dirs, files in os.walk(path):
            for f in files:
                try:
                    if 'DS' not in f:
                        os.rename(path + '/' + f, path + '/' + a[-1] + str(count) + '.txt')
                        count = count + 1
                except:
                    pass
def get_percentage(root):
    dir_list = []
    txt_n = []
    num = 0
    sum = 0
    # 遍历所有文件夹，存在paths列表中
    for rt, dirs, files in os.walk(root):
        for d in dirs:
            if '分词结果' not in d:
                root1 = root + '/' + d
                dir_list.append(root1)
    # 遍历每个文件夹中的文件，存在txt_list中
    for path in dir_list:
        txt_n.append(0)
        for rt, dirs, files in os.walk(path):
            for f in files:
                txt_n[num] = txt_n[num] + 1
        num = num + 1
    for x in txt_n:
        sum = sum + x
    result = []
    for x in txt_n:
        x = x / sum
        result.append(x)
    return result
if __name__ == '__main__':
    root = "/Users/mac/Desktop/实验四 6/dataset_616979/616979/体育领域/体育分类测试文档"
    # 对测试文档重命名
    rename(root)

