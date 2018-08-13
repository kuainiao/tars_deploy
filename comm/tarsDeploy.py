#!/usr/bin/python
# encoding: utf-8
import tarsLog
from tarsUtil import *

log = tarsLog.getLogger()
def do():

    return

def getDBDir():
    dir = getAbabsolutePath()
    return

def initDB():
    dbDir=getDBDir()
    mysqlHost = getCommProperties("mysql.host")
    mysqlPort = getCommProperties("mysql.port")
    mysqlRootPassWord = getCommProperties("mysql.root.password")
    localIp = getLocalIp()
    doCmd("mysql -uroot -p{}  -e \"grant all on *.* to 'tars'@'%' identified by 'tars2015' with grant option;flush privileges;\"".format(mysqlRootPassWord))
    log.info(" the mysqlHost is {} , mysqlPort is {},  mysqlRootPassWord is {}".format(mysqlHost,mysqlPort,mysqlRootPassWord))
    doCmd("sed -i 's/192.168.2.131/{}/g' {}/db_tars.sql".format(localIp,dbDir))
    doCmd("sed -i 's/db.tars.com/{}/g' {}/db_tars.sql".format(localIp,dbDir))
    doCmd("sed -i 's/192.168.2.131/{}/g' `grep 192.168.2.131 -rl ./*`".format(localIp))
    doCmd("sed -i 's/db.tars.com/{}/g' `grep db.tars.com -rl ./*`".format(localIp))
    doCmd("sed -i 's/10.120.129.226/{}/g' `grep 10.120.129.226 -rl ./*`".format(localIp))

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

    return


if __name__ == '__main__':
    pass