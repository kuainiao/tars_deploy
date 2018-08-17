#!/usr/bin/python
# encoding: utf-8
import os
import comm.tarsUtil as tarsUtil

def getAbabsolutePath():
    path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    return path

if __name__ == '__main__':
    #tarsUtil.doCmd("/data/tars_deploy/pout.sh")
    rcode = os.system("/data/tars_deploy/pout.sh")
    print rcode
    pass

