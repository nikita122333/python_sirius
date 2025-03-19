#exam1
def twoarray(nums):
  set_nums = set(nums)
  mas2arr = []
  while nums != []:
    mas2 = []
    for symb in set_nums:
      if symb in nums:
        nums.remove(symb)
        mas2 += [symb]
    mas2arr.append(mas2)
  return(mas2arr)