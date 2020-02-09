import random
import pprint
i=1
ssum={1:0,2:0,3:0,4:0,5:0,6:0}
while True:
    a=random.randint(1,6)
    ssum[a]+=1
    ssum[a]/=i
    i+=1
    pprint.pprint(ssum)
