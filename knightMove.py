N = 8

def printSolution(board): 
	for i in range(N): 
		for j in range(N): 
			print(board[i][j],end =' ') 
		print() 


def iCanPlaceKnight(board, r, c):

    if (r>= 0 and c>= 0 and r <N  and c <N and board[r][c] == 0) :
        return True
    return False


def knightMoveUtils(board, count_no, curRow, curCol):
    if count_no == N*N:
        return True

    rowDir = [+2, +1, -1, -2, -2, -1, +1, +2]
    colDir = [+1, +2, +2, +1, -1, -2, -2, -1]

    # rowDir = [ -1, 1, -2, 2, -1, 1, -2, 2]
    # colDir = [2, 2, 1, 1, -2, -2, -1, -1]

    for i in range(8):
        nextRow = curRow + rowDir[i]
        nextCol = curCol + colDir[i]
        
        if iCanPlaceKnight(board, nextRow, nextCol) == True:
            board[nextRow][nextCol] = count_no + 1
            
            if knightMoveUtils(board, count_no + 1, nextRow, nextCol) == True:
                return True
            board[nextRow][nextCol] = 0

    return False



def solveKM():
    global N
    N = int(input())
    board = [[0 for i in range(N)]for i in range(N)]    
    board[0][0] = 1
    if (knightMoveUtils(board, 1, 0, 0)) == True:
        print("YES")
        printSolution(board)
    else:
        print("NO")
    return True

solveKM()

