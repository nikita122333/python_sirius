#зачет1 (проверку на букву можно через ord() и сравнить с определенным диапазоном чисел)
def abreviature(frase):
  ans = ""
  for index in range(len(frase)):
    if frase[index].isalpha():
      if index == 0 or frase[index-1]== ' ':
        ans = ans+frase[index]
  return(ans)