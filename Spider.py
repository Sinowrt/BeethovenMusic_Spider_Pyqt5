# -*- coding: utf-8 -*-


import json
import time

import sys
import urllib
import os
import re
import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import *
import lxml

class Spider(QObject):
    start_time = time.time()
    updateProcessor_signal = pyqtSignal(int)

    # 获取演奏家
    def get_all_artists(self):
        artistsUrl_list=list()
        url='http://47.92.145.115/list.html'
        print(url)
        web_data = requests.get(url)
        web_data.content.decode('utf-8')
        soup=BeautifulSoup(web_data.text,'html.parser')

        titleP = re.compile("artist/\S*");  # also match a-incontent a-title cs-contentblock-hoverlink

        content = soup.find_all(href=titleP);
        # print(content)
        for link in content:
            artistsUrl_list.append(link.get("href"))
            # print(link.get("href"));
        return artistsUrl_list

    # 获取所有演奏家的所有歌曲列表
    def get_all_artists_song(self):
        artistsUrl_list=self.get_all_artists()
        Artists_list=[]
        k=0

        count=0
        total=len(artistsUrl_list)

        for artistUrl in artistsUrl_list:
            ArtistItemDict={'artistUrl': artistUrl}
            url='http://47.92.145.115/'+artistUrl
            print(url)
            data=requests.get(url)
            data.encoding = 'utf-8'
            # data.content.decode('utf-8')

            soup = BeautifulSoup(data.text, 'lxml')
            res=soup.find_all("p", class_="lead")
            count=count+1
            artistName = artistUrl.replace("artist/", "").replace("/art.html", "")
            print(artistName)

            ArtistItemDict['artistName']=artistName

            Series_List=[]
            self.updateProcessor_signal.emit(count/total * 100)


            for i in res:
                SeriesItemDict = {'series': i.get_text().replace(":", "-").rstrip()}
                songList = []
                print(i.get_text())
                p=i.find_next_sibling()

                if not(len(p)>1):
                    p = i.find_next_sibling().find_next_sibling()

                while len(p) > 1:
                    songName = p.find('p').get_text()
                    src = p.find('audio').get('src')
                    url = "http://47.92.145.115/" + artistUrl
                    songUrl = url.replace("art.html", src)

                    SongDict = {'songName': songName, 'songUrl': songUrl}

                    print(songUrl)
                    print(p.find('p').get_text())
                    p = p.find_next_sibling()

                    songList.append(SongDict)
                print("===============================")
                SeriesItemDict['songList']=songList
                Series_List.append(SeriesItemDict)
            ArtistItemDict['seriesList']=Series_List
            Artists_list.append(ArtistItemDict)
            print(len(Artists_list))
            # k=k+1
            # if k==4:
            #     return Artists_list
        print(Artists_list)
        # list=Artists_list
        return Artists_list

    def DownloadModule(self):
        for m in self.series_list:

            path="D:/music/"+m['artistName']+"/"+m['title']
            name="/"+m['songName']+".mp3"
            print(path)
            self.isValidPath(path)

            try:
                self.start_time = time.time()
                urllib.request.urlretrieve(self.downloadUrl, path+name, self.Schedule)
            except:
                print('Download wrong~')
        return


    def Schedule(self,blocknum, blocksize, totalsize):
        speed = (blocknum * blocksize) / (time.time() - self.start_time)
        # speed_str = " Speed: %.2f" % speed
        speed_str = " Speed: %s" % self.format_size(speed)
        recv_size = blocknum * blocksize

        # 设置下载进度条
        f = sys.stdout
        pervent = recv_size / totalsize
        percent_str = "%.2f%%" % (pervent * 100)
        n = round(pervent * 50)
        s = ('#' * n).ljust(50, '-')
        f.write(percent_str.ljust(8, ' ') + '[' + s + ']' + speed_str)
        f.flush()
        time.sleep(0.5)
        f.write('\r')

    # 字节bytes转化K\M\G
    def format_size(self,bytes):
        try:
            bytes = float(bytes)
            kb = bytes / 1024
        except:
            print("传入的字节格式不对")
            return "Error"
        if kb >= 1024:
            M = kb / 1024
            if M >= 1024:
                G = M / 1024
                return "%.3fG" % (G)
            else:
                return "%.3fM" % (M)
        else:
            return "%.3fK" % (kb)

    def isValidPath(self,path):
        folder = os.path.exists(path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print("folder successfully created!")
        else:
            print("folder exit!")
        return

    # get_all_artists()
    # get_all_artists_song()



