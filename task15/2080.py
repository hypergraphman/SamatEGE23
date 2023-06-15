for  a in range(1, 1000):
    if all((x**2 - 10*x + 16 > 0) or ( y**2 - 10*y + 21 > 0) or (x*y < 2*a) for x in range (1, 1000) for y in range(1, 1000)):
        print(a)