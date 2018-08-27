#!/usr/bin/python
# encoding: utf-8
import sys
import os
import tarsLog
from tarsUtil import *
log = tarsLog.getLogger()
checkServer =["git","gcc","gcc-c++","yasm","glibc-devel","flex","bison","cmake","ncurses-devel","zlib-devel","autoconf"]
def do():
    check()
    return

def check():
    if not hasInstallServer("yum"):
        log.infoPrint("yum cannot work,please check it .")
        return
    for server in checkServer:
        log.infoPrint(" check and install server {}".format(server))
        installIfNotExistsByYum(server)
    return

def hasInstallServer(server):
    (rCode,msg) = doCmd("which {}".format(server))
    log.infoPrint(" cmd  which yum  rCode is {} ,msg is {}".format(rCode,msg))
    if rCode == 0:
        return True
    else:
        return False

def installIfNotExistsByYum(server):
    os.system("yum install  -y {}".format(server))
    return

if __name__ == '__main__':
    pass