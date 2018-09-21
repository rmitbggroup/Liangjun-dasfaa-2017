
def readsummary(file,my=False):
    summary = [[0]]
    summary.remove([0])
    f = open(file,"rb");
    lines = f.readlines()
    ct=0
    summary.append([])
    indexappend=1
    if my:
        indexappend=0
    for l in lines:
        numbers = l.split()
        if l.split(',')[0].isdigit():
            summary.append([])

        if len(numbers) ==2 and numbers[0].isdigit():
            if int(numbers[0])==ct+indexappend:
                line_togo = int(numbers[1])
                summary.append([])
            else:
                ct=ct+1
        else: summary[ct].append(l)
    return summary

def Coverage(l1,l2):
    ct = 0.0
    for i in l2:
        if i in l1:
            ct=ct+1.0
    return (ct)/(len(l2)*1.0)

def dissimilarity(m1,m2):
    k1 = m1.split()
    k2 = m2.split()
    ct = 0.0
    for k in k1:
        if k in k2:
            ct= ct + 1.0
    return 1.0 - ct / (len(k1)*1.0 + len(k2)*1.0 - ct)

def Diversity(filter,k):
    l1 = []
    div=0.0
    num_div = 0
    for s in summary:
        if (len(s) < filter):
            continue
        l1 = s[0:k]
        ct = 0.0
        for i in l1:
            di = 1.0
            for j in l1:
                if(i!=j):
                    d=dissimilarity(i,j)
                    if d < di:
                        di = d
            ct = ct + di
        div = div+ ct / (len(l1)*1.0)
        num_div= num_div+1
    return div / num_div


def Effectiveness(filter):
    sumset = []
    e = 0.0
    ct_e = 0
    for s in summary:
        if(len(s)<filter):
            continue
        fulls = []
        for ss in range(0,len(s)-1):
            fulls = fulls+s[ss].split()
            if(ss<k):
                sumset=sumset+s[ss].split()

        r = Coverage(sumset,fulls)
        e=e+r
        ct_e=ct_e+1.0

    print e/ct_e*1.0


    return


W = 10
global tau
tau = 5
T = []
def Efficiency(filter):
    T = []
    pre = 0
    mx =0
    for mt in summary:
        if(len(mt)<2 or len(mt) < filter):
            continue
        if(len(mt)>mx):
            mx = len(mt)
        if mt[-1][0].isdigit()==False:
            continue

        dd = mt[-1].split(',')[1]
        #print len(mt),(len(mt)*1.0+100.0/ta)*1.0/(filter*1.0)
        T.append((int(dd)-pre))
        pre = int(dd)
    return T


# ssss = readsummary("centroid_res.txt")
# for s in range(0,len(ssss)):
#     if len(ssss[s]) > 10 and len(ssss[s])<20:
#         print s
def Efficiency_test():
    for i in range(0,10):
        n = i*10+10
        tau = i*5+5
        T = Efficiency(n)
        ss = 0.0
        ct = 0.0
        for s in T:
            ss= ss+s
            ct = ct +1.0
        if ct<0.1:
            print i*10+5, 0.0;
            continue
        print  ss/ct

def PickCases(no):
    summary=readsummary("centroid_res.txt",my=False)
    for i in range(0,len(summary)):
        if i == no:
            for item in summary[i]:
                print item
    summary=readsummary("eff_greedy_res.txt",my=True)
    for i in range(0,len(summary)):
        if i == no:
            for item in summary[i]:
                print item
    summary=readsummary("lex_res.txt",my=False)
    for i in range(0,len(summary)):
        if i == no:
            for item in summary[i]:
                print item
PickCases(74)




