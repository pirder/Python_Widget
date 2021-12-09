import os
import sys
import mmap


# 先加载所有文件 在进行文件的修改
ALLFILESPATH = []  # 所以文件路径 为空代表完成了所有的文件处理

# 输入名字 tom 或者 jeames 或者什么 将其修改为什么 对应长度吧

# 修改文件作者


def changeOneFile(path, maybeName, replaceName):

    changeResult = False
    file = os.open(path, os.O_RDWR)
    changeManager = mmap.mmap(file, 0)

    maybeNameData = str.encode(maybeName, 'utf-8')
    replaceNameData = str.encode(replaceName, 'utf-8')

    nameLenth = len(maybeName)
    findId = changeManager.find(maybeNameData, 0)

    if findId > 0:

        dateStr = " on 2021/11/28."
        dateStringStart = nameLenth + findId
        dateStringEnd = dateStringStart + len(dateStr)
        dataStr = changeManager[int(dateStringStart):int(dateStringEnd)]

        temp = replaceName + dataStr.decode('utf-8')
        replaceNameData = str.encode(temp, 'utf-8')

        changeManager.seek(findId)
        changeManager.write(replaceNameData)
        print("修改成功 路径为" + path + " 名字为 " + temp + "")
        changeResult = True
    else:
        print("" + path + "该文件暂无名字" + maybeName + "的作者")

    changeManager.close()
    os.close(file)
    return changeResult

# 加载所有的文件


def walkFile(filePath):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            file_path = os.path.join(root, f)
            file_ext = file_path.rsplit('.', maxsplit=1)
            if len(file_ext) != 2:
                continue
            if file_ext[1] == 'swift' or file_ext[1] == 'h' or file_ext[1] == 'm':
                ALLFILESPATH.append(file_path)
    print("文件总数" + str(len(ALLFILESPATH)) + "")


def replaceAllFilesAuthorName():
    while (len(ALLFILESPATH) > 0):
        file = ALLFILESPATH.pop()
        for key, value in developerDict.items():
            name = key
            replaceName = value
            result = changeOneFile(file, name, replaceName)
            print("key:" + key + "   value:" + value)
            if result == True:
                continue

# 反转字典 key value


def reverserDictionary(dict):
    for key, value in dict.items():
        name = key
        replaceName = value
        del dict[name]
        dict[replaceName] = name

# 打印字典内容


def printDictionary(dict):
    for key, value in dict.items():
        name = key
        replaceName = value
        print("key:" + key + "   value:" + value)


if __name__ == "__main__":

    # 因为此脚本使用的是 mmap内存映射修改 速度快 缺点在于不能增加字符 也就意味着 修改名字个数必须一致
    # 若需要修改 替换 changeOneFile函数实现就好了

    # 测试使用 是否成功 能否改回去
    isReverseOrNot = False

    developerDict = {
        "zhangyuhui": "priderszyh",
        "hello__zyh": "zyhpriders",
        "seeyou_zyh": "priders_cn"
    }
    # printDictionary(developerDict) //
    if isReverseOrNot:
        reverserDictionary(developerDict)

    # filePath = "/Users/priders/Documents/TESTPYTHON"
    if (len(sys.argv) >= 2):
        filePath = sys.argv[1]
        if os.path.isdir(filePath):
            walkFile(filePath)
            replaceAllFilesAuthorName()
        else :
            print("提供的参数不是文件夹呀！！！")
    else :
        print("请提供文件夹参数 第一个参数")
