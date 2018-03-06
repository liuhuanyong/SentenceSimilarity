#coding=utf-8
import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from simhash import Simhash,SimhashIndex
import jieba.posseg as pseg

def haming_distance(code_s1,code_s2):#利用海明距离,计算全文编码距离
    x = (code_s1 ^ code_s2) & ((1 << 64) - 1)
    ans = 0
    while x:
        ans += 1
        x &= x - 1
    return ans

def get_similarity(a,b):#利用相似度计算方式,计算全文编码相似度
    if a > b : 
        return b / a
    else:
        return a / b

def get_features(string):#对全文进行分词,提取全文特征,使用词性将虚词等无关字符去重
    word_list=[word.word for word in pseg.cut(string) if word.flag[0] not in ['u','x','w','o','p','c','m','q']]
    return word_list


def get_distance(code_s1,code_s2):#计算两个全文编码的距离
    return haming_distance(code_s1,code_s2)


def get_code(string):#对全文进行编码
    return Simhash(get_features(string)).value

def compute_similarity_semantic(s1,s2):
     #对文件进行simhash编码
    code_s1=get_code(s1)
    code_s2=get_code(s2)
    #分别计算s1,s2,s3之间的距离,s1与s2之间的距离为<4时,认为两者之间时重复的,可以依据此规则进行相似度去重.
    similarity=haming_distance(code_s1,code_s2)
    return similarity

def main():
    text1=raw_input("please enter text1:")
    text2=raw_input("please enter text2:")
    while(1):
        try:
            similarity=compute_similarity_semantic(text1,text2)
        except:
            similarity=0.0            
        print "similarity_simhash",similarity

        text1=raw_input("please enter word1:")
        text2=raw_input("please enter word2:")


if __name__=="__main__":
    main()
