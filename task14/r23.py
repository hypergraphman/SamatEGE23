x = 9 ** 9 - 3 ** 9 + 9 ** 19 - 19
r = ''
p = 3
while x > 0:
    r = '0123456789ABCDEF'[x % p] + r
    x //= p
print(r)
print(r.count('2'))
print(sum(map(int, r)))