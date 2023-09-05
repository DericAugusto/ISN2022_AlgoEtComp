# Algorithime Gluton - Greedy
# 23/02/23

# aux functions ------------------------------
def ratio(volume, value):
  ratio_list = []
  for i in range(len(volume)):
    ratio_list.append(value[i]/volume[i])
  return ratio_list

def solution(volume, value, sac):
  volume_used = 0
  earnings = 0
  for i in range(len(sac)):
    volume_used += sac[i]*volume[i]
    earnings += sac[i]*value[i]
  return earnings, volume_used
# -------------------------------------------- 


print("\n\nProblème du sac à dos Recursive :\n") #-----------------

def find_index_greater(volume, value, space):
  ratio = []
  n_size = len(volume)
  for i in range(n_size):
    ratio.append(value[i]/volume[i])
  
  greater_ratio = 0
  for i in range(n_size):
    if ratio[i] > greater_ratio and volume[i] <= space:
      greater_ratio = ratio[i]
      indx_greater = i
  return indx_greater


def knapsack(volumes, values, space, indexes):

  indx_greater = find_index_greater(volumes, values, space)

  # preciso ler toda a lista de indexes pra saber como armazenar esse index aqui:

  # descobrindo quantos elementos anteriores eu tirei pra adicionar depois
  past_indexes = 0
  for i in range(len(indexes)):
    if indexes[i] >= indx_greater:
      past_indexes += 1
  correct_indx = indx_greater + past_indexes
  indexes.append(correct_indx)


  volumes_new = volumes.pop(indx_greater)
  values_new = values.pop(indx_greater)

  volume_ocupied = 

  space_available =  space - volume_ocupied


  # trivial case
  return indexes


  # recursive case
  return knapsack(volumes_new, values_new, space_available, indexes)
    



volumes = [230, 6, 70, 6, 12, 83, 8, 45, 16, 2]
values = [700, 120, 10, 300, 550, 50, 88, 32, 43, 1000]
space = 150




print("\nvolume:", volumes)
print("value:", values)
print("total space: ", space)
print("ratio:", ratio(volumes, values))



