def task2(com1,com2):
    c = 0
    while c%com1 != 0 or c%com2!=0 or c ==0:
        if com1 > com2:
            c +=com1
        else:
            c +=com2
    return c
