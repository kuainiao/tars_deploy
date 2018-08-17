#!/usr/bin/python
# encoding: utf-8
import os
import comm.tarsUtil as tarsUtil
import subprocess
import sys
import time
import random
import re

def getAbabsolutePath():
    path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    return path

def doCom(cmd):
    popen = subprocess.Popen(cmd, stdout = subprocess.PIPE)
    while True:
        print popen.stdout.readline()
    return


if __name__ == '__main__':
    doCmd("/data/tars_deploy/pout.sh")
    pass

