
count = 0

def calculAn(a,n):
    global count
    res = 0
    if n == 1:
        count += 1
        return a
    if n%2 == 0:
        count += 1
        res = calculAn(a, n//2)*calculAn(a, n//2)
    else:
        count += 1
        res = calculAn(a, n//2)*calculAn(a, n//2)*a
    return res


a = 3
n = 8

print()
print(calculAn(a,n))
print()
print(count)
print()
print(a**n)
