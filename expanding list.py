def expanding(lst):
    lst1=[]
    for i in range(1, len(lst)):
        a = lst[i]-lst[i-1]
        lst1.append(abs(a))
    e = True
    for i in range(1, len(lst1)):
        if lst1[i]<=lst1[i-1]:
            e = False
            break

    return e

lst = list(map(int,input().split()))
print(expanding(lst))