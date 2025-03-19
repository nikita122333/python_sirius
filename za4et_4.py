#зачет4
def reverse(strr, num):
  import math
  answ = ''
  r = 0
  first = 0
  last = num
  flag = 2
  for _ in range(math.ceil(len(strr)/num)):
    srez = strr[first : last]
    if flag%2 == 0:
      answ = answ + srez[::-1]
    else:
      answ = answ + srez
    first += num
    last += num
    flag +=1
  return answ