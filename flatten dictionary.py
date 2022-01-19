def check(a):
    for i in range(len(a)):
        x = a[i]-a[i-1]
        y = a[i-1]-a[i-2]
        if x**2 > y**2:
            e = True
        else:
            e = False
    return e
n = list(map(int, input().split()))
m = check(n)
print(m)