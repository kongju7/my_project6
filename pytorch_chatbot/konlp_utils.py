import numpy as np

# 한국어 형태소 
from konlpy.tag import Okt
okt = Okt()

# 한글 표제어 추출: 한글 용언 분석기(Korean Lemmatizer) 사용 
# url: https://github.com/lovit/korean_lemmatizer
from soylemma import Lemmatizer
lemmatizer = Lemmatizer()

def tokenize(sentence):
    stopwords = ['도', '는', '다', '의', '가', '이', '은', '한', '에', '하', '고', '을', '를', '인', '듯', '과', '와', '네', '들', '듯', '지', '임', '게']
    tokenized = okt.morphs(sentence)
    tokenized = [item for item in tokenized if item not in stopwords]
    return tokenized

def stem(word):
    if lemmatizer.lemmatize(word):
        return lemmatizer.lemmatize(word)[0][0]
    return word

def bag_of_words(tokenized_sentence, words):
    # 각 단어 표제어 추출 
    sentence_words = [stem(word) for word in tokenized_sentence]
    # bag 초기화 
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
    return bag