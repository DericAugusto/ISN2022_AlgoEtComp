# Algorithme et complexité
# Annexe des fonctions créées
# Déric Augusto FRANÇA DE SALES
# 30/12/22

import numpy as np

def balance2Plateaux(W):

	# Attribution d'éléments aux plats
	leftPlate = W[:]
	rightPlate = []

	oddLoop = True
	while 1: 
		# Calcul du poids total des assiettes
		weightLeft = sum(leftPlate)
		weightRight = sum(rightPlate)

		# 1ère condition d'arrêt : sortie d'une boucle infinie
		if oddLoop:
			weightLeftPrev = weightLeft
			oddLoop = False
		else:
			if weightLeftPrev == weightLeft:
				break
			else:
				oddLoop = True

		# Calcul de la différence de poids entre les deux plaques
		diffWSides = abs(weightLeft - weightRight)
		
		# Passer l'élément qui minimise la différence avec l'autre plaque
		diffWList = []
		if weightLeft > weightRight:
			for i in range(len(leftPlate)):
				diffWList.append(diffWSides - leftPlate[i])
			# 2ème condition d'arrêt : si la différence ne peut être minimisée
			if all(n <= 0 for n in diffWList):
				break
			else:
				minPositive = min([x for x in diffWList if x >= 0])
				rightPlate.append(leftPlate.pop(diffWList.index(minPositive)))
		else:
			for i in range(len(rightPlate)):
				diffWList.append(diffWSides - rightPlate[i])
			if all(n <= 0 for n in diffWList):
				break
			else:
				minPositive = min([x for x in diffWList if x >= 0])
				leftPlate.append(rightPlate.pop(diffWList.index(minPositive)))

	return leftPlate, rightPlate


def backtracking(W, n = 2, X = np.array([]), solutions = {}):
  '''
    Realiza o balanceamento dos pesos W em n pratos, através de um algoritmo
    backtracking. Devolve a matriz de solução com a melhor solução encontrada. 
  '''
  # Inicializando função
  if X.size == 0 :
    lenW = len(W)
    X = np.zeros((n,lenW), dtype=int)
    X[0,:] = np.ones((lenW), dtype=int)

  # calcula a lista dos pesos balanceados 
  weightList = totalWeight(W, X)
  # armazena a solução atual no dicionário de soluções
  solutions[balanceValue(weightList)] = np.copy(X)

  # caso trivial (peso distribuído em cada balança é exatamente igual)
  elementsAreEqual = np.all(weightList == weightList[0])
  elementsAreInScales = np.all(np.any(X == 1, axis=0))
  if elementsAreEqual and elementsAreInScales:
    return X

  # caso recursivo
  else:
    try:
      X = moveWeight(X, -1)
      return backtracking(W, n, X, solutions)
      # caso tenha tentado todas as possibilidades,
      # retorna a melhor solução encontrada
    except IndexError:
      return solutions[min(solutions.keys())]


def backtrackingSol(W, n = 2, solution = False, X = np.array([]), solutions = {}):
  '''
    Realiza o balanceamento dos pesos W em n pratos, através de um algoritmo
    backtracking. Devolve a matriz de solução com a melhor solução encontrada. 
    Se a variável solution for definida para verdadeiro, devolve a tupla sendo
    o primeiro elemento a matriz com a melhor solução X e o segundo, um 
    dicionário de soluções, onde as chaves são as grandezas que representa o 
    quão boa é a solução e as chaves a solução X. 
  '''
  # Inicializando função
  if X.size == 0 :
    lenW = len(W)
    X = np.zeros((n,lenW), dtype=int)
    X[0,:] = np.ones((lenW), dtype=int)
  
  # calcula a lista dos pesos balanceados 
  weightList = totalWeight(W, X)
  # armazena a solução atual no dicionário de soluções
  solutions[balanceValue(weightList)] = np.copy(X)

  # caso trivial (peso distribuído em cada balança é exatamente igual)
  if solution == False:
    elementsAreEqual = np.all(weightList == weightList[0])
    elementsAreInScales = np.all(np.any(X == 1, axis=0))
    if elementsAreEqual and elementsAreInScales:
      return X

  # caso recursivo
  else:
    try:
      X = moveWeight(X, -1)
      return backtracking(W, n, solution, X, solutions)
      # caso tenha tentado todas as possibilidades,
      # retorna a melhor solução encontrada
    except IndexError:
      if solution == True:
        return solutions[min(solutions.keys())], solutions
      else: 
        return solutions[min(solutions.keys())]


def moveWeight(X, col):
  ''' 
   Recebe como entrada a matriz de posicionamento dos pesos X e a coluna onde 
   os pesos serão movimentados. É uma função recursiva onde a movimentação 
   sempre começa da última coluna até a primeira. O elemento da coluna é movido
   para a linha de baixo, representando uma movimentação entre pratos diferentes
   da balança. Tem como saída a matrix X com o peso movimentado na coluna 
   indicada.
  '''
  n = X.shape[0]
  column = X[:, col]
  number1LineIndex = int(np.where(column == 1)[0])

  # caso trivial (movendo o 1)
  if number1LineIndex <= n-2 :  
    # movendo o 1 para a linha abaixo
    X[number1LineIndex, col] = 0
    X[number1LineIndex + 1, col] = 1
    return X

  # caso recursivo 
  # (não dá pra mover o 1, então movemos na coluna anterior)
  else :
    # movendo o um para a primeira linha na coluna analisada
    X[number1LineIndex, col] = 0
    X[0, col] = 1
    return moveWeight(X, col-1)


def totalWeight(W, X):
  '''
    devolve numpy array dos pesos balanceados entre cada prato a partir dos 
    vetores W de pesos e X, que indica onde os pesos estão posicionados entre
    cada balança. 
  '''
# devolve uma lista numpy dos pesos balanceados entre cada prato a partir dos 
# vetores W de pesos e X
  numRows, numColumns = X.shape
  weightList = np.array([])
  for row in range(numRows):
    plateWeight = 0
    for column in range(numColumns):
      plateWeight += W[column]*X[row][column]
    weightList = np.append(weightList, [plateWeight])
  return weightList


def weightDifference(weightList):
  '''
    Retorna o vetor (numpy array) que indica todas as diferenças dos elementos 
    entre si, a partir do vetor de pesos. 
  '''
# retorna o vetor com as diferenças entre todos os elementos entre si
  diffList = np.array([], dtype=int)
  weightList = np.copy(weightList)
  weightsToCompare = np.copy(weightList)

  # para cada elemento
  for index1 in range(weightList.size):
    weightOnPlate = weightList[index1]
    weightsToCompare = np.delete(weightsToCompare, 0)

    # Diferença entre o elemento X e todos os outros
    for index2 in range(weightsToCompare.size):
      diff = abs(weightOnPlate - weightsToCompare[index2])
      diffList = np.append(diffList, [diff])
  
  return diffList


def balanceValue(weightList):
  '''
    Retorna um valor que indica o quão balanceada está a solução. Esse valor é
    gerado a partir da média da lista de diferenças entre os pesos. Recebe como
    entrada a lista de pesos totais em cada prato das balanças.
  '''
  # devolve o valor que define o quão balanceada está a solução
  diffList = weightDifference(weightList)
  return sum(diffList)/len(diffList)
