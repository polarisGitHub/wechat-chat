# -*- coding: utf-8 -*-
# 提取聊天记录

import sys
import csv
import codecs
import jieba
import re

csv.field_size_limit(sys.maxsize)

jieba.load_userdict("dict/dict.dat")
p = re.compile('@\S*')


def stopwords(filepath):
    return [line.strip() for line in codecs.open(filepath, 'r', encoding='utf-8').readlines()]


stop = stopwords("dict/stop.dat")
process_file_name = '20220615'


def get_chat_message(message):
    if ':\n' not in message:
        return ''
    if "<?xml" not in message and "<msg>" not in message and '<sysmsg' not in message and '</msg>' not in message:
        return "".join(message.split(":")[1:]).replace("\n", "")
    return ''


with codecs.open("data/{}_chat.txt".format(process_file_name), 'w', encoding='utf-8') as w:
    with codecs.open("data/{}.csv".format(process_file_name), 'r', encoding='utf-8') as f:
        csv_file = csv.reader(f)
        for row in csv_file:
            if len(row) == 2:
                message = row[1]
                chat_message = get_chat_message(message)
                if chat_message:
                    cut = jieba.lcut(re.sub(p, "", chat_message))
                    stop_cut = []
                    for word in cut:
                        if word.strip() != '' and word not in stop:
                            stop_cut.append(word)
                    write_text = " ".join(stop_cut)
                    if write_text:
                        w.write(" ".join(stop_cut))
                        w.write("\r")
