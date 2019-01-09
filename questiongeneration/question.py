import sys
import argparse
from questiongeneration.question_generator import QuestionGenerator


def add_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '-sentence', type=str, help="The sentence for which questions are to be generated.")
    parser.add_argument('-t', '-question_type', type=str, default=['Wh', 'Are', 'Who', 'Do'], choices=['Wh', 'Are', 'Who', 'Do', 'All'], help='The types of questions to be generated.')
    return parser.parse_args()

def genQ(filename, description):
    # x = filenam
    data = ""
    data += str(description[0])
    with open(filename, 'r') as file:
        data+=file.read().replace('\n\r', ' ')
    # print("$$$$$$$$$$$$$$$$$ DATA $$$$$$$$$$$$$$$$$$$$")
    # print(data)
    q  = QuestionGenerator()
    question_list = q.generate_question(data)
    # print(question_list)
    return question_list

# if __name__ == '__main__':
    # args = add_arguments()
    # print(args.s)
    # x = str(input())
    # print(x)
    # if not x:
    #     sys.stdout.write('No input given\n')
    #     sys.exit()
    # q  = QuestionGenerator()

    # question_list = q.generate_question(x) #, args.t)
    # print(question_list)
