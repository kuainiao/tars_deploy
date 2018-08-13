#!/usr/bin/python
# encoding: utf-8

import ConfigParser
import commands
import tarsLog
import socket
import fcntl
import struct
import os

log = tarsLog.getLogger()
def getIpAddress(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def getLocalIp():
    return getIpAddress("eth0")

def getBaseDir():
    cwd = os.getcwd()
    log.info("  os.getcwd() is {}".format(cwd))
    path = os.path.abspath(os.path.join(os.getcwd(), ".."))
    return path

def doCmd(cmd):
    log.info(" execute cmd  start ,cmd : {}".format(cmd))
    result = dict()
    (status, output) = commands.getstatusoutput(cmd)
    result["status"] = status
    result["output"] = output
    log.info(" execute cmd  end ,cmd : {},status :{} , output: {}".format(cmd,status,output))
    if (0 != status):
        raise Exception("execute cmd  error ,cmd : {}, status is {} ,output is {}".format(cmd,status, output))
    return result

def doCmdIgnoreException(cmd):
    log.info(" execute cmd  start ,cmd : {}".format(cmd))
    result = dict()
    (status, output) = commands.getstatusoutput(cmd)
    result["status"] = status
    result["output"] = output
    log.info(" execute cmd  end ,cmd : {},status :{} , output: {}".format(cmd, status, output))
    return result

def getCommProperties(paramsKey):
    baseDir = getBaseDir()
    cf = ConfigParser.ConfigParser()
    propertiesDir =baseDir+"/tars_deploy/comm.properties"
    cf.read(propertiesDir)
    log.info(" commProperties is {} ".format(propertiesDir))
    cf.sections()
    value = cf.get('tarscomm', paramsKey)
    return value

if __name__ == '__main__':
    print(getIpAddress("eth0"))
    pass