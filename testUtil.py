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

def doCmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            print "Subprogram output: [{}]".format(line)
    if p.returncode == 0:
        print "Subprogram success"
    else:
        print "Subprogram failed"
    p.stdin.close()
    p.stdout.close()
    p.stderr.close()
    return


if __name__ == '__main__':
    doCmd("/data/tars_deploy/pout.sh")
    pass

