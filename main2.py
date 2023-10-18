#Паліндром 0642?
# def find_polindr(walter):
#     return str(walter)==str(str(walter)[::-1])
# def has_polimdrom(number):
#     count = 0
#     for i in range(1,number+1):
#         if find_polindr(i):
#             count+=1
#     return count
# n=int(input())
# print(has_polimdrom(n))
#0599
n=int(input())
list1=list(map(int,input().split()))
m=int(input())
list2=list(map(int,input().split()))
k=int(input())
listing=[]
for i in list1:
    for item in list2:
        summ=i+item
        listing.append(summ)
listing.sort()
print(listing[k-1])