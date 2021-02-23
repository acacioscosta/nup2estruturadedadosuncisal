import time

def gnomeSortWithDetails(list):
  started             = time.time()
  index               = 0
  amountMovement      = 0
  amountVerifications = 0
  infoToPrint         = list

  while index < len(list) - 1:
    if list[index] > list[index + 1]:
      list[index + 1], list[index] = list[index], list[index + 1]
      amountMovement += 1
      infoToPrint = str(list) + ' ' + str(list[index + 1]) + ' > ' + str(list[index]) + ' - Movimentou => ' + str(list[index + 1]) + ' e ' + str(list[index])

      if index > 0:
        index -= 2

    print(infoToPrint)
    infoToPrint = str(list) + ' ' + str(list[index]) + ' > ' + str(list[index + 1]) + ' - Não movimentou'
    index += 1
    amountVerifications += 1

  print('----------------------------------------')
  print('Verificações :', amountVerifications)
  print('Movimentações:', amountMovement)
  print('Tempo        :', time.time() - started)

def gnomeSortWithoutDetails(list):
  started = time.time()
  index   = 0

  while index < len(list) - 1:
    if list[index] > list[index + 1]:
      list[index + 1], list[index] = list[index], list[index + 1]

      if index > 0:
        index -= 2

    index += 1

  print('Lista ordenada =>', list)
  print('----------------------------------------')
  print('Tempo:', time.time() - started)

data = [10, 5, 2, 11, 1]
print('Lista inicial =>', data)
print('----------------------------------------')

gnomeSortWithDetails(data)
gnomeSortWithoutDetails(data)