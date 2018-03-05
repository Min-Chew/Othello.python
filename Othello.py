'''****************************************************************
** Program Filename: Othello
** Author: Min Chew
** Date: 26 November 2017
** Description: This is a "X" and "O" version of the game Othello
** Input: Row, column, if want to play for another round 
** Output: The game commences 
*******************************************************************'''


'''****************************************************************
** Function: preboard
** Description: Setting up the frame of the board
** Parameters: r, c
** Pre-conditions: The parameters must be ints
** Post-conditions: Returns empty board 
*******************************************************************'''
def preboard(r,c):
	board = [' ']*r
	for i in range (r):
		board[i] = [' ']*c
	return board 


'''****************************************************************
** Function: print_board
** Description: Prints the board
** Parameters: board
** Pre-conditions: There must be a board to print 
** Post-conditions: Prints board
*******************************************************************'''
def print_board(board):
	print("\n------------------------")
	for i in range (len(board)):
		for j in range (len(board[i])):
			print("|"+board[j][i]+"|", end='')
		print("\n------------------------")


'''*********************************************************************
** Function: get_input
** Description: Gets user input on row/column position
** Parameters: variable, fixed
** Pre-conditions: Must know if going to ask for row/column
** Post-conditions: Asks user for row/column postition and gets input  
************************************************************************'''	
def get_input(variable, fixed):
	x = input(variable+" position (1-"+str(fixed)+"): ")
	while x<"1" or x>str(fixed):
		print("That is not a valid choice, try again.")
		x = input(variable+" position (1-"+str(fixed)+") ")
	return int(x)-1


'''****************************************************************
** Function: place_token
** Description: Places token on the board
** Parameters: board, token, x, y
** Pre-conditions: Must have a board and valid token 
** Post-conditions: Places token on board 
*******************************************************************'''
def place_token(board, token, x, y):
	board[x][y] = token
	return board


'''***********************************************************************
** Function: check_left
** Description: Checks left of token to see if token position is valid
** Parameters: x, y, token, row, board
** Pre-conditions: Must have a board and potential token 
** Post-conditions: Checks if its a valid move 
**************************************************************************'''
def check_left(x, y, token, row, board):
	myList = []
	while board[x][y] == token:
		if board[x-1][y] == ' ' or x-1 < 0:
			return ' '
		else:
			if board[x-1][y] == token:
				return ' '
			else:
				if token == "X":
					optoken = "O"
				else: 
					optoken = "X"
				x = x-1
				while x>=0 and board[x][y] == optoken:
					myList += x,y
					x -= 1
				if x<0:
					return ' '
				if board[x][y] == token:
					return myList
	return ' ' 	


'''***********************************************************************
** Function: check_right
** Description: Checks right of token to see if token position is valid
** Parameters: x, y, token, row, board
** Pre-conditions: Must have a board and potential token 
** Post-conditions: Checks if its a valid move 
**************************************************************************'''
def check_right(x, y, token, row, board):
	myList = []
	while board[x][y] == token:
		if x+1 > 7 or board[x+1][y] == ' ':
			return ' '
		else:
			if board[x+1][y] == token:
				return ' '
			else:
				if token == "X":
					optoken = "O"
				else:
					optoken = "X"
				x = x+1
				while x<=7 and board[x][y] == optoken:
					myList += x,y
					x += 1
				if x>7:
					return ' '
				if board[x][y] == token:
					return myList
	return ' '


'''***********************************************************************
** Function: check_up
** Description: Checks above token to see if token position is valid
** Parameters: x, y, token, row, board
** Pre-conditions: Must have a board and potential token 
** Post-conditions: Checks if its a valid move 
**************************************************************************'''
def check_up(x, y, token, column, board):
	myList = []
	while board[x][y] == token:
		if board[x][y-1] == ' ' or y-1 < 0:
			return ' '
		else:
			if board[x][y-1] == token:
				return ' '
			else:
				if token == "X":
					optoken = "O"
				else:
					optoken = "X"
				y = y-1
				while y>=0 and board[x][y] == optoken:
					myList += x,y
					y -= 1
				if y<0:
					return ' '	
				if board[x][y] == token:
					return myList
	return ' '
	

'''***********************************************************************
** Function: check_down
** Description: Checks below token to see if token position is valid
** Parameters: x, y, token, row, board
** Pre-conditions: Must have a board and potential token 
** Post-conditions: Checks if its a valid move 
**************************************************************************'''
def check_down(x, y, token, column, board):
	myList = []
	while board[x][y] == token:
		if y+1 > 7 or board[x][y+1] == ' ': 
			return ' '
		else:
			if board[x][y+1] == token:
				return ' '
			else:
				if token == "X":
					optoken = "O"
				else:
					optoken = "X"
				y = y+1
				while y<=7 and board[x][y] == optoken:
					myList += x,y
					y += 1
				if y>7:
					return ' '	
				if board[x][y] == token:
					return myList
	return ' '


