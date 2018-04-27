#!/usr/bin/env python3
# coding: utf-8
# File: sim_tokenvector.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-27
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import numpy as np

class SimTokenVec:

    def __init__(self):
        self.embedding_path = 'model/token_vector.bin'
        self.model = gensim.models.KeyedVectors.load_word2vec_format(self.embedding_path, binary=False)

    '''获取词向量文件'''
    def get_wordvector(self, word):#获取词向量
        try:
            return self.model[word]
        except:
            return np.zeros(200)

    '''基于余弦相似度计算句子之间的相似度，句子向量等于字符向量求平均'''
    def similarity_cosine(self, word_list1,word_list2):#给予余弦相似度的相似度计算
        vector1 = np.zeros(200)
        for word in word_list1:
            vector1 += self.get_wordvector(word)
        vector1=vector1/len(word_list1)
        vector2=np.zeros(200)
        for word in word_list2:
            vector2 += self.get_wordvector(word)
        vector2=vector2/len(word_list2)
        cos1 = np.sum(vector1*vector2)
        cos21 = np.sqrt(sum(vector1**2))
        cos22 = np.sqrt(sum(vector2**2))
        similarity = cos1/float(cos21*cos22)
        return  similarity

    '''计算句子相似度'''
    def distance(self, text1, text2):#相似性计算主函数
        word_list1=[word for word in text1]
        word_list2=[word for word in text2]
        return self.similarity_cosine(word_list1,word_list2)

def test():
    text1 = '我喜欢你'
    text2 = '我讨厌你'
    simer = SimTokenVec()
    sim = simer.distance(text1, text2)
    print(sim)
test()