import os
import requests
import time
import re
import urllib
import traceback

class Getfile(object):  #下载文件
    def __init__(self,url):
        self.url=url
        self.flag=True  #当self.flag=False，暂停或取消下载，也就是结束下载线程
        self.header_flag=False #当为True时，设置header，断点续传
        try:
            print("headerUrl================"+url)
            self.re=requests.head(url,allow_redirects=True,timeout=20)  #运行head方法时重定向
        except:
            traceback.print_exc()

        self.downfullPath=str()
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
    def downfile(self,filename):  #下载文件
        self.headers={}
        self.mode='wb'
        self.isValidPath(filename)
        self.downfullPath=filename

        print("i am downfile,i am downloading")
        if os.path.exists(filename) :
            self.headers={'Range': 'bytes=%d-' %os.path.getsize(filename) }
            self.mode='ab'
        self.r = requests.get(self.url,stream=True,headers=self.headers)

        print(self.mode)
        with open(filename, self.mode) as code:
            for chunk in self.r.iter_content(chunk_size=1024): #边下载边存硬盘
                if chunk and self.flag:
                    code.write(chunk)
                else:
                    break
        time.sleep(1)


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


