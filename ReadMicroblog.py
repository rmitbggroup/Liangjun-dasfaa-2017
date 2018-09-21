import microblog as mc
import tweetdoc as td
import pickle
import os.path
import amendsumy
import time

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as lsa
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


Fileadrr="/home/lancelot/Code/Microblogs/MRST/tt.txt"
M = [[]]
def picklefile(name):
    if os.path.isfile(name):
        file = open(name)
        M = pickle.load(name)


def ReadMicrblogFromFile(addr):
    # if os.path.isfile(addr):
    #     file = open(addr)
    #     M = pickle.load(file)
    #     return
    f = open(Fileadrr)
    d = f.readlines()

    ct = 0
    sum = 0
    wd = []
    signal = -1
    t = ""
    re = ""
    con = ""
    mt = []
    for i in d:
        if signal>=0:
            if signal ==0:
                t = i
            if signal == 1:
                re = i
            if signal == 2:
                con = i
            if signal == 3:
                m = mc.microblog(con,t)
                mt.append(m)
            signal=(signal + 1)%4


        if str(i[0:-1]).isdigit():
            if len(mt)!=0:
                M.append(mt)
            mt = []
            ct = ct + 1
            k = (int(i[0:-1]))
            if k > 10000000:
                continue
            wd.append(k)
            sum = sum + k
            signal = 0

    pfile = open(addr,"wb")
    pickle.dump(M,pfile)
ReadMicrblogFromFile("MTs.pickle")
mts = []
for mt in M:
    doc = td.tweetdoc()
    for m in mt:
        sent = unicode(m.content, errors='ignore')
        if(len(sent)>2):
            doc.append(sent)
    #print doc.sentences

    mts.append(doc)


print len(mts)
LANGUAGE = "english"
SENTENCES_COUNT = 10
stemmer = Stemmer(LANGUAGE)

# lex = amendsumy.LexRankSummarizer(stemmer)
# lex.stop_words = get_stop_words(LANGUAGE)
#
lsasum = lsa(stemmer)
lsasum.stop_words = get_stop_words(LANGUAGE)

import Baselines as bs

def testsummary(input):
    documents={}
    cc=0
    for s in input.sentences:
        documents[cc] = s
        cc=cc+1
    for s in lsasum(input,len(input.sentences)):
        file.write(s.content)

    return

file = open("lsa_res.txt","wb")


millis = int(round(time.time() * 1000))

num_of_res=0

for m in range(1,len(mts)):
    print m
    file.write(str(m)+' '+str(len(mts[m].sentences))+'\n')
    testsummary(mts[m])
    milliss = int(round(time.time() * 1000))
    num_of_res= num_of_res+len(mts[m].sentences)

    file.write( str(num_of_res)+"," +str(milliss - millis)+'\n')

milliss = int(round(time.time() * 1000))
print milliss - millis