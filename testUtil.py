#!/usr/bin/python
# encoding: utf-8
import os
def getAbabsolutePath():
    path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    return path

if __name__ == '__main__':
    print(getAbabsolutePath())
    pass

