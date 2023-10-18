#Step 1
n,m  = list(map(int, input().split()))
list=list(map(int,input().split()))
#Step 2
m*=100
list = [i * 100 for i in list]
#Step 3
list.sort()
index_of_low=0
#Step 4
while m>0:
    lowest_value=list[0]
    index_of_low = 0
    for i in range(1, len(list)):
        if list[i]==lowest_value:
            index_of_low+=1
        else:
            break
    #Step 5
    if index_of_low+1<len(list):
        nextDifference=list[index_of_low+1]-list[index_of_low]
    else:
        nextDifference=10**12
    ammount_of_lowesr_values=index_of_low+1
    #Step 6
    if nextDifference*ammount_of_lowesr_values>m:
        difference=m//ammount_of_lowesr_values
        for i in range(index_of_low,-1,-1):
            list[i]+=difference
            m-=difference
        #остача
        for i in range(index_of_low, -1, -1):
            if m==0: break
            list[i]+=1
            m-=1
    else:
        nextDifference=list[index_of_low+1]-list[index_of_low]
        for i in range(index_of_low, -1, -1):
            list[i] += nextDifference
            m -= nextDifference
#Step 7
print(" ".join(
    map(lambda x: f"{x/100:.2f}", list)
))











