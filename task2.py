def task2(a,b):
    if a>b:
        c = a
        while c%b != 0:
            c +=a
    else:
        c = b
        while c%a != 0:
            c +=b
    return c
task2(7,5)