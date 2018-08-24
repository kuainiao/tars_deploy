#!/usr/bin/python
# encoding: utf-8
import subprocess
import tarsLog
import os
import requests
from tarsUtil import *
log = tarsLog.getLogger()
localIp = getLocalIp()
def do():
    (rCode,msg) = testRegistry()
    if rCode !=0:
        return (rCode,msg)
    (rCode,msg) = testNode()
    if rCode !=0:
        return (rCode,msg)
    (rCode,msg) = testWeb()
    if rCode !=0:
        return (rCode,msg)
    (rCode,msg) = testFrameServer()
    if rCode !=0:
        return (rCode,msg)
    return (0,"")

def testRegistry():
    return (0,"")

def testNode():
    return (0,"")

def testWeb():
    return testByInterface("/pages/tree","")

def testFrameServer():
    return (0,"")

def testByInterface(uri,params):
    url ="http://{}:8080/{}".format(localIp,uri)
    params["server_ids"]="2"
    params["command"]="tars.viewversion"
    result = requests.get(url,data=params)
    if(result.status_code!=200):
        return (-1,"tarweb cannot visit")
    else:
        if result.text.find("succ") == -1:
            return (-1,"get tarsversion fail,please check")
    return (0,"")

if __name__ == '__main__':
    pass