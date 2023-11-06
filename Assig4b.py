N=int(input("Enter the no.of Queens [N] : "))
board=[] #Board la tayar kel
for j in range(N):
temp = []
for i in range(N):
temp.append(0) #[0,0,0,0]
board.append(temp)
#Cheking whether the (i,j)th position is safe for the queen or not
def isSafe(i,j):
for p in range(N):
if board[i][p]==1 or board[p][j] ==1:
return False
for x in range(N):
for y in range(N):
if i+j==x+y or i-j==x-y:
if board[x][y]==1:
return False
return True
#Checking places to fit the nqueen in the board
def nqueen(noq): #noq no. of queens
if noq==0:
return True
for i in range(N):
for j in range(N):
if board[i][j] !=1 and isSafe(i,j):
board[i][j] = 1 #First queen placed
if nqueen(noq - 1)==True: #other queens (N-1) will be placed
return True
board[i][j]=0 #queen ko nikalna hai
return False
if nqueen(N):
for i in board:
print(i)
else:
print("Hello hello hello")