'''**************************************************************************
** Function: check_NE
** Description: Checks Northeast of token to see if token position is valid
** Parameters: x, y, token, row, board
** Pre-conditions: Must have a board and potential token 
** Post-conditions: Checks if its a valid move 
*****************************************************************************'''
def check_NE(x, y, token, column, board):
	myList = []
	while board[x][y] == token:
		if x+1>7 or board[x+1][y-1] == ' ' or y-1<0:
			return ' '
		else:
			if board[x+1][y-1] == token:
				return ' '
			else:
				if token == "X":
					optoken = "O"
				else:
					optoken = "X"
				x = x+1
				y = y-1
				while x<=7 and y>=0 and board[x][y] == optoken:
					myList += x,y
					x += 1
					y -= 1
				if x>7 or y<0:
					return ' '
				if board[x][y] == token:
					return myList
	return ' '


'''**************************************************************************
** Function: check_NW
** Description: Checks Northwest of token to see if token position is valid
** Parameters: x, y, token, row, board
** Pre-conditions: Must have a board and potential token 
** Post-conditions: Checks if its a valid move 
*****************************************************************************'''
def check_NW(x, y, token, column, board):
	myList = []
	while board[x][y] == token:
		if y-1<0 or board[x-1][y-1] == ' ' or x-1<0:
			return ' '
		else:
			if board[x-1][y-1] == token:
				return ' '
			else:
				if token == "X":
					optoken = "O"
				else:
					optoken = "X"
				x = x-1
				y = y-1
				while x>=0 and y>=0 and board[x][y] == optoken:
					myList += x,y
					x -= 1
					y -=1
				if x<0 or y<0:
					return ' '
				if board[x][y] == token:
					return myList
	return ' '


'''**************************************************************************
** Function: check_SW
** Description: Checks Southwest of token to see if token position is valid
** Parameters: x, y, token, row, board
** Pre-conditions: Must have a board and potential token 
** Post-conditions: Checks if its a valid move 
*****************************************************************************'''
def check_SW(x, y, token, column, board):
	myList = []
	while board[x][y] == token:
		if x-1<0 or y+1>7 or board[x-1][y+1] == ' ':
			return ' '
		else:
			if board[x-1][y+1] == token:
				return ' '
			else:
				if token == "X":
					optoken = "O"
				else:
					optoken = "X"
				x = x-1
				y = y+1
				while x>=0 and y<=7 and board[x][y] == optoken:
					myList += x,y
					x -= 1
					y += 1
				if x<0 or y>7:
					return ' '	
				if board[x][y] == token:
					return myList
	return ' '


'''**************************************************************************
** Function: check_SE
** Description: Checks Southeast of token to see if token position is valid
** Parameters: x, y, token, row, board
** Pre-conditions: Must have a board and potential token 
** Post-conditions: Checks if its a valid move 
*****************************************************************************'''
def check_SE(x, y, token, column, board):
	myList = []
	while board[x][y] == token:
		if x+1>7 or y+1>7 or board[x+1][y+1] == ' ':
			return ' '
		else:
			if board[x+1][y+1] == token:
				return ' '
			else:
				if token == "X":
					optoken = "O"
				else:
					optoken = "X"
				x = x+1
				y = y+1
				while x<=7 and y<=7 and board[x][y] == optoken:
					myList += x,y
					x += 1
					y += 1
				if x>7 or y>7:
					return ' '	
				if board[x][y] == token:
					return myList
	return ' '


'''**************************************************************************
** Function: check_valid
** Description: Checks all around token to see if position is valid
** Parameters: x, y, token, row, board
** Pre-conditions: Must have a board and potential token 
** Post-conditions: Checks if its a valid move 
*****************************************************************************'''
def check_valid(x, y, token, column, board):
	validity = []
	myList = []
	res1 = check_left(x, y, token, column, board)
	validity.append(res1)
	res2 = check_right(x, y, token, column, board)
	validity.append(res2)
	res3 = check_up(x, y, token, column, board)
	validity.append(res3)
	res4 = check_down(x, y, token, column, board)
	validity.append(res4)
	res5 = check_NE(x, y, token, column, board)
	validity.append(res5)
	res6 = check_SE(x, y, token, column, board)
	validity.append(res6)
	res7 = check_SW(x, y, token, column, board)
	validity.append(res7)
	res8 = check_NW(x, y, token, column, board)
	validity.append(res8)
	for i in range (len(validity)):
		if validity[i] != ' ':
			x = validity[i]
			myList += x
	return myList


