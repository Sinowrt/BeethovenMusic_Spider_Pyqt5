# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QCheckBox,QProgressBar,QTableWidgetItem


from Spider import *
import getfile
import re
import threading
import threadpool
import time
import os

class Ui_MainWindow(QObject):
    insert_signal = pyqtSignal(str)
    updatespeed_signal=pyqtSignal(str,int)
    updateprogress_signal=pyqtSignal(int,int)
    updatatotalProgress_signal=pyqtSignal(float)
    updateStatue_signal=pyqtSignal(str)
    updaterest_signal=pyqtSignal(str)
    clearTable_signal=pyqtSignal()
    showMessageBox_signal=pyqtSignal(str)
    updateSize_signal=pyqtSignal(int,str)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1000, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        QMessageBox.about(self.centralwidget, "Info","版本：2018.11.30\n新特性：\n1.解决网络异常闪退问题\n2.增强版断点续存\nEnjoy it！")
        self.setupUiItems(MainWindow)


    def setupUiItems(self,MainWindow):
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 40, 331, 491))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 540, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 540, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 540, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 150, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 10, 91, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 540, 54, 20))
        self.label_4.setObjectName("label_4")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(400, 540, 591, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 32, 401, 41))
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(850, 40, 75, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(840, 80, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(350, 80, 300, 16))
        self.label_10.setObjectName("label_10")

        self.initVar()
        self.table_setup()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(self.multipleThread)
        self.pushButton_4.clicked.connect(self.initThread)
        self.pushButton_5.clicked.connect(self.browsePath)
        self.pushButton.clicked.connect(self.selectAll)
        self.pushButton_2.clicked.connect(self.unSelectAll)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.insert_signal.connect(self.insert_table)
        self.updatespeed_signal.connect(self.updata_speed)
        self.updateprogress_signal.connect(self.update_progress)
        self.updatatotalProgress_signal.connect(self.updata_totalProgress)
        self.spider.updateProcessor_signal.connect(self.updata_totalProgress)
        self.updateStatue_signal.connect(self.updateStatue)
        self.updaterest_signal.connect(self.update_rest)
        self.clearTable_signal.connect(self.clear_table)
        self.showMessageBox_signal.connect(self.showMessageBox)
        self.updateSize_signal.connect(self.updateSize)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "I am Spider!"))
        self.pushButton.setText(_translate("MainWindow", "全选"))
        self.pushButton_2.setText(_translate("MainWindow", "全不选"))
        self.pushButton_3.setText(_translate("MainWindow", "下载所选"))
        self.label.setText(_translate("MainWindow", "仪表盘"))
        self.label_2.setText(_translate("MainWindow", "资源列表"))
        self.pushButton_4.setText(_translate("MainWindow", "资源导入"))
        self.label_4.setText(_translate("MainWindow", "总进度"))
        self.label_5.setText(_translate("MainWindow", "当前路径:"))
        self.pushButton_5.setText(_translate("MainWindow", "浏览"))
        self.label_7.setText(_translate("MainWindow", "剩余："))
        self.label_10.setText(_translate("MainWindow", "状态："))
        self.display_table.setSortingEnabled(False)
        self.progressBar_2.setValue(0)
        item = self.display_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.display_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "曲目"))
        item = self.display_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "速度"))
        item = self.display_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "已下载/全部"))
        item = self.display_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "进度"))

    def updateStatue(self,str):
        self.label_10.setText("状态："+str)


    def multipleThread(self):
        self.downloadFlag=False
        self.pool.dismissWorkers(len(self.func_var),do_join=True)

        button = QMessageBox.question(self.centralwidget, "提示", "由于程序尚未完善，点击“下载所选”将立即下载所有选择的曲目，无法停止（除了关闭窗口），确定下载吗？",
                                      QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)

        if button == QMessageBox.Ok:
            self.downloadFlag=True
            self.clearTable_signal.emit()
            self.generateFunc_var()
            self.updatatotalProgress_signal.emit(0)
            downloadListSize = len(self.downLoadList)
            if downloadListSize == 0:
                self.showMessageBox_signal.emit('未选择任何项目！')
            else:
                if self.downLoadPath != '':
                    self.updateStatue_signal.emit("正在下载...当前最大下载线程数为" + str(self.downloadThreadNum))
                    self.pool = threadpool.ThreadPool(self.downloadThreadNum)
                    requests = threadpool.makeRequests(self.download, self.func_var)
                    [self.pool.putRequest(req) for req in requests]
                    self.pool.poll()
                else:
                    self.showMessageBox_signal.emit('请设置下载路径')
        else:
            return

    def initVar(self):
        self.downLoadList=list()
        self.downLoadPath=str()
        self.func_var=[]
        self.pool=threadpool.ThreadPool(2)
        self.tableRow=0
        self.downloadTotal=0
        self.downLoadRest=0
        self.spider=Spider()
        self.downloadThreadNum=10
        self.downloadFlag=True

    def selectAll(self):
        self.setSelect(Qt.Checked)


    def unSelectAll(self):
        self.setSelect(Qt.Unchecked)


    def setSelect(self,flag):
        root = self.treeWidget.invisibleRootItem()
        signal_count = root.childCount()

        for i in range(signal_count):
            signal = root.child(i)
            num_children = signal.childCount()
            for n in range(num_children):
                child = signal.child(n)
                num_xchildren=child.childCount()
                for n in range(num_xchildren):
                    xchild = child.child(n)
                    xchild.setCheckState(0, flag)

    def download(self,url,currentPath,row):
        time.sleep(1)
        self.insert_signal.emit(self.downLoadList[row]['songName'])

        if not re.match('^(https?|ftp)://.+$',url):
            self.updatespeed_signal.emit('无效的网址或目标路径',row)
        else:
            try:
                gf=getfile.Getfile(url)
            except Exception as e:
                self.updatespeed_signal.emit('无法访问该网址',row)
                gf.flag=False
                return
            #name=gf.getfilename()

            self.progressbar_thread(gf,row,currentPath)

            self.downLoadRest = self.downLoadRest - 1
            self.updatatotalProgress_signal.emit((self.downloadTotal-self.downLoadRest )/ self.downloadTotal * 100)
            self.updaterest_signal.emit(str(self.downLoadRest))

            if self.downLoadRest == 0:
                self.updateStatue_signal.emit("下载完毕!")
            return

    def generateFunc_var(self):
        self.downLoadList=self.find_checked()
        self.func_var.clear()
        self.downloadTotal=len(self.downLoadList)
        self.downLoadRest=self.downloadTotal

        print(self.downLoadList)
        if self.downLoadPath != '':
            index=0

            self.updaterest_signal.emit(str(self.downLoadRest))
            for temp in self.downLoadList:
                print("==========generate start!")
                if index % 100 == 0:
                    self.updateStatue_signal.emit("正在生成线程池参数"+str(index))
                    self.updatatotalProgress_signal.emit(index/self.downloadTotal*100)
                list=[]
                currentPath=self.downLoadPath+"/"+temp['artistName']+"/"+temp['series']+"/"+temp['songName']+".mp3"
                currentDownLoadUrl=temp['songUrl']

                list.append(currentDownLoadUrl)
                list.append(currentPath)
                list.append(index)

                self.func_var.append((list,None))
                index=index+1
                print("==========generate complete!"+str(index))
        return

    def progressbar_thread(self,gf, index,currentPath):
        t2 = threading.Thread(target=gf.downfile, args=(currentPath,))
        t2.setDaemon(True)
        t2.start()
        time.sleep(1)

        file_size = 0
        file_total = gf.getsize()  # 获取下载文件大小
        filename=gf.getdownfullPath()
        speed0Time=time.time()
        flag = True

        if file_total == -1:
            self.updatespeed_signal.emit('获取文件大小失败', index)
            return

        while file_size < file_total and gf.flag:
            #print(filename)
            time.sleep(1)
            speedValue=0
            speed=str()

            if os.path.exists(filename):
                speedValue=(os.path.getsize(filename) - file_size) / 1024
                speed=str(speedValue)+'KB/S'
                try:
                    file_size = os.path.getsize(filename)
                except:
                    file_size = 0

            if speedValue == 0 and flag:
                speed0Time=time.time()
                flag=False
            elif speedValue!=0:
                flag=True

            if time.time()-speed0Time>(60) and (not flag):
                print("================================I am redownloading!"+str(index))
                gf.flag=False
                time.sleep(1)
                gf.flag=True
                t2 = threading.Thread(target=gf.downfile, args=(currentPath,))
                t2.setDaemon(True)
                t2.start()
            else:
                self.updatespeed_signal.emit(speed, index)

            self.updateprogress_signal.emit(file_size / file_total * 100,index)
            self.updateSize_signal.emit(index,'{:.1f}M/{:.1f}M'.format(file_size / 1024 / 1024, file_total / 1024 / 1024))

            if self.downloadFlag==False:
                gf.flag=False

        #print("totalsize======"+str(file_total)+"||||||||downloaded=============="+str(file_size))
        if file_size >= file_total:
            self.updatespeed_signal.emit('下载完毕', index)

    def updata_totalProgress(self,percent):
        self.progressBar_2.setValue(percent)

    def updateSize(self,row,str):
        self.display_table.setItem(row, 3, QTableWidgetItem(str))

    def update_rest(self,str):
        self.label_7.setText("剩余："+str+"首")



    def showMessageBox(self,str):
        QMessageBox.information(self.centralwidget, '错误', str, QMessageBox.Yes, QMessageBox.Yes)




    def update_progress(self,percent,index):
        self.display_table.cellWidget(index,4).setValue(percent)

    def updata_speed(self,speed,index):
        self.display_table.setItem(index,2,QTableWidgetItem(str(speed)))

    def browsePath(self):
        path= QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget,"选取文件夹","./")
        if path != '':
            self.downLoadPath=path+"/music"
            self.label_5.setText("当前路径:"+self.downLoadPath)
        return

    def initThread(self):
        t1 = threading.Thread(target=self.init, args=())
        t1.setDaemon(True)
        t1.start()

    def init(self):
        self.updateStatue_signal.emit("正在获取资源列表...")
        self.treeWidget.clear()
        list=self.spider.get_all_artists_song()

        print(len(list))
        for i in list:
            parent = QtWidgets.QTreeWidgetItem(self.treeWidget)
            parent.setText(0, i['artistName'])
            parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            for m in i['seriesList']:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, m['series'])
                child.setFlags(child.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
                for n in m['songList']:
                    xchild = QtWidgets.QTreeWidgetItem(child)
                    xchild.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                    xchild.setText(0, n['songName'])
                    xchild.setText(1, n['songUrl'])
                    xchild.setCheckState(0, Qt.Unchecked)
        # self.find_checked()

        self.treeWidget.show()
        self.updateStatue_signal.emit("资源列表加载完毕！")
        return

    def find_checked(self):
        root = self.treeWidget.invisibleRootItem()
        # print(root.child(0).text(1))
        signal_count = root.childCount()
        checked_sweeps = list()
        for i in range(signal_count):
            signal = root.child(i)
            artist = signal.text(0)
            num_children = signal.childCount()
            for n in range(num_children):
                child = signal.child(n)
                num_xchildren=child.childCount()
                series=child.text(0)
                for n in range(num_xchildren):
                    xchild = child.child(n)
                    if xchild.checkState(0) == QtCore.Qt.Checked:
                        checked = dict()
                        songName = xchild.text(0)
                        songUrl = xchild.text(1)
                        print(xchild.text(1))
                        checked['artistName'] = artist
                        checked['series'] = series
                        checked['songName'] = songName
                        checked['songUrl'] = songUrl
                        checked_sweeps.append(checked)
        return checked_sweeps

    def table_setup(self):
        self.display_table = QtWidgets.QTableWidget(self.centralwidget)
        self.display_table.setGeometry(QtCore.QRect(350, 100, 641, 431))
        self.display_table.setObjectName("display_table")
        self.display_table.setColumnCount(5)
        self.display_table.setRowCount(0)
        self.display_table.setEnabled(True)

        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.display_table.setFont(font)
        self.display_table.setAutoFillBackground(False)
        self.display_table.setStyleSheet("border-image: None;\n"
                                         "background-color:rgba(0, 0, 0,0.3);\n"
                                         "font: 10pt \"幼圆\";\n"
                                         "\n"
                                         "selection-background-color: rgba(0, 0, 0,0.5);\n"
                                         "selection-color: rgb(255, 255, 255);\n"
                                         "gridline-color: white;\n"
                                         "color:white;\n"
                                         "border-radius:10px;")
        self.display_table.setAutoScroll(True)
        self.display_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.display_table.setAlternatingRowColors(False)
        self.display_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.display_table.setShowGrid(False)
        self.display_table.setGridStyle(QtCore.Qt.SolidLine)


        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(4, item)

        self.display_table.horizontalHeader().setVisible(True)
        self.display_table.horizontalHeader().setCascadingSectionResizes(False)
        self.display_table.horizontalHeader().setHighlightSections(False)
        self.display_table.horizontalHeader().setSortIndicatorShown(False)
        self.display_table.verticalHeader().setVisible(False)
        self.display_table.verticalHeader().setDefaultSectionSize(37)
        self.display_table.verticalHeader().setHighlightSections(True)
        self.display_table.verticalHeader().setSortIndicatorShown(False)
        self.display_table.verticalHeader().setStretchLastSection(False)

        self.display_table.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical{"  # 垂直滑块整体  
            "padding-top:20px;"  # 上预留位置（放置向上箭头）  
            "padding-bottom:20px;"  # 下预留位置（放置向下箭头）  
            "padding-left:3px;"  # 左预留位置（美观）  
            "padding-right:3px;"  # 右预留位置（美观）  
            "border-left:1px solid white;}"  # 左分割线  
            "QScrollBar::handle:vertical{"  # 滑块样式  
            "background:rgba(100,100,100,0.3);"  # 滑块颜色  
            "border-radius:6px;"  # 边角圆润  
            "min-height:60px;}"  # 滑块最小高度  
            "QScrollBar::handle:vertical:hover{"  # 鼠标触及滑块样式  
            "background:rgba(0,0,0,0.3);}"  # 滑块颜色  
            "QScrollBar::add-line:vertical{"  # 向下箭头样式  
            "background:;}"
            "QScrollBar::sub-line:vertical{"  # 向上箭头样式  
            "background:;}")
        self.display_table.horizontalScrollBar().setStyleSheet(
            "QScrollBar:vertical{"  # 垂直滑块整体  
            "padding-top:20px;"  # 上预留位置（放置向上箭头）  
            "padding-bottom:20px;"  # 下预留位置（放置向下箭头）  
            "padding-left:3px;"  # 左预留位置（美观）  
            "padding-right:3px;"  # 右预留位置（美观）  
            "border-left:1px solid white;}"  # 左分割线  
            "QScrollBar::handle:vertical{"  # 滑块样式  
            "background:rgba(100,100,100,0.3);"  # 滑块颜色  
            "border-radius:6px;"  # 边角圆润  
            "min-height:60px;}"  # 滑块最小高度  
            "QScrollBar::handle:vertical:hover{"  # 鼠标触及滑块样式  
            "background:rgba(0,0,0,0.3);}"  # 滑块颜色  
            "QScrollBar::add-line:vertical{"  # 向下箭头样式  
            "background:;}"
            "QScrollBar::sub-line:vertical{"  # 向上箭头样式  
            "background:;}")
        self.display_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background:rgba(0,0,0,0.1); padding-left:4px; border:1px solid white; }"
            # "QHeaderView::section:checked{background-color:green; }"
        )
        self.display_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{background:rgba(0,0,0,0.1); padding-left:4px; border:1px solid white; }"
            # "QHeaderView::section:checked{background-color:green; }"
        )
        self.display_table.setColumnWidth(0, 40)
        self.display_table.setColumnWidth(1, 210)
        self.display_table.setColumnWidth(2, 80)
        self.display_table.setColumnWidth(3, 100)
        self.display_table.setColumnWidth(4, 200)


    def clear_table(self):
        while self.display_table.rowCount():
            self.display_table.removeRow(0)
        self.tableRow=0


    def insert_table(self,title):
        progress = QProgressBar()
        row = self.display_table.rowCount()
        self.display_table.insertRow(row)
        self.display_table.setRowHeight(row,25)

        self.display_table.setItem(row, 0, QTableWidgetItem(str(row)))
        self.display_table.setItem(row, 1, QTableWidgetItem(str(title)))
        self.display_table.setItem(row, 2, QTableWidgetItem("KB/S"))
        self.display_table.setItem(row, 3, QTableWidgetItem("--M/--M"))
        self.display_table.setCellWidget(row, 4, progress)





