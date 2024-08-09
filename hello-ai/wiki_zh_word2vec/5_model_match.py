#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 测试训练好的模型

import gensim

if __name__ == '__main__':
    model = gensim.models.Word2Vec.load('./data/wiki.zh.text.model')
    word = model.wv.most_similar(u'足球', topn=5)
    for t in word:
        print(t[0], t[1])

    word = model.wv.most_similar(positive=[u'皇上', u'国王'], negative=[u'皇后'])
    for t in word:
        print(t[0], t[1])
    print("==========")
    print(model.wv.doesnt_match(u'太后 妃子 贵人 贵妃 才人'.split()))
    print("===========")
    print(model.wv.similarity(u'书籍', u'书本'))
    print(model.wv.similarity(u'逛街', u'书本'))