'''**************************************************************************
** Function: flip_token
** Description: Flips sandwiched opponent's token to your token 
** Parameters: validity, token, board
** Pre-conditions: Must have sandwiched opponent's token to flip
** Post-conditions: Flips "X"s to "O"s and vice versa 
*****************************************************************************'''
def flip_token(validity, token, board):
	if token == "X":
		for i in range ((len(validity)//2)):
			x = validity[i+i]
			y = validity[i+(1*i)+1]
			board[x][y] = "X"
		return board
	elif token == "O":
		for i in range ((len(validity)//2)):
			x = validity[i+i]
			y = validity[i+(1*i)+1]
			board[x][y] = "O"
		return board


'''**************************************************************************
** Function: check_valid_move
** Description: Checks if the potential position is empty or already taken 
** Parameters: token, column, board
** Pre-conditions: Must have board to check agaisnt
** Post-conditions: If potential position is already taken, returns false
*****************************************************************************'''
def check_valid_move(token, column, board):
	for x in range (8):
		for y in range (8):
			if board[x][y] == ' ':
				myList = check_valid(x, y, token, column, board)
				if (len(myList)) == 0:
					return True
	return False


'''**************************************************************************
** Function: calculate
** Description: Calculates the score of each player
** Parameters: board
** Pre-conditions: Must have board to calculate the values of
** Post-conditions: Returns the score of each player in a list 
*****************************************************************************'''
def calculate(board):
	myList = [0,0,0]
	for x in range (8):
		for y in range (8):
			if board[x][y] == "X":
				myList[0] += 1
			elif board[x][y] == "O":
				myList[1] += 1
			else:
				myList[2] += 1
	return myList

def main():
	scoreboard = [0,0]
	wantPlay = True
	while wantPlay == True:
		row = 8
		column = 8
		board = preboard(row,column)
		board[3][3] = "X"
		board[3][4] = "O"
		board[4][4] = "X"
		board[4][3] = "O"
		print_board(board)
		currentPlayer = "X"
		name = "player 1"
		win = False
		while win == False:
			print("This is "+name+" 's turn")
			gotMoves = check_valid_move(currentPlayer, column, board)
			if gotMoves == True:
				x = get_input("Column", row)
				y = get_input("Row", column)
				while board[x][y] != ' ':
					print("This spot is taken, try again.")
					x = get_input("Column", row)
					y = get_input("Row", column)
				board = place_token(board, currentPlayer, x, y)
				validity = check_valid(x, y, currentPlayer, column, board)
				while validity==[]:
					print("This move is invalid, try again.")
					board[x][y] = ' '
					print("This is "+name+"'s turn") 
					x = get_input("Column", row)
					y = get_input("Row", column)
					while board[x][y] != ' ':
						print("This spot is taken, try again.")
						x = get_input("Column", row)
						y = get_input("Row", column)
					board = place_token(board, currentPlayer, x, y)
					validity = check_valid(x, y, currentPlayer, row, board)
				board = flip_token(validity, currentPlayer, board)
				res = print_board(board)
				if currentPlayer == "X":
					currentPlayer = "O"
					name = "player 2"
				else:
					currentPlayer  = "X"
					name = "player 1" 
			else:
				print("No valid moves for "+name+". Turn is forfeited")
				if currentPlayer == "X":
					currentPlayer = "O"
					name = "player 2"
				else:
					currentPlayer = "X"
					name = "player 1" 
				gotMoves = check_valid_move(currentPlayer, column, board)
				if gotMoves == True:
					print("This is "+name+" 's turn")
					x = get_input("Column", row)
					y = get_input("Row", column)
					while board[x][y] != ' ':
						print("This spot is taken, try again.")
						x = get_input("Column", row)
						y = get_input("Row", column)
					board = place_token(board, currentPlayer, x, y)
					validity = check_valid(x, y, currentPlayer, column, board)
					while validity==[]:
						print("This move is invalid, try again.")
						board[x][y] = ' '
						print("This is "+name+"'s turn") 
						x = get_input("Column", row)
						y = get_input("Row", column)
						while board[x][y] != ' ':
							print("This spot is taken, try again.")
							x = get_input("Column", row)
							y = get_input("Row", column)
						board = place_token(board, currentPlayer, x, y)
						validity = check_valid(x, y, currentPlayer, row, board)
					board = flip_token(validity, currentPlayer, board)
					res = print_board(board)
					if currentPlayer == "X":
						currentPlayer = "O"
						name = "player 2"
					else:
						currentPlayer  = "X"
						name = "player 1" 
				else:
					print("There are no valid moves for both players. End of game.")
					win = True 
		myList = calculate(board)
		if int(myList[0])>int(myList[1]):
			print("Player 1 won the game.")
			scoreboard[0] += 1
		elif int(myList[1])>int(myList[0]):
			print("Player 2 won the game.")
			scoreboard[1] += 1
		else:
			print("This game is tied.")
		print(scoreboard)
		repeat = input("Do you want to play again?\n Y - Yes  N - No\n")
		if repeat == "Y":
			wantPlay = True
		elif repeat == "N":
			wantPlay = False

main()
