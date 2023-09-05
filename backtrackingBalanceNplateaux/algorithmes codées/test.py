#import os
#os.chdir(sys.path[0])
from functions import backtracking 

n = 3

#W1 = [3, 2, 1, 4, 2]
#W2 = [1, 2, 3, 6]
#W3 = [3, 13, 9, 8, 1, 5]
#W4 = [3, 10, 15, 5, 2, 1]
W4 = [-100, 843, -300, 400, 43]

#sol1 = backtracking(W1,n)
#sol2 = backtracking(W2,n)
#sol3 = backtracking(W3,n)
sol4 = backtracking(W4,2)

#print("Solution 1 :"); print(sol1)
#print("Solution 2 :"); print(sol2)
#print("Solution 3 :"); print(sol3)
print("Solution 4 :"); print(sol4)