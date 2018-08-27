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
    for server in checkServer:
        log.infoPrint(" check and install server {}".format(server))
        installIfNotExistsByYum(server)
    return

def hasInstallServer(server):
    (rCode,msg) = doCmd("which {}".format(server))
    if rCode == 0:
        return True
    else:
        return False
    return

def installIfNotExistsByYum(server):
    if hasInstallServer("yum"):
        os.system("yum install  -y {}".format(server))
    return

if __name__ == '__main__':
    pass