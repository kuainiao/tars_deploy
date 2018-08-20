#!/usr/bin/python
# encoding: utf-8
import tarsLog
import shutil
import os
import sys
import stat
from tarsUtil import *
log = tarsLog.getLogger()
tarsDeploy = "/usr/local/app/tars"
tarsDeployFrameBasicServerList = ["tarsregistry", "tarsnode", "tarsAdminRegistry", "tarspatch","tarsconfig"]
#tarsDeployFrameCommServerList = ["tarsnotify", "tarsstat", "tarsproperty", "tarsquerystat", "tarsqueryproperty", "tarslog", "tarsauth"]
tarsDeployFrameCommServerList = []
baseDir = getBaseDir()
def do():
    log.infoPrint("initDB start ...")
    initDB()
    log.infoPrint("initDB success ")
    log.infoPrint("deploy frameServer start ...")
    deployFrameServer()
    log.infoPrint("deploy frameServer success ")
    log.infoPrint("deploy web start ... ")
    deployWeb()
    log.infoPrint("deploy web success")
    return

def getDBDir():
    dbDir = baseDir+"/cpp/framework/sql/"
    return dbDir

def deployFrameServer():
    for server in tarsDeployFrameBasicServerList:
        srcDir = "{}/cpp/build/framework/deploy/{}".format(baseDir,server)
        confDir = "{}/cpp/framework/deploy/{}".format(baseDir,server)
        dstDir = "/usr/local/app/tars/{}".format(server)
        log.infoPrint(" deploy {} start srcDir is {} , confDir is {} , dstDir is {}  ".format(server,srcDir,confDir,dstDir))
        copytree(srcDir,dstDir)
        log.infoPrint(" deploy {} copy srcDir sucess  ".format(server))
        copytree(confDir,dstDir)
        log.infoPrint(" deploy {} copy conf sucess  ".format(server))
        updateConf(server)
        log.infoPrint(" deploy {} update conf sucess  ".format(server))
        os.chmod(dstDir+"/util/start.sh",stat.S_IXGRP)
        doCmd(dstDir+"/util/start.sh".format(server))
        log.infoPrint(" deploy {}  sucess".format(server))

    for server in tarsDeployFrameCommServerList:
        srcDir = "{}/cpp/build/framework/deploy/{}".format(baseDir,server)
        confDir = "{}/cpp/framework/deploy/{}".format(baseDir, server)
        dstDir = "/usr/local/app/tars/{}/bin/".format(server)
        if not os.path.exists(dstDir):
            os.makedirs(dstDir)
        shutil.copyfile(srcDir+"/"+server,dstDir)
        copytree(confDir, dstDir)
        updateConf(server)
        os.chmod(dstDir+"/"+server+"/util/start.sh",stat.S_IXGRP)
        doCmd(dstDir+"/"+server+"/util/start.sh".format(server))
    return

def updateConf(server):
    mysqlHost = getCommProperties("mysql.host")
    localIp = getLocalIp()
    doCmd("sed -i 's/localip.tars.com/{}/g' `find /usr/local/app/tars -name *.conf`".format(localIp))
    doCmd("sed -i 's/192.168.2.131/{}/g' `find /usr/local/app/tars -name *.conf`".format(localIp))
    doCmd("sed -i 's/db.tars.com/{}/g' `find /usr/local/app/tars -name *.conf`".format(mysqlHost))
    doCmd("sed -i 's/registry.tars.com/{}/g' `find /usr/local/app/tars -name *.conf`".format(localIp))
    doCmd("sed -i 's/registry.tars.com/{}/g' `find /usr/local/app/tars -name '*.sh'`".format(localIp))
    doCmd("sed -i 's/web.tars.com/{}/g' `find /usr/local/app/tars -name *.conf`".format(localIp))
    doCmd("sed -i 's/10.120.129.226/{}/g' `find /usr/local/app/tars -name *.conf`".format(localIp))
    return

