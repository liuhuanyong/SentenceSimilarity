#coding=utf-8
import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import numpy as np

import jieba.posseg as pesg
model = gensim.models.KeyedVectors.load_word2vec_format("token_vector.bin", binary=False)


def calculate_semantic(word1,word2):
    try:
        word_score=model.similarity(word1,word2)
    except:
        word_score=0

    return word_score

def get_wordvector(word):
    try:
        return model[word]
    except:
        return np.zeros(200)

def similarity_jaccard(word_list1,word_list2):
    score_wordlist1=0
    score_wordlist2=0
    for word1 in word_list1:
        score_list=[]
        for word2 in word_list2:
            score_list.append(calculate_semantic(word1,word2))
        try:    
            score_wordlist1+=sorted(score_list)[-1]
        except:
            pass
    

    for word2 in word_list2:
        score_list=[]
        for word1 in word_list1:
            score_list.append(calculate_semantic(word1,word2))
        try:
            score_wordlist2+=sorted(score_list)[-1]
        except:
            pass
        
    similarity=(score_wordlist1+score_wordlist2)/float((len(word_list1)+len(word_list2)))
        
    return similarity


def similarity_cosine(word_list1,word_list2):
    simalrity=0
    vector1=np.zeros(200)
 
    for word in word_list1:
        vector1+=get_wordvector(word)
    
    vector1=vector1/len(word_list1)

    vector2=np.zeros(200)

    for word in word_list2:
        vector2+=get_wordvector(word)

    vector2=vector2/len(word_list2)

    cos1 = np.sum(vector1*vector2)
    cos21 = np.sqrt(sum(vector1**2))
    cos22 = np.sqrt(sum(vector2**2))
    similarity = cos1/float(cos21*cos22)

    return  similarity


def main():
    text1=raw_input("please enter text1:").decode('utf-8')
    text2=raw_input("please enter text2:").decode('utf-8')


    while(1):
        word_list1=[]
        word_list2=[]
        for word in text1:
            word_list1.append(word)

        for word in text2:
            word_list2.append(word)

        similarity_ja=0
        similarity_cos=0
        similarity_ja=similarity_jaccard(word_list1,word_list2)
        similarity_cos=similarity_cosine(word_list1,word_list2)
        
        print 'similarity_jaccard',similarity_ja
        print 'similairy_cosine',similarity_cos
        text1=raw_input("please enter word1:").decode('utf-8')
        text2=raw_input("please enter word2:").decode('utf-8')


if __name__=="__main__":
    main()
    #get_wordvector()
    #test()