############################################################
# CIS 521: Homework 8
############################################################

student_name = "Type your full name here."

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import nltk


############################################################
# Section 1: Hidden Markov Models
############################################################

def load_corpus(path):
    #"D:/SCMP/CIS521/Assignment8/brown_corpus.txt"
    fp = open(path)
    C = []
    for i, line in enumerate(fp):
        A = line.split()
        x = []
        for j in A:
            x.append(tuple(j.split("=")))
        C.append(x)
    fp.close()
    return C

class Tagger(object):

    def __init__(self, sentences):
        pass

    def most_probable_tags(self, tokens):
        pass

    def viterbi_tags(self, tokens):
        pass

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
