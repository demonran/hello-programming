#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 将繁体转换为简体
import codecs
import logging
import os
import sys

from opencc import OpenCC

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])  # 得到文件名
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    in_file = "./data/wiki.zh.txt"
    out_file = "./data/wiki.zh.simp.txt"
    converter = OpenCC("t2s")

    out = codecs.open(out_file, 'w', encoding='utf8')
    with codecs.open(in_file, 'r', encoding='utf8') as contents:
        i = 0
        for line in contents:
            convert_line = converter.convert(line)
            out.write(convert_line)
            i = i + 1
            if i % 10000 == 0:
                out.flush()
                logger.info("处理了" + str(i) + "行数据")
    out.close()
