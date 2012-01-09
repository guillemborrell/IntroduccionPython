if __name__ == '__main__':
    f0 = 1
    f1 = 1
    n = 1
    print f0,f1,
    while n < 20:
        f0, f1 = f1, f1+f0
        print f1,
        n += 1
