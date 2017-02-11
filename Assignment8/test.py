fp = open("D:/SCMP/CIS521/Assignment8/brown_corpus.txt")
C=[]
for i, line in enumerate(fp):
    A=line.split()
    x=[]
    for j in A:
        x.append(tuple(j.split("=")))
    C.append(x)
fp.close()