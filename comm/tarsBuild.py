#!/usr/bin/python
# encoding: utf-8
import subprocess
import tarsLog
from tarsUtil import *
log = tarsLog.getLogger()
def do():
    build()
    return

def build():
    baseDir = getBaseDir()
    doCmd("{}/cpp/build/build.sh cleanall".format(baseDir))
    rCode = buildCmd("{}/cpp/build/build.sh all".format(baseDir))
    if rCode == 0:
        log.info(" build success !!!")
    else:
        log.info(" build error !!!")
    return

def buildCmd(cmd):
    rCode=0
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            print line
           #log.info(line)
    if p.returncode == 0:
        rCode =0
    else:
        rCode=-1
    p.stdin.close()
    p.stdout.close()
    return rCode

if __name__ == '__main__':
    pass