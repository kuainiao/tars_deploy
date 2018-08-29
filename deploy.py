#!/usr/bin/python
# encoding: utf-8
import sys
import comm.tarsBuild as tarsBuild
import comm.tarsCheck as tarsCheck
import comm.tarsDeploy as tarsDeploy
import comm.tarsTest as tarsTest

def do():
    print len(sys.argv)
    if len(sys.argv)==1:
        help()
        return
    param =  sys.argv[1]
    print param

    #check()
    #build()
    #deploy()
    #test()
    return

def check():
    tarsCheck.do()

def build():
    tarsBuild.do()

def deploy():
    tarsDeploy.do()

def test():
    tarsTest.do()


def help():
    print "help:"
    return

if __name__ == '__main__':
    do()
    pass