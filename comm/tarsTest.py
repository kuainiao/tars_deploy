#!/usr/bin/python
# encoding: utf-8
import subprocess
import tarsLog
import os
import requests
from tarsUtil import *
log = tarsLog.getLogger()
#localIp = getLocalIp()
localIp = "172.16.0.17"
webPort = "8080"
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
    return testByInterface("/pages/tree","","tarspatch")

def testFrameServer():
    frameServer = [("tarspatch","1"),("tarsconfig","2"),("tarsnotify","20"),("tarsstat","23"),("tarsproperty","25"),("tarsqueryproperty","27"),("tarsquerystat","29")]
    for (serverName,serverId) in frameServer:
        log.infoPrint("test server {} start ".format(serverName))
        (retCode,msg) = testByInterface("/pages/server/api/send_command?server_ids={}&command=tars.viewversion".format(serverId),"","succ")
        if retCode != 0 :
            return (retCode,msg)
        else:
            log.infoPrint("server {} test success ".format(serverName))
    return (0,"")

def testByInterface(uri,params,indexKey):
    url ="http://{}:{}/{}".format(localIp,webPort,uri)
    log.info(url)
    result = requests.get(url,data=params)
    log.info(" url is {} ,statusCode is {} ,text is {} ".format(url,result.status_code,result.text))
    if(result.status_code!=200):
        return (-1,"test fail,tarweb cannot visit")
    else:
        if result.text.find(indexKey) == -1:
            return (-1,"test fail")
    return (0,"")

if __name__ == '__main__':
    pass