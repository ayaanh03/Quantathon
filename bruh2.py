import random
import pprint

def payoff(a): 
    return (.6**(len(a))*max(a))

def test():
    a=[]
    rolls  =  []
    results=[]
    resultsn=[]
    for k in range(10000):
        for n in range(1,100):
            roll = random.randint(1,6)
            rolls += [roll]
            x = payoff(rolls)
            a += [x]
        i = a.index(max(a))
        print(i)
        #print("max",max(a))
        results += [max(a)]
        resultsn+= [i+1]
        a=[]
        rolls  =  []
    assert(len(results)==len(resultsn))
    avgr=sum(results)/len(results)
    avgn=sum(resultsn)/len(resultsn)
    return ("\n",avgr,avgn)

pprint.pprint(test())