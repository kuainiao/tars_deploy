#!/usr/bin/python
# encoding: utf-8

import ConfigParser
import commands
import tarsLog
import socket
import fcntl
import struct
import os
import shutil

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

def copytree(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2,
             ignore_dangling_symlinks=False):
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()
    if not os.path.exists(dst):
        os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.islink(srcname):
                linkto = os.readlink(srcname)
                if symlinks:
                    # We can't just leave it to `copy_function` because legacy
                    # code with a custom `copy_function` may rely on copytree
                    # doing the right thing.
                    os.symlink(linkto, dstname)
                    shutil.copystat(srcname, dstname, follow_symlinks=not symlinks)
                else:
                    # ignore dangling symlink if the flag is on
                    if not os.path.exists(linkto) and ignore_dangling_symlinks:
                        continue
                    # otherwise let the copy occurs. copy2 will raise an error
                    if os.path.isdir(srcname):
                        copytree(srcname, dstname, symlinks, ignore,
                                 copy_function)
                    else:
                        shutil.copy_function(srcname, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks, ignore, copy_function)
            else:
                # Will raise a SpecialFileError for unsupported file types
                shutil.copy_function(srcname, dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except shutil.Error as err:
            errors.extend(err.args[0])
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
    try:
        shutil.copystat(src, dst)
    except OSError as why:
        # Copying file access times may fail on Windows
        if getattr(why, 'winerror', None) is None:
            errors.append((src, dst, str(why)))
    if errors:
        raise shutil.Error(errors)
    return dst

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