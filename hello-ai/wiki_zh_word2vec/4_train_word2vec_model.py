#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 使用gensim word2vec训练脚本获取词向量
import logging
import multiprocessing
import os
import sys
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])  # 得到文件名
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    inp= './data/wiki.zh.simp.seg.txt'
    outp1 = './data/wiki.zh.text.model'
    outp2 = './data/wiki.zh.text.vector'

    model = Word2Vec(LineSentence(inp), vector_size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())

    model.save(outp1)
    # model.wv.save_word2vec_format(outp2, binary=False)
