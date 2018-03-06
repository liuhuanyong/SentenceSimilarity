#coding=utf-8
import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba

semantic_dict={}
for line in open("glossary.dat"):
    word_list=[word for word in line.strip().decode('utf-8').replace(' ','>').replace('\t','>').split('>') if word !='']
    word=word_list[0]
    word_def=word_list[2]
    if word not in semantic_dict:
        semantic_dict[word]=word_def
    else:
        semantic_dict[word]='='+word_def

def calculate_semantic(DEF1,DEF2):
    DEF_INTERSECTION=set(DEF1).intersection(set(DEF2))
    DEF_UNION=set(DEF1).union(set(DEF2))   
    score=float(len(DEF_INTERSECTION))/float(len(DEF_UNION))
    return score

def compute_similarity(word1,word2):
    DEFS_word1=[]
    if word1 in semantic_dict:
        for semantic in semantic_dict[word1].split('='):
            DEFS_word1.append(semantic.split(','))

    DEFS_word2=[]
    if word2 in semantic_dict:
        for semantic in semantic_dict[word2].split('='):
            DEFS_word2.append(semantic.split(','))

    score_list=[]

    for DEF_word1 in DEFS_word1:
        for DEF_word2 in DEFS_word2:
            score=calculate_semantic(DEF_word1,DEF_word2)
            score_list.append(score)
    
    try:
        return sorted(score_list)[-1]
    except:
        return 0.0

def compute_similarity_semantic(text1,text2):
    word_list1=[word for word in jieba.cut(text1)]
    word_list2=[word for word in jieba.cut(text2)]
    score_wordlist1=0
    score_wordlist2=0
    for word1 in word_list1:
        score_list=[]
        for word2 in word_list2:
            score=compute_similarity(word1,word2)
            score_list.append(score)
        score_wordlist1+=score_list[-1]

    for word2 in word_list2:
        score_list=[]
        for word1 in word_list1:
            score=compute_similarity(word1,word2)
            score_list.append(score)

        score_wordlist2+=score_list[-1]
        
    similarity=(score_wordlist1+score_wordlist2)/float((len(word_list1)+len(word_list2)))
    
    return similarity 

def main():
    text1=raw_input("please enter text1:")
    text2=raw_input("please enter text2:")
    while(1):
        try:
            similarity=compute_similarity_semantic(text1,text2)
        except:
            similarity=0.0
            
        print "similarity_jaccard",similarity

        text1=raw_input("please enter word1:")
        text2=raw_input("please enter word2:")

if __name__=="__main__":
    main()