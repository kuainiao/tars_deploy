#!/usr/bin/python
# encoding: utf-8
import subprocess
import tarsLog
import os
import requests
from tarsUtil import *
log = tarsLog.getLogger()
def do():
    (rCode,msg) = testRegistry()
    if rCode !=0:
        log.infoPrin(msg)
        return (rCode,msg)
    (rCode,msg) = testNode()
    if rCode !=0:
        log.infoPrin(msg)
        return (rCode,msg)
    (rCode,msg) = testWeb()
    if rCode !=0:
        log.infoPrin(msg)
        return (rCode,msg)
    (rCode,msg) = testFrameServer()
    if rCode !=0:
        log.infoPrin(msg)
        return (rCode,msg)
    log.infoPrin("TARS DEPLOY  SUCCESS!")
    return

def testRegistry():
    return (0,"")

def testNode():
    return (0,"")

def testWeb():
    return testByWebInterface("","")

def testFrameServer():
    return (0,"")

def testByWebInterface(url,params):
    url ="http://111.230.151.221:8080/pages/server/api/send_command?server_ids=2&command=tars.viewversion"
    result = requests.get(url,data=postJson)
    resultJson = result.json()
    if(resultJson["ret_code"]!=200):
        return (-1,"tarweb cannot ")
    else:
        if resultJson["data"].find("succ")=-1:
            return (-1,"get tarsversion fail,please check")
    return (0,"")

if __name__ == '__main__':
    pass