#!/usr/bin/python
# encoding: utf-8
import comm.tarsLog as tarsLog
import comm.tarsUtil as tarsUtil
import shutil
def do():
    tarsUtil.doCmd("ps -aux|grep resin|grep -v grep|awk '{print \" kill -9\" ,$2}'|bash")
    #shutil.rmtree("/usr/local/app")
    return
if __name__ == '__main__':
    do()
    pass