max=20
for n in range(1, max +1):
    print(end=str(n) + ': ')
    for factor in range(1, n + 1):
        if n % factor==0:
            print(factor, end=' ')
    print()
