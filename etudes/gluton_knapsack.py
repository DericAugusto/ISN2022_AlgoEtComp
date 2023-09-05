# Algorithime Gluton - Greedy
# 21/02/23

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


print("\n\nProblème du sac à dos Interactive :\n") #-----------------


def find_index_greater(volume, value, sac, space):
  index_greater = None

  used_space = 0
  for i in range(len(sac)):
    used_space += sac[i]*volume[i]
  left_space = space - used_space

  greater_ratio = 0
  for i in range(len(sac)):
    if sac[i] == 0 :
      ratio = value[i]/volume[i]
      if ratio >= greater_ratio and volume[i] <= left_space:
        index_greater = i
        greater_ratio = ratio
    
  return index_greater


def knapsack(volume, value, sac, space):
  while 1:
    index_greater = find_index_greater(volume, value, sac, space)
    if index_greater == None:
      break
    sac[index_greater] = 1
  
  return sac


volume = [230, 6, 70, 6, 12, 83, 8, 45, 16, 2]
value = [700, 120, 10, 300, 550, 50, 88, 32, 43, 1000]
space = 150

sac = [0]*len(volume)

print("\nvolume:", volume)
print("value:", value)
print("total space: ", space)
print("ratio:", ratio(volume, value))

print("\nsac solution:", knapsack(volume, value, sac, space))
earnings, volume_used = solution(volume, value, sac)
print("earnings: ", earnings)
print("volume used: ", volume_used)






