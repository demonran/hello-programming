#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 逐行读取文件数据进行jieba分词
import codecs
import logging
import os
import sys

import jieba

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])  # 得到文件名
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    out = codecs.open('./data/wiki.zh.simp.seg.txt', 'w', encoding='utf8')
    with codecs.open('./data/wiki.zh.simp.txt', 'r', encoding='utf8') as contents:
        i = 0
        for line in contents:
            line_seg = ' '.join(jieba.cut(line, cut_all=False))
            out.writelines(line_seg)
            i = i + 1
            if i % 10000 == 0:
                out.flush()
                logger.info("处理了" + str(i) + "行数据")
        logger.info("处理了" + str(i) + "行数据")
    out.close()
