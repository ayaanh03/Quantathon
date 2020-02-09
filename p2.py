import random
def payoffs(N):
    a=[0]
    for i in range(1,N+1):
        a+=[(i/N)]
    return random.choice(a[0:])

def payoff(n,L):
    return (.6**n)*(max(L))

def test(N):
    currp=[]
    size=0
    for i in range(size):
        currp+=[payoffs(N)]
        prev=payoff


