# -*- coding: utf-8 -*-
# 提取聊天记录

import csv
import codecs
import jieba
import re

jieba.load_userdict("dict/dict.dat")
jieba.enable_parallel(8)
p = re.compile('@\S*')


def stopwords(filepath):
    return [line.strip() for line in codecs.open(filepath, 'r', encoding='utf-8').readlines()]


stop = stopwords("dict/stop.dat")
process_file_name = '2019'

with codecs.open("data/{}_chat.txt".format(process_file_name), 'w', encoding='utf-8') as w:
    with codecs.open("data/{}.csv".format(process_file_name), 'r', encoding='utf-8') as f:
        csv_file = csv.reader(f)
        for row in csv_file:
            if len(row) == 2:
                if ":" not in row[1]:
                    chat = row[1]
                else:
                    chat = "".join(row[1].split(":")[1:]).replace("\n", "")
                if "<?xml" not in chat and "<msg>" not in chat and '<sysmsg' not in chat and '</msg>' not in chat:
                    cut = jieba.lcut(re.sub(p, "", chat))
                    stop_cut = []
                    for word in cut:
                        if word.strip() != '' and word not in stop:
                            stop_cut.append(word)
                    w.write(" ".join(stop_cut))
                    w.write("\r")
