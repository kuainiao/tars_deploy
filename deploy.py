#!/usr/bin/python
# encoding: utf-8
import comm.tarsBuild as tarsBuild
import comm.tarsCheck as tarsCheck
import comm.tarsDeploy as tarsDeploy
import comm.tarsTest as tarsTest
import comm.tarsLog as tarsLog
import comm.tarsUtil as tarsUtil

def do():
    check()
    build()
    deploy()
    test()
    return

def check():
    return

def build():
    tarsBuild.do()
    return

def deploy():
    tarsDeploy.do()
    return

def test():
    return

if __name__ == '__main__':
    do()
    pass