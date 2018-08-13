#!/usr/bin/python
# encoding: utf-8
import logging, os
class Logger:
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # 设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)

loggermap = {}
def getLogger(logName="info.log"):
    logPath ="/data/log/tars/"
    isExists=os.path.exists(logPath)
    if not isExists:
        os.makedirs(logPath)
    if logPath+logName in loggermap:
        return loggermap[logPath+logName]
    else:
        logger = Logger(logPath+logName, logging.INFO, logging.INFO)
        loggermap[logPath+logName] = logger
        return logger


if __name__ == '__main__':
    #logyyx = Logger('d://yyx.log', logging.ERROR, logging.DEBUG)
    log = getLogger()
    log.info("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")