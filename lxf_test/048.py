import os

def searchFiles(path,words):
    for x in os.listdir(path) :
        fullPath=os.path.join(path,x)
        if os.path.isdir(fullPath):
            searchFiles(fullPath,words)
        else:
            searchWords(fullPath,words)

def searchWords(filePath,words):
     with open(filePath, 'r', encoding='utf-8') as f:
        s=f.read()
        if s.find(words)>0:
            s=s.replace('cn.zhouyafeng.itchat4j','com.itchat4j')
            with open(filePath, 'w', encoding='utf-8') as w:
                w.write(s)
            

if __name__=='__main__':
    #print('abcds'.replace('ab','xy'))
    searchFiles('E:/Workspaces/MyEclipse/dm_wxchart/src/com/itchat4j','cn.zhouyafeng.itchat4j');
