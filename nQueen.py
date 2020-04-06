# Python program to solve N Queen 
# Problem using backtracking 

# global N
# N = 4

def printSolution(board):    
	for i in range(N): 
		for j in range(N): 
			print (board[i][j], end =" ")
		print()


def isSafe(board, row, col): 
	
	# Check this row on left side 	
	for i in range(col): 
		if board[row][i] == 1: 
			return False

	# Check upper diagonal on left side 
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	# Check lower diagonal on left side 
	for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	return True

def solveNQUtil(board, col): 

	if col >= N: 
		return True
	

	for i in range(N): 

		if isSafe(board, i, col): 

			board[i][col] = 1			

			if solveNQUtil(board, col + 1) == True: 
				return True

			board[i][col] = 0
	# print(board)
	return False


def solveNQ():
	global N
	
	N = int(input())
	board = [[0 for i in range(N)]for i in range(N)]
	print(board)
	if solveNQUtil(board, 0) == False: 
		print ("NO")
		return False

	print("YES")
	printSolution(board) 
	return True


solveNQ() 


