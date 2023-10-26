def checking(station,x,v):
    timeTramvToStation=station//v
    timeBoyToStation=abs(station-x)
    return timeBoyToStation<=timeTramvToStation
v,x,a,b=map(int,input().split())
caseA=checking(a,x,v)
caseB=checking(b,x,v)
if caseA and caseB:
    if abs(x-a)<=abs(x-b):
        print("1")
    else:
        print("2")
elif caseA or caseB:
    if caseA:
        print("1")
    else:
        print("2")
else:
    print("-1")