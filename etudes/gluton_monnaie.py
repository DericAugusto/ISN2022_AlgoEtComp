# Algorithime Gluton - Greedy
# 21/02/23


print("\nProblème pièce de monnaie Interactive :\n") #-----------------

change = 550
values = [200, 100, 50, 20, 10, 5, 33, 2, 1, 27]

def find_greater(values, limit):
  greater_element = 0
  for i in range(len(values)):
    if values[i] <= limit and values[i] >= greater_element:
      greater_element = values[i]
  return greater_element

def piece_monaie(values, limit):
  wallet = []
  cash_register = values.copy()

  while 1:
    greater_element = find_greater(cash_register, limit)
    if sum(wallet) + greater_element >= limit:
      break
    if greater_element == 0:
      break
    wallet.append(greater_element)
    cash_register.remove(greater_element)
  return wallet


wallet = piece_monaie(values, change)
print(wallet)
print(sum(wallet))
























