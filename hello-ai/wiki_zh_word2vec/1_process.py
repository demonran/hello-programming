#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 将xml的wiki数据转换为text格式
import codecs
import logging
import os
import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])  # 得到文件名
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    in_file = "./data/zhwiki-latest-pages-articles.xml.bz2"
    out_file = "./data/wiki.zh.txt"
    space = " "

    out = codecs.open(out_file, 'w')
    wiki = WikiCorpus(in_file, dictionary={})
    i = 0
    for text in wiki.get_texts():
        out.write(space.join(text) + '\n')
        i = i + 1
        if i % 10000 == 0:
            out.flush()
            logger.info("Saved " + str(i) + " articles")
    out.close()
    logger.info("Saved " + str(i) + " articles")
