import microblog as mc
import tweetdoc as td
import pickle
import os.path
import Queue
import amendsumy
import time

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as lsa
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


Fileadrr="tt.txt"
M = [[0]]
def picklefile(name):
    if os.path.isfile(name):
        file = open(name)
        M = pickle.load(name)

M.remove([0])
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
                usr, rp= re.split()
                m.rep(usr,rp)
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
    if len(mt) != 0:
        M.append(mt)

ReadMicrblogFromFile(" ")
ind = [[0]]
ind.remove([0])
for MT in M:
    dic = {}
    m_in= []
    for m in range(0,len(MT)):
        mc = MT[m]
        dic[mc.usr] = m
        if mc.reply =="NONE" or mc.reply not in dic:
            m_in.append(0)
        else:
            m_in.append(dic[mc.reply])
    ind.append(m_in)
print len(ind[0])






def dissimilarity(m1,m2):
    k1 = m1.content.split()
    k2 = m2.content.split()
    ct = 0.0
    for k in k1:
        if k in k2:
            ct= ct + 1.0
    return 1.0 - ct / (len(k1)*1.0 + len(k2)*1.0 - ct)

def coverage(m1,l2):
    """ test the keywords coverage of l1 in l2"""
    l1 = m1.split()
    ct= 1e-10
    for k in l1:
        if k in l2:
            ct = ct  + 1.0
    return (ct+1e-10)/(len(l1)*1.0+len(l2)*1.0-ct+1e-10)


def findleaf(enter,d):
    q = Queue.Queue()
    q.put(enter)
    res = []
    while q.empty() != True:
        t = q.get()
        if(len(d)>t and len(d[t])>0):
            for e in d[t]:
                q.put(e)
        else:
            res.append(t)
    return res


def GreedySummarization(mt,index,K):
    keywords = [[0]]
    keywords.remove([0])
    dialogue = [[0]]
    dialogue.remove([0])
    for m in range(0,len(mt)):
        kw = mt[m].content.split()
        if index[m] == m:
            keywords.append(kw)
        else:
            keywords.append(kw)
            keywords[m] = keywords[index[m]]+(kw)
            while(len(dialogue)<=index[m]):
                dialogue.append([])
            #print m,index[m],dialogue
            dialogue[index[m]].append(m)
    summary=[]
    for k in range(0,K):
        goodf=0
        goodn=-1
        for m in range(0,len(mt)):
            if m in summary:
                continue
            leaf = findleaf(m, dialogue)
            gf = 0
            cc= 1.0
            for e in leaf:
                cc = cc * coverage(mt[m].content, keywords[e])

            div = 100.9
            ds = -1
            gf = cc
            for s in summary:
                dt = dissimilarity(mt[m],mt[s])
                if dt < div:
                    div = dt
                    ds = s
            if ds == -1:
                gf = cc
            else:
                gf = (cc*1.0 + div*9.0)/10.0
            if gf > goodf:
                goodf = gf
                goodn = m
        if goodn!=-1:
            summary.append(goodn)
    for s in summary:
        file.write(mt[s].content)
    return summary






file = open("k_80_greedy_res.txt","wb")

K = 80
millis = int(round(time.time() * 1000))

num_of_res=0
for m in range(0,len(M)):
    print m
    file.write(str(m)+' '+str(len(M[m]))+'\n')
    L = min(K,len(M[m]))
    GreedySummarization(M[m],ind[m],L)
    milliss = int(round(time.time() * 1000))
    num_of_res= num_of_res+len(M[m])
    file.write( str(num_of_res)+"," +str(milliss - millis)+'\n')

milliss = int(round(time.time() * 1000))
print milliss - millis
