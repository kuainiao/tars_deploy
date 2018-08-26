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
    #build()
    #deploy()
    #test()
    return

def check():
    return

def build():
    return tarsBuild.do()

def deploy():
    return tarsDeploy.do()

def test():
    return tarsTest.do()

if __name__ == '__main__':
    do()
    pass