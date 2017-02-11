############################################################
# CIS 521: Homework 8
############################################################

student_name = "github/talllankydude"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import numpy
import nltk
from collections import defaultdict
import operator



############################################################
# Section 1: Hidden Markov Models
############################################################

def load_corpus(path):
    f=open(path)
    doc=[]
    for line in f:
        x=line.split()
        token=[]
        for y in x:
            pos=y.split('=')
            token.append(tuple((pos[0],pos[1])))
        #print token
        doc.append(token)
    return doc


class Tagger(object):
    tags = []
    wordtags=[]
    piprob = []
    transprob=[]
    emisprob = []

    def __init__(self, sentences):
        for i in sentences:
            for w in range(len(i)-1) :
                if i[w][1] in self.tags:
                    if w == 0:
                        self.piprob[(self.tags.index(i[w][1]))] += 1;
                    else:
                        #print (self.tags.index(i[w - 1][1])),(self.tags.index(i[w][1]))
                        self.transprob[(self.tags.index(i[w - 1][1]))][(self.tags.index(i[w][1]))] += 1
                else:
                    self.piprob.append(1)
                    self.wordtags.append([])
                    self.transprob.append([])
                    for tag in self.tags:
                        self.transprob[-1].append(0)
                    self.emisprob.append([])
                    for lines in self.transprob:
                        lines.append(0)
                    self.tags.append(i[w][1])

                if i[w][0] in self.wordtags[(self.tags.index(i[w][1]))]:
                    self.emisprob[(self.tags.index(i[w][1]))][self.wordtags[(self.tags.index(i[w][1]))].index(i[w][0])]+=1
                else:
                    self.wordtags[(self.tags.index(i[w][1]))].append(i[w][0])
                    self.emisprob[(self.tags.index(i[w][1]))].append(1)
        self.piprob =[float(x)/sum(self.piprob[:]) for x in self.piprob]
        for row in range(len(self.transprob)):
            values=self.transprob[row]
            tag=[float(x)/sum(values[:]) for x in values]
            self.transprob[row]=tag
        for row in range(len(self.emisprob)):
            values = self.emisprob[row]
            tag = [float(x) / sum(values[:]) for x in values]
            self.emisprob[row]=tag
        print self.tags

    def most_probable_tags(self, tokens):
        tags=[]
        for i in tokens:
            tag=''
            prob=-1
            for t in range(len(self.tags)):
                if i in self.wordtags[t]:
                    if self.emisprob[t][self.wordtags[t].index(i)] > prob:
                        prob= self.emisprob[t][self.wordtags[t].index(i)]
                        tag=self.tags[t]
            tags.append(tag)
        return tags

    def viterbi_tags(self, tokens):

        trellis=[]
        bparray=[]
        path=[-1 for x in tokens]
        for t in self.tags:
            trellis.append([])
            bparray.append([])
            for states in tokens:
                trellis[-1].append(0)
                bparray[-1].append(0)

        for i in range(len(tokens)):
            tags=self.get_tags(tokens[i])
            for t in self.tags:
                #if tokens in self.wordtags[t][:]:
                    if i==0 and t in tags:
                        trellis[t][0]=self.piprob[t]*self.emisprob[t][self.wordtags[t].index(tokens[i])]
                    else:
                        temp=[self.transprob[x][t]*trellis[i-1][t] for x in range(len(self.tags))]
                        trellis[t][i]=max(temp)*self.emisprob[t][i]
                        bparray[t][i - 1]= temp.index(max(temp))
        path[-1] = trellis[:][-1].index(max(trellis[:][-1]))
        i=len(tokens)-2

        while i >-1:
            path[i]= bparray[i+1][path[i+1]]
            i-=1
        return [self.tags[t] for t in path]

    def get_tags(self,tokens):
        return [tag for tag in range(len(self.tags)) if tokens in self.wordtags[tag]]

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


# c = load_corpus("brown_corpus.txt")
# print c[1402]
# print c[1799]

c = load_corpus("brown_corpus.txt")
t = Tagger(c)
print t.most_probable_tags(["The", "man", "walks", "."])
print t.most_probable_tags(["The", "blue", "bird", "sings"])


s = "I am waiting to reply".split()
t.most_probable_tags(s)
for x in s:
    print t.get_tags(x)
#['PRON', 'VERB', 'VERB', 'PRT', 'NOUN']
t.viterbi_tags(s)
#['PRON', 'VERB', 'VERB', 'PRT', 'VERB']
print 'done'

s = "I saw the play".split()
t.most_probable_tags(s)
for x in s:
    print t.get_tags(x)
#['PRON', 'VERB', 'DET', 'VERB']
t.viterbi_tags(s)
#['PRON', 'VERB', 'DET', 'NOUN']