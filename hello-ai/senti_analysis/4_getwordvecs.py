#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 从词向量模型中提取文本特征向量
import codecs
import logging
import os
import sys
import gensim
import numpy as np
import pandas as pd


def getWordVecs(wordList, model):
    vecs = []
    for word in wordList:
        word = word.replace('\n', '')
        # print word
        try:
            vecs.append(model[word])
        except KeyError:
            continue
    return np.array(vecs, dtype='float')


def build_vecs(filename, model):
    fileVecs = []
    with codecs.open(filename, 'rb', encoding='utf-8') as contents:
        for line in contents:
            logger.info("Start line: " + line)
            wordList = line.split(' ')
            vecs = getWordVecs(wordList, model)
            # print vecs
            # sys.exit()
            # for each sentence, the mean vector of all its vectors is used to represent this sentence
            if len(vecs) > 0:
                vecsArray = sum(np.array(vecs)) / len(vecs)  # mean
                # print vecsArray
                # sys.exit()
                fileVecs.append(vecsArray)
    return fileVecs


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # load word2vec model
    fdir = 'tmp/'
    inp = fdir + 'wiki.zh.text.vector'
    model = gensim.models.Word2Vec.load('../wiki_zh_word2vec/data/wiki.zh.text.model')
    posInput = build_vecs(fdir + '2000_pos_cut_stopword.txt', model.wv)
    negInput = build_vecs(fdir + '2000_neg_cut_stopword.txt', model.wv)

    Y = np.concatenate((np.ones(len(posInput)), np.zeros(len(negInput))))
    X = posInput[:]
    for neg in negInput:
        X.append(neg)
    X = np.array(X)

    # write in file
    df_x = pd.DataFrame(X)
    df_y = pd.DataFrame(Y)
    data = pd.concat([df_y, df_x], axis=1)
    # print data
    data.to_csv(fdir + '2000_data.csv')
