#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:50:20 2018

@author: hanmufu
"""

import os
import logging
logger_name = "myLog"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# 获取文件夹下除了隐藏文件之外的文件
def getLocalNormalFiles():
    listFiles = os.listdir(os.getcwd())
    localFiles = []
    # 获取文件夹下所有分文件夹的名字
    for i in range(len(listFiles)):
        if listFiles[i][0] != '.':
            localFiles.append(listFiles[i])
    return localFiles

def rmTempFiles():
    listFiles = os.listdir(os.getcwd())
    for i in range(len(listFiles)):
        if listFiles[i][0:13] == 'videoCapturer':
            os.system("rm %s" % listFiles[i])

# e.g. hanmufu
usr = (os.getcwd().split('/'))[2]
# e.g. /Users/hanmufu
usr_path = '/Users/%s' % usr

# 进入腾讯视频下载文件夹
os.chdir("%s/Library/Containers/com.tencent.tenvideo/Data/Library/Application Support/Download/video" % usr_path)
# 进入地球脉动第二集的文件夹
os.chdir("./q0022m7d26n.321004.hls")
Folders = getLocalNormalFiles()
# 遍历所有分文件夹，并合并
for i in range(len(Folders)):
    os.chdir("./%s" % Folders[i])
    rmTempFiles()
    videos = getLocalNormalFiles()
    videos.sort(key= lambda x:int(x[:-3]))
    cmd_allVideosInOneFolder = ' '.join(videos)
    logging.info("..floder \"%s\" has been done" % Folders[i])
    os.system("cat %s > %s/Downloads/videoCapturer%s.ts" % (cmd_allVideosInOneFolder, usr_path, str(int(int(videos[0][:-3]) / 30))))
    os.chdir("..")
allCapturedVideos = []
for i in range(len(Folders)):
    allCapturedVideos.append("videoCapturer%s.ts" % i)
cmd_allCapturedVideos = ' '.join(allCapturedVideos)
os.chdir("%s/Downloads" % usr_path)
os.system("cat %s > enjoy.ts" % cmd_allCapturedVideos)
logging.info("...videos has been put together")
rmTempFiles()
logging.info("...deleted temp files")
logging.info("...ALL DONE")
#print("ALL DONE")
    

