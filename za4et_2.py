#зачет2
def num_in_int(intg, num):
  int_str = str(intg)
  num_str = str(num)
  flag = 0
  for index in range(len(int_str)):
    if num_str== int_str[index]:
      flag +=1
  return(flag)