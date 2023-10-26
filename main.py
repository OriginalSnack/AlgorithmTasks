#0890
# def worker(s):
#     walter=list(s)
#     count=0
#     for i in range(len(walter)-1):
#         if walter[i]==walter[i+1]:
#             if walter[i]=='B':
#                 walter[i]=='Y'
#                 count+=1
#             else:
#                 walter[i]=='B'
#                 count+=1
#     return count
# s=input()
# print(worker(s))
def balls(a,b):
    list_y=['Y']*a
    list_g=['G']*b
    list_end=[]
    if len(list_g)>len(list_y):
        # while(len(list_g)!=0):
        #     list_end.append('G')
        #     list_end.append('Y')
        #     list_g.pop()
        #     list_y.pop()
        for i in range(a+b):
            list_end.append('G')
            list_end.append('Y')
    else:
        while(len(list_y)!=0):
            list_end.append('Y')
            list_end.append('G')
            list_y.pop()
            list_g.pop()
    return list_end
a,b =map(int,input().split())
print(balls(a,b))



