#!/usr/bin/python
# encoding: utf-8
import tarsLog
from tarsUtil import *

log = tarsLog.getLogger()
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
    baseDir = getBaseDir()
    dbDir = baseDir+"/cpp/framework/sql/"
    return dbDir

def deployFrameServer():
    mysqlHost = getCommProperties("mysql.host")
    localIp = getLocalIp()
    doCmd("mkdir -p /usr/local/app/tars")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tars* /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tarsregistry /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tarsAdminRegistry /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tarsnode /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tarsconfig /usr/local/app/tars/")
    doCmd("cp -rf  /data/Tars/cpp/build/framework/deploy/tarsnotify /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tarspatch /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tarsstat /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tarsproperty /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tarsquerystat /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tarsqueryproperty /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/build/framework/deploy/tarslog /usr/local/app/tars/")
    doCmd("cp -rf /data/Tars/cpp/framework/deploy/tars* /usr/local/app/tars/")
    doCmd("mkdir -p /usr/local/app/tars/tarsauth/bin;mv /usr/local/app/tars/tarsauth/tarsauth /usr/local/app/tars/tarsauth/bin/")
    doCmd("mkdir -p /usr/local/app/tars/tarslog/bin;mv /usr/local/app/tars/tarslog/tarslog /usr/local/app/tars/tarslog/bin/")
    doCmd("mkdir -p /usr/local/app/tars/tarsnotify/bin;mv /usr/local/app/tars/tarsnotify/tarsnotify /usr/local/app/tars/tarsnotify/bin/")
    doCmd("mkdir -p /usr/local/app/tars/tarsproperty/bin;mv /usr/local/app/tars/tarsproperty/tarsproperty /usr/local/app/tars/tarsproperty/bin/")
    doCmd("mkdir -p /usr/local/app/tars/tarsqueryproperty/bin;mv /usr/local/app/tars/tarsqueryproperty/tarsqueryproperty /usr/local/app/tars/tarsqueryproperty/bin/")
    doCmd("mkdir -p /usr/local/app/tars/tarsquerystat/bin;mv /usr/local/app/tars/tarsquerystat/tarsquerystat  /usr/local/app/tars/tarsquerystat/bin")
    doCmd("mkdir -p /usr/local/app/tars/tarsstat/bin;mv /usr/local/app/tars/tarsstat/tarsstat /usr/local/app/tars/tarsstat/bin/")

    doCmd("sed -i 's/localip.tars.com/{}/g' `find /usr/local/app/tars -name *.conf`".format(localIp))
    doCmd("sed -i 's/192.168.2.131/{}/g' `find /usr/local/app/tars -name *.conf`".format(localIp))
    doCmd("sed -i 's/db.tars.com/{}/g' `find /usr/local/app/tars -name *.conf`".format(mysqlHost))
    doCmd("sed -i 's/registry.tars.com/{}/g' `find /usr/local/app/tars -name *.conf`".format(localIp))
    doCmd("sed -i 's/registry.tars.com/{}/g' `find /usr/local/app/tars -name '*.sh'`".format(localIp))
    doCmd("sed -i 's/web.tars.com/{}/g' `find /usr/local/app/tars -name *.conf`".format(localIp))
    doCmd("sed -i 's/10.120.129.226/{}/g' `find /usr/local/app/tars -name *.conf`".format(localIp))

    doCmd("find /usr/local/app/tars/  -name '*.sh'| xargs chmod u+x")
    doCmd("/usr/local/app/tars/tarsregistry/util/start.sh")
    doCmd("/usr/local/app/tars/tarsnode/util/start.sh")
    doCmd("/usr/local/app/tars/tarsAdminRegistry/util/start.sh")
    doCmd("/usr/local/app/tars/tarsconfig/util/start.sh")
    doCmd("/usr/local/app/tars/tarsnotify/util/start.sh")
    doCmd("/usr/local/app/tars/tarspatch/util/start.sh")
    doCmd("/usr/local/app/tars/tarsstat/util/start.sh")
    doCmd("/usr/local/app/tars/tarsproperty/util/start.sh")
    doCmd("/usr/local/app/tars/tarsquerystat/util/start.sh")
    doCmd("/usr/local/app/tars/tarsqueryproperty/util/start.sh")
    doCmd("/usr/local/app/tars/tarslog/util/start.sh")
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