#!/usr/bin/python3

import glob


out_str = ""
for fpath in glob.iglob('./**/log.txt', recursive=True):
    f = open(fpath, "r")
    for line in f.readlines():
        for s in line.split(' '):
            if "fastq" in s or "good.fq" in s:
                s = s.replace("qtrim-", ' ')
                s = s.replace("good.fq", 'fastq.gz')
                out_str += ' ' + s
    out_str = out_str.replace('\n', '')
    f.close()
print(out_str)
