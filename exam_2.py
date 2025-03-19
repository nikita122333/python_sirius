#exam2
def calcDistance(text_way):
  count = ''
  sum = 0
  for ind in range(len(text_way)):
    if text_way[ind].isdigit():
      count = count + text_way[ind]
      if text_way[ind+1].isalpha():
        if text_way[ind+1] == 'm':
          sum += int(count)
        else:
          sum += int(float(count) * 1000)
        count = ''
  return sum