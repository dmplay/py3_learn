# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import zipfile

def pathTset():
    print(os.path.join('usr', 'bin', 'spam'))
    print(os.getcwd())
    os.chdir('C:\\Windows\\System32')
    print(os.getcwd())
    print(os.path.abspath('.'))
    print(os.path.abspath('.\\Scripts'))
    print(os.path.isabs('.'))
    print(os.path.isabs(os.path.abspath('.')))
    print(os.path.relpath('C:\\Windows', 'C:\\'))

    path = 'D:\logs\dmplay\log2017-05-16.txt'
    print(os.path.basename(path))
    print(os.path.dirname(path))
    print(os.path.split(path))
    print((os.path.dirname(path), os.path.basename(path)))
    print(path.split(os.path.sep))

    print(os.path.getsize(path))
    print(os.listdir(os.path.dirname(path)))

    totalSize = 0
    for filename in os.listdir(os.path.dirname(path)):
        file_size=os.path.getsize(os.path.join(os.path.dirname(path), filename))
        totalSize = totalSize + file_size
        print(filename.ljust(20),str(file_size).rjust(10))
    print('total'.ljust(20),str(totalSize).rjust(10))

def fileTest():
    path = 'D:\logs\dmplay\log2017-05-16.txt'
    helloFile = open(path,encoding="utf-8")
    helloContent = helloFile.read()
    print(helloContent)

def fileWalk():
    for folderName, subfolders, filenames in os.walk('D:\\dmplay'):
        print('The current folder is ' + folderName)
        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')

def zipRead():
    exampleZip = zipfile.ZipFile('D:\\dmplay\\git.zip')
    list =exampleZip.namelist()
    print(list)
    spamInfo = exampleZip.getinfo('git/leetcode_java/LeetCode/src/com/play/easy/HammingDistance.java')
    print(spamInfo.file_size)
    print(spamInfo.compress_size)
    print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
    exampleZip.close()

    os.chdir('D:\\dmplay\\test')
    exampleZip = zipfile.ZipFile('D:\\dmplay\\git.zip')
    exampleZip.extractall()
    exampleZip.close()

    exampleZip = zipfile.ZipFile('D:\\dmplay\\git.zip')
    exampleZip.extract('git/leetcode_java/LeetCode/src/com/play/easy/HammingDistance.java')
    exampleZip.extract('git/leetcode_java/LeetCode/src/com/play/easy/HammingDistance.java', 'D:\\dmplay\\test\\zip')
    exampleZip.close()

def zipWrite():
    os.chdir('D:\\dmplay\\test')
    newZip = zipfile.ZipFile('new.zip', 'w')
    newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

def zipAppend():
    os.chdir('D:\\dmplay\\test')
    newZip = zipfile.ZipFile('new.zip', 'a')
    newZip.write('aha.txt', compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

if __name__=='__main__':
    zipAppend()