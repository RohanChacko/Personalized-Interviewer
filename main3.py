from main import parser_matcher
import glob
import os
import warnings
import pandas as pd

# warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
# from gensim.summarization import summarize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
# import pdf2txt as pdf
# import csv
from questiongeneration.question import genQ

lis, description = parser_matcher()

# print(lis)

TOP_FIVE = "Parsed_Resumes/"

five = []

for i in range(5):
    five.append(TOP_FIVE + lis[i]+'.pdf.txt')

# print(five)


tr = genQ(five[0],description)


Scores = []
if len(tr)  < 5:
    qn  = tr
else:
    qn = tr[:5]
print(qn)
for qset in qn:
    Ordered_list_Resume_Score = []
    ANS_DES = 0
    EXPECTED_DES = 0
    print(qset["Q"])
    input_ans = str(input())
    text = input_ans
    str_text = str(text)
    text = [str_text]
    vectorizer = TfidfVectorizer(stop_words = 'english')
    vectorizer.fit(text)
    vector = vectorizer.transform(text)
    ANS_DES = [vector.toarray()]
    text2 = [qset["A"]]
    vector = vectorizer.transform(text2)
    EXPECTED_DES = vector.toarray()


    for i in ANS_DES:
        neigh = NearestNeighbors(n_neighbors=1)
        neigh.fit(i)
        NearestNeighbors(algorithm='auto', leaf_size=40)
        Ordered_list_Resume_Score.extend(neigh.kneighbors(EXPECTED_DES)[0][0].tolist())

    # print(Ordered_list_Resume_Score)
    Scores.append(Ordered_list_Resume_Score[0])


Filtered_Scores = []
Sum = 0
Number = 0
for score in Scores:
    if(score <= 0.8):
        Filtered_Scores.append(score)
        Sum += score
        Number += 1

Deviation = Sum/Number
Percentage_fit = (1-Deviation) * 100
print("Percentage Fit: ",Percentage_fit)
