def sumar(*args):
  result = 0
  for n in args:
    result += n
  return result

def restar(*args):
  result = 0  
  cont = 0
  for n in args:
    if cont >= 1:
      result -= n
    else:
      result = n
    cont += 1
  return result

def multiplicar(*args):
  result = 1
  for n in args:
    result *= n
  return result

def dividir(*args):
  temp = []
  for item in args:    
    temp.append(item)
  result = 0
  n = 0
  while n < len(temp):
    if n <= (len(temp)-2):
      result = temp[n] / temp[n+1]
      temp[n+1] = result
    n += 1
  return result
