#!/usr/bin/python
# encoding: utf-8
import os
def getAbabsolutePath():
    path = os.path.split(os.path.realpath(__file__))[0];
    return path

if __name__ == '__main__':
    print(getAbabsolutePath())
    pass

