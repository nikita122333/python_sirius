#зачет3
def pascal(rowIndex):
  if rowIndex ==0:
    return([1])
  elif rowIndex ==1:
    return([1, 1])

  pascstr = [1,1]
  while rowIndex != len(pascstr)-1:
    pascstr2 = [1]
    for i in range(len(pascstr)-1):
      pascstr2.append(pascstr[i]+pascstr[i+1])
    pascstr2.append(1)
    pascstr = pascstr2
  return(pascstr)