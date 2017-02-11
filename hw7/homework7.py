############################################################
# CIS 521: Homework 7
############################################################

student_name = "github\talllankydude"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import numpy
import math
import random
from nltk.tokenize import TweetTokenizer
#from nltk.util import ngrams



############################################################
# Section 1: Markov Models
############################################################

def mytokenize(text):
    tknzr = TweetTokenizer()
    return tknzr.tokenize(text)


def ngrams(n, tokens):
    newtokens=[]
    ng=[]
    for i in range(n-1):
        newtokens.append('<START>')
    for i in tokens:
        newtokens.append(i)
    newtokens.append('<END>')
    for i in range(len(tokens)+1):
        toke=[]
        for j in range(n-1):
            toke.append(newtokens[i+j])
        ng.append((tuple(toke),newtokens[n-1+i]))
    return ng



class NgramModel(object):
    n=0
    allngrams=[]

    def __init__(self, n):
        self.n=n

    def update(self, sentence):
        for i in ngrams(self.n,mytokenize(sentence)):
            self.allngrams.append(i)

    def prob(self, context, token):
        print  context,token
        nr=0
        dr=0
        for i in self.allngrams:
            if (context,token) == i:
                nr+=1
            if context in i:
                dr+=1
        if dr:
            return float(nr)/dr
        else:
            return 0

    def random_token(self, context):
        sub=[]
        for i in self.allngrams:
            if context in i:
                sub.append(i[1])
        return random.choice(sub)

    def random_text(self, token_count):
        context=[]
        for i in range(self.n-1):
            context.append('<START>')
        tokens=[]
        for i in range(token_count):
            toke=self.random_token(tuple(context))
            tokens.append(toke)
            if self.n > 1:
                if toke !='<END>':
                    context.append(toke)
                    context=context[1:]
                else:
                    context = []
                    for x in range(self.n - 1):
                        context.append('<START>')
        sentence=' '.join(word for word in tokens)
        return sentence

    def perplexity(self, sentence):
        ng=ngrams(self.n,mytokenize(sentence))
        perp=0
        for i in range(len(ng)):
            perp+=-\
                math.log10(self.prob(ng[i][0],ng[i][1]))
        return math.pow(math.pow(10,perp),(float(1)/len(ng)))


def create_ngram_model(n, path):
    f= open(path,'r')
    doc=NgramModel(n)
    for line in f:
        doc.update(line)
    return doc

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
################################################################

# print mytokenize("  This is an example.  ")
# print mytokenize("a b c d")
# print mytokenize("'Medium-rare,' she said.")
# print ngrams(1, ["a", "b", "c"])
# print ngrams(3, ["a", "b", "c"])
# print ngrams(2, ["a", "b", "c"])

m = NgramModel(1)
m.update("a b c d")
m.update("a b a b")
# # # print m.prob((), "a")
# # # print m.prob((), "c")
# # # print m.prob((), "<END>")
# random.seed(1)
# # print [m.random_token(())
# #      for i in range(25)]
# print m.random_text(13)
print m.perplexity("a b")

m = NgramModel(2)
m.update("a b c d")
m.update("a b a b")
# # # print m.prob(("<START>",), "a")
# # # print m.prob(("b",), "c")
# # # print m.prob(("a",), "x")
# random.seed(2)
# # print [m.random_token(("<START>",)) for i in range(6)]
# # print [m.random_token(("b",)) for i in range(6)]
# print m.random_text(15)
print m.perplexity("a b")

# m = create_ngram_model(3, "frankenstein.txt");
# print m.random_text(45)