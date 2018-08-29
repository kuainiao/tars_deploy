#!/usr/bin/python
# encoding: utf-8
import sys
import comm.tarsBuild as tarsBuild
import comm.tarsCheck as tarsCheck
import comm.tarsDeploy as tarsDeploy
import comm.tarsTest as tarsTest

def do():
    if len(sys.argv)==1:
        help()
        return
    param =  sys.argv[1]
    if "all" == param:
        print "all"
    elif "check"== param:
        print "check"
    elif "build" == param:
        print "build"
    elif "deploy" ==  param:
        print "deploy"
    elif "test" == param:
        print "test"
    else:
        paramError()
        return
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
    helpMsg = '''
    This script is used to deploy tars frame
    Parameter:
        all : check the environment,build the code ,deploy and test
        check : check the environment
        build : build the code to get binary file
        deploy : deploy the frame ,you must run the command build to get  binary file
        test :  test if all the server are ok
    '''
    print helpMsg
    return

def paramError():
    print "param error!"
    help()
    return


if __name__ == '__main__':
    do()
    pass