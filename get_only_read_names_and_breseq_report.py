#!/usr/bin/python3

import glob


month_d = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

for fpath in glob.iglob('./**/log.txt', recursive=True):
    out_str = ""

    f = open(fpath, "r")

    date_s = f.readline()
    date_s = ' '.join(date_s.split())
    date_l = date_s.split(' ')
    date_s = str(month_d[date_l[1]]) + '/' + date_l[2] + '/' + date_l[4]
    out_str += date_s + ','

    for x in fpath.split('/')[-3].split('-'):
        out_str += x + ','

    out_str += '"'
    i = 0
    for line in f.readlines():
        for s in line.split(' '):
            if "fastq" in s or "fq" in s:
                if "qtrim-" in s:
                    s = s.replace("qtrim-", '')
                if "good.fq" in s:
                    s = s.replace("good.fq", "fastq.gz")
                if "fastq.gz" not in s:
                    s = s.replace("fastq", "fastq.gz")
                if i != 0:
                    out_str += ','
                s = s[s.rfind('/')+1:]  # removing the filesystem tree per read file
                out_str += s
                i += 1
    out_str += '"'
    out_str = out_str.replace('\n', '')
    f.close()
    print(out_str)
