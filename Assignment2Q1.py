lst1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lst2=[]
for i in lst1:
    lst2.append(i[1])
for j in range(len(lst2)):
    for k in range(j,len(lst2)):
        if lst2[j]>lst2[k]:
            lst2[j],lst2[k]=lst2[k],lst2[j]          
lst3=[]
for f in lst2:
    for r in lst1:
        if f ==(r[1]):
          lst3.append(r)
print(lst3)
