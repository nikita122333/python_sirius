#зачет2
def num_in_int(intg):
  int_str = str(intg)
  for num in range(10):
    flag = 0
    num_str = str(num)
    for index in range(len(int_str)):
      if num_str== int_str[index]:
        flag +=1
    print(num_str, ': ', flag)
