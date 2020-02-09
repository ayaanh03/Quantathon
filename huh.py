import random
import pprint

def payoff(a): 
    return (.6**(len(a))*max(a))

def test():
    a=[]
    rolls  =  []
    results=[]
    resultsn=[]
    countn={}
    size=10**7
    d=[1,2,3,4,5,6]
    for k in range(size):
        while True:
            random.shuffle(d)
            roll = d[0]
            rolls += [roll]
            x = payoff(rolls)
            a += [x]
            #pprint.pprint(rolls)
            if roll>=3: break
        i = a.index(max(a))
        #print("max",max(a))
        results += [max(a)]
        resultsn+= [i+1]
        a=[]
        rolls  =  []
    assert(len(results)==len(resultsn))
    avgr=sum(results)/len(results)
    avgn=sum(resultsn)/len(resultsn)

    for n in resultsn:
        if n in countn:
            countn[n] += 1
        else:
            countn[n] = 1
    avgcount = {}
    for n in countn:
        avgcount[n] = countn[n]/size

    pprint.pprint(avgcount)
    return ("\n",avgr,avgn)

pprint.pprint(test())