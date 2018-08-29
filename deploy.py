#!/usr/bin/python
# encoding: utf-8
import sys
import comm.tarsBuild as tarsBuild
import comm.tarsCheck as tarsCheck
import comm.tarsDeploy as tarsDeploy
import comm.tarsTest as tarsTest

def do():
    #check()
    #build()
    deploy()
    test()
    return

def check():
    tarsCheck.do()

def build():
    tarsBuild.do()

def deploy():
    tarsDeploy.do()

def test():
    tarsTest.do()

if __name__ == '__main__':
    param =  sys.argv[1]
    print param
    #do()
    pass