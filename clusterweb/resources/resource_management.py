#!/bin/env/python
#-*- encoding: utf-8 -*-
"""

"""
from __future__ import print_function, division
import psutil
import sys
import os

class System(object):

    def __init__(self):
        self.os_type = sys.platform


def main():
    s = System()
    print(s.os_type)

if __name__ == "__main__":
    main()