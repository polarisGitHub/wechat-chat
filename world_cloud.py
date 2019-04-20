# -*- coding: utf-8 -*-

import codecs
from wordcloud import WordCloud

file_name = '2019_chat'
with codecs.open("data/{}.txt".format(file_name), 'r', encoding='utf-8') as f:
    text = f.read()

wordcloud = WordCloud(background_color="white", width=2000, height=1720, margin=2, max_words=300, font_step=2,
                      font_path="/System/Library/fonts/PingFang.ttc"
                      ).generate(text)

wordcloud.to_file("data/{}.png".format(file_name))
