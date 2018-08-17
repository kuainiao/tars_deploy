#!/usr/bin/python
# encoding: utf-8

import tarsLog
import tarsUtil
def do():
    build()
    return

def build():
    baseDir = getBaseDir()
    doCmd("{}/cpp/build/build.sh cleanall".format(baseDir))
    doCmd("{}/cpp/build/build.sh all".format(baseDir))
    return


if __name__ == '__main__':
    pass