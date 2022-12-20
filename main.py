# a = ''
# for i in range(1,26):
#     if i <6:
#         print(i,end = ',')
#     if i>=6 and i<=10:
#         a = a+str(i)
#
#     if i>10:
#         print(i,end = ',')
#
# for j in a:
#     print(int(j),end = ',')
#
# l="AC*wv12n/:#e123we2.45oin  (fwoi6n#a98nfwb+owi"   #[2.45, 6, 12, 98, 1234]
# l1=[]
# str=""
# for i in l:
#     if i.isdigit() or i=='.':
#         str+=i
#     else:
#         if str!="":
#             l1.append(eval(str))
#             str=""
# if str!='':
#     l1.append(eval(str))
# print(sorted(l1))
def str(l):
    l1=[]
    str=""
    for i in l:
        if i.isdigit() or i=='.':
            str+=i
        else:
            if str!="":
                l1.append(eval(str))
                str=""
    if str!='':
        l1.append(eval(str))
    return l1
l="AC*wv12n/:#e123we2.45oin  (fwoi6n#a98nfwb+owi"
print(sorted(str(l)))