#! /usr/bin/env python
# -*- coding:gbk -*-

"""
Notes:
    A python script that use regex to replace all the label of a html file
"""

import os
import sys
import re

if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, 'r') as fp:
        for line in fp:
            line = line.rstrip()
            pattern = re.compile(r'<([^>]*)>')
            match_list = pattern.findall(line)
            for i in range(0, len(match_list)):
                print "matched:%s" %match_list[i]
            line = pattern.sub('', line)
            print line
