def task4(string, substring):
  string = list(string)
  substring = list(substring)
  flag = False
  sum = 0
  for ind in range(len(string)):
    if string[ind] == substring[0]:
      flag = True
      next_ind = ind+1
      e = 1
      while e<len(substring) and next_ind < len(string):
        if substring[e] != string[next_ind]:
          flag = False
        next_ind+=1
        e+=1
      if flag==True:
        sum+=1
  return(sum)