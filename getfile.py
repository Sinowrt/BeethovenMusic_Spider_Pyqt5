import os
import requests
import time
import re
import urllib
import traceback

class Getfile(object):  #下载文件
    def __init__(self,url,path):
        self.url=url
        self.flag=True  #当self.flag=False，暂停或取消下载，也就是结束下载线程
        self.header_flag=False #当为True时，设置header，断点续传
        self.downfullPath = path
        self.headReaponseCode=int()

        try:
            print("headerUrl================"+url)
            self.re=requests.head(url,allow_redirects=True,timeout=20)  #运行head方法时重定向
            self.headReaponseCode=self.re.status_code
            if self.headReaponseCode == 404:
                self.clear0MFile()
                self.flag=False

        except:
            traceback.print_exc()


    def clear0MFile(self):
        try:
            if os.path.isfile(self.downfullPath):
                os.remove(self.downfullPath)
                if not os.listdir(os.path.dirname(self.downfullPath)):
                    os.rmdir(os.path.dirname(self.downfullPath))
                    print('移除空目录: ' + os.path.dirname(self.downfullPath))


        except:
            traceback.print_exc()

    def getsize(self):
        try:
            self.file_total=int(self.re.headers['Content-Length']) #获取下载文件大小    
            return self.file_total
        except:
            return -1

    def getdownfullPath(self):

        return self.downfullPath

    def getfilename(self):  #获取默认下载文件名
        if 'Content-Disposition' in self.re.headers:
            n=self.re.headers.get('Content-Disposition').split('name=')[1]
            filename=urllib.parse.unquote(n,encoding='utf8')
        else :
            filename=os.path.basename(self.re.url.split('?')[0])
        if filename=='':
            filename='index.html'
        return filename

    def downfile(self):  #下载文件
        self.headers={}
        self.mode='wb'
        self.isValidPath(self.downfullPath)


        print("i am downfile,i am downloading")
        if os.path.exists(self.downfullPath) :
            self.headers={'Range': 'bytes=%d-' %os.path.getsize(self.downfullPath) }
            self.mode='ab'
        self.r = requests.get(self.url,stream=True,headers=self.headers)

        # print(self.mode)
        try:
            with open(self.downfullPath, self.mode) as code:
                for chunk in self.r.iter_content(chunk_size=1024): #边下载边存硬盘
                    if chunk and self.flag:
                        code.write(chunk)
                    else:
                        break
        except:
            traceback.print_exc()


    def isValidPath(self,fullpath):
        path=os.path.dirname(fullpath)
        folder = os.path.exists(path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            try:
                os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
                print("folder successfully created!")
            except Exception as msg:
                print(msg)

        else:
            print("folder exit!")
        return

    def cancel(self,filename):  #取消下载
        self.flag=False
        time.sleep(1)
        if os.path.isfile(filename):
            os.remove(filename)


