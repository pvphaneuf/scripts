#!/usr/bin/python3

import glob


for fpath in glob.iglob('./**/log.txt', recursive=True):
    f = open(fpath, 'r')
    l = f.readline().replace('\n', '')
    print(l)
    f.close()
