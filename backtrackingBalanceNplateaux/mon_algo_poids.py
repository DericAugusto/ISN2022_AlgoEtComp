poids = [23,44,33,11,77,44,33]

balanceA = []
balanceB = []

% distribuer les poids entre les plateux
for i in poids:
  sumA = sum(balanceA)
  if sumA > sumB:
    balanceB.append(i)
  else:
    balanceA.append(i)

% chercher le poid dans le platux plus chargée pour reduire la différence 
sumA = sum(balanceA)
sumB = sum(balanceB)
if sumA > sumB:
  difAB = sumA - sumB
  difDif = []
  for i in sumA:
    difDif.append(sumA - difAB)

% pegar o que tem a maior diferença em difDif e jogar pro outro lado

% fazer isso até que durante x interações a solução não melhore.
    



