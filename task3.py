def task3(dnk):
  zipdnk = str()
  symb = "0"
  flag = 1
  for i in dnk:
    if i == symb:
      flag +=1
    elif symb == '0':
      pass
    else:
      zipdnk = zipdnk + symb + str(flag)
      flag = 1
    symb = i
  zipdnk = zipdnk + symb + str(flag)
  return(zipdnk)