def copyFile4FrameServer():
    return

def replaceConfig4FrameServer():
    return

def startServerFrameServer():
    return

def deployWeb():
    mysqlHost = getCommProperties("mysql.host")
    localIp = getLocalIp()
    doCmd("sed -i 's/registry.tars.com/{}/g' /usr/local/app/resin/webapps/ROOT/WEB-INF/classes/tars.conf".format(localIp))
    doCmd("sed -i 's/registry.tars.com/{}/g' /usr/local/app/resin/webapps/ROOT/WEB-INF/classes/app.config.properties".format(localIp))
    doCmd("sed -i 's/db.tars.com/{}/g' /usr/local/app/resin/webapps/ROOT/WEB-INF/classes/tars.conf".format(mysqlHost))
    doCmd("sed -i 's/db.tars.com/{}/g' /usr/local/app/resin/webapps/ROOT/WEB-INF/classes/app.config.properties".format(mysqlHost))
    doCmd("chmod u+x /usr/local/app/resin/bin/resin.sh")
    doCmd("/usr/local/app/resin/bin/resin.sh start")
    return

def initDB():
    dbDir=getDBDir()
    mysqlHost = getCommProperties("mysql.host")
    mysqlPort = getCommProperties("mysql.port")
    mysqlRootPassWord = getCommProperties("mysql.root.password")
    localIp = getLocalIp()
    log.info(" dbDir is{} , mysqlHost is {} , mysqlPort is {} mysqlRootPassWord is {} ,localIp is {} ".format(dbDir,mysqlHost,mysqlPort,mysqlRootPassWord,localIp))
    doCmd("mysql -uroot -p{}  -e \"grant all on *.* to 'tars'@'%' identified by 'tars2015' with grant option;flush privileges;\"".format(mysqlRootPassWord))
    log.info(" the mysqlHost is {} , mysqlPort is {},  mysqlRootPassWord is {}".format(mysqlHost,mysqlPort,mysqlRootPassWord))
    doCmd("sed -i 's/192.168.2.131/{}/g' {}/db_tars.sql".format(localIp,dbDir))
    doCmd("sed -i 's/db.tars.com/{}/g' {}/db_tars.sql".format(localIp,dbDir))
    doCmd("sed -i 's/192.168.2.131/{}/g'  {}/*".format(localIp,dbDir))
    doCmd("sed -i 's/db.tars.com/{}/g'  {}/*".format(localIp,dbDir))
    doCmd("sed -i 's/10.120.129.226/{}/g' {}/*".format(localIp,dbDir))

    doCmd("mysql -utars -ptars2015 -e 'create database db_tars'")
    doCmd("mysql -utars -ptars2015 -e 'create database tars_stat'")
    doCmd("mysql -utars -ptars2015 -e 'create database tars_property'")

    doCmd("mysql -utars -ptars2015 db_tars < {}/db_tars.sql".format(dbDir))
    doCmd("mysql -utars -ptars2015 db_tars < {}/tarsconfig.sql".format(dbDir))
    doCmd("mysql -utars -ptars2015 db_tars < {}/tarslog.sql".format(dbDir))
    doCmd("mysql -utars -ptars2015 db_tars < {}/tarspatch.sql".format(dbDir))
    doCmd("mysql -utars -ptars2015 db_tars < {}/tarsproperty.sql".format(dbDir))
    doCmd("mysql -utars -ptars2015 db_tars < {}/tarsqueryproperty.sql".format(dbDir))
    doCmd("mysql -utars -ptars2015 db_tars < {}/tarsquerystat.sql".format(dbDir))
    doCmd("mysql -utars -ptars2015 db_tars < {}/tarsstat.sql".format(dbDir))
    doCmd("mysql -utars -ptars2015 db_tars < {}/tarsnotify.sql".format(dbDir))
    return

if __name__ == '__main__':
    pass