import glob
import os
import warnings
import pandas as pd

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.summarization import summarize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pdf2txt as pdf
import csv

def descriptions_extractor(input_file_name, company_name, title_name):
    '''takes an input file, company name and position
    title and returns a list of object with
    the corresponding descriptions.
    '''
    csv.register_dialect('myDialect',
    delimiter = ',',
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True)
    descriptions = []
    with open(input_file_name) as file:
        reader = csv.reader(file, delimiter=',') # DEBUG: THIS PART NEEDS TO BE CHECKED FOR READING MULTIPLE OBJECTS FROM THE CSV
        try:
            for row in reader:
                if row[1] == company_name and row[2] == title_name:
                    # print("$$$$$$$$$$$$$ ROW 1 ROW 2 $$$$$$$$$$$$$$$")
                    # print(row[1],row[2])
                    descriptions.append(row[3])
        except:
            pass
    return(descriptions)


def job_descriptors(descriptions):
    JOB_DESC = 0
    LIST_JOB_FILES = []
    LIST_JOB_DESCP = []

    for desc in descriptions:
        LIST_JOB_DESCP.append(desc)

    # print("in here")
    for desc in LIST_JOB_DESCP:
        # print("inside  here")

        # f = open(path_to_jobs , 'r')
        # text = f.read()
        # str_text = str(text)
        # f.close
        text = desc
        str_text = str(text)
        # str_text = summarize(str_text, word_count=100)
        # print("this\n",str_text)
        text = [str_text]
        # print(text)
        vectorizer = TfidfVectorizer(stop_words = 'english')
        # print(vectorizer)
        vectorizer.fit(text)

        vector = vectorizer.transform(text)
        # print(vector)
        JOB_DESC = vector.toarray()
    return JOB_DESC, vectorizer, LIST_JOB_DESCP



class ResultElement:
    def __init__(self, rank, filename):
        self.rank = rank
        self.filename = filename

def getfilepath(loc):
    temp = str(loc).split('/')
    return temp[-1]

def parser_matcher():
    Resume_Vector = []
    Ordered_list_Resume = []
    Ordered_list_Resume_Score = []
    LIST_OF_PDF_FILES = []

    for file in glob.glob("./Original_Resumes/*.pdf"):
        LIST_OF_PDF_FILES.append(file)

    files = glob.glob('./Parsed_Resumes/*')
    for f in files:
    	os.remove(f)

    print("Total Files to Parse\t" , len(LIST_OF_PDF_FILES))
    print("########## PARSING ###########")
    for i in LIST_OF_PDF_FILES:
        try:
            pdf.extract_text([str(i)] , all_texts=None , output_type='text' , outfile='./Parsed_Resumes/'+getfilepath(i)+'.txt')
        except TypeError:
            print("Error: "+i)
            os.remove('./Parsed_Resumes/'+getfilepath(i)+'.txt')

    print("Done Parsing.")
    print("\n\n")


    PATH_TO_FILE = "data/data.csv"
    COMPANY_NAME = "JG"
    TITLE_NAME = "Front End Software Engineer"
    descriptions = descriptions_extractor(PATH_TO_FILE, COMPANY_NAME, TITLE_NAME)
    Job_Desc,vectorizer, LIST_JOB_DESCP = job_descriptors(descriptions)

    print("########## PARSING FOR: ###########\n COMPANY NAME: \n JOB TITLE: ",COMPANY_NAME, TITLE_NAME)

    LIST_OF_TXT_FILES = []
    for file in glob.glob("./Parsed_Resumes/*.txt"):
        LIST_OF_TXT_FILES.append(file)

    for i in LIST_OF_TXT_FILES:
        Ordered_list_Resume.append(i)
        f = open(i , 'r')
        text = f.read()

        read_text = str(text)
        try:
            read_text = summarize(read_text, word_count=200)
        except ValueError:
            print("Error in sumarizer,Length of text "+str(len(read_text)))
            continue

        text = [read_text]
        f.close()
        vector = vectorizer.transform(text)

        aaa = vector.toarray()
        Resume_Vector.append(vector.toarray())

    for i in Resume_Vector:
        samples = i

        neigh = NearestNeighbors(n_neighbors=1)
        neigh.fit(samples)
        NearestNeighbors(algorithm='auto', leaf_size=40)
        Ordered_list_Resume_Score.extend(neigh.kneighbors(Job_Desc)[0][0].tolist())

    Z = [x for _,x in sorted(zip(Ordered_list_Resume_Score,Ordered_list_Resume))]
    # print(Ordered_list_Resume)
    # print(Ordered_list_Resume_Score)
    flask_return = []
    for n,i in enumerate(Z):
        name = getfilepath(i)
        name = name.split('.')[0]
        rank = n+1
        res = ResultElement(rank, name)
        flask_return.append(res.filename)
        print(f"Rank{res.rank} :\t {res.filename}")
    return flask_return, LIST_JOB_DESCP

if __name__ == '__main__':
    parser_matcher()
