
#n(1/3)**n-1*(2/3)
import pprint
ssum=0
n=1
def p(n):
    return n*((1/3)**(n-1))*(2/3)


while True:
    ssum+=p(n)
    n+=1
    print(ssum,n)