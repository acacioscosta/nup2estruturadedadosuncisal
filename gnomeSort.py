import time

def gnomeSortDetailed(list):
  start               = time.time()
  index               = 0
  amountMovement      = 0
  amountVerifications = 0

  while index < len(list):
    if index == 0:
      index += 1

    if list[index] >= list[index -1]:
      print(list, '- Verificou ', list[index], 'e', list[index - 1])
      index += 1
    else:
      list[index], list[index - 1] = list[index - 1], list[index]
      print(list, '- Movimentou', list[index], 'e', list[index - 1])
      index -= 1
      amountMovement += 1

    amountVerifications += 1

  print('-----------------------------------------------')
  print('Lista ordenada:', list)
  print('Tempo         :', time.time() - start)
  print('Movimentacoes :', amountMovement)
  print('Verificacoes  :', amountVerifications)

def gnomeSort(list):
  start = time.time()
  index = 0

  while index < len(list):
    if index == 0:
      index += 1

    if list[index] >= list[index -1]:
      index += 1
    else:
      list[index], list[index - 1] = list[index - 1], list[index]
      index -= 1

  print('Lista ordenada:', list)
  print('-----------------------------------------------')
  print('Tempo:', time.time() - start)

initialList = [10, 5, 2, 11, 1]
print('Lista inicial:', initialList)
print('-----------------------------------------------')

# gnomeSortDetailed(initialList)
gnomeSort(initialList)