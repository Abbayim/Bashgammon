class Board:
	def __init__(self):
		self.myBoard = {}
		for i in range(24):
			self.myBoard[i] = 0
		self.myBoard[0] = 2
		self.myBoard[5] = -5
		self.myBoard[7] = -3
		self.myBoard[11] = 5
		self.myBoard[12] = -5
		self.myBoard[16] = 3
		self.myBoard[18] = 5
		self.myBoard[23] = -2
		self.maxRows = 5
		self.xFree = 0
		self.oFree = 0
		self.xJail = 0
		self.oJail = 0
		self.xHome = 5
		self.oHome = 5
	
	def makeMove(self, space, side, steps):
		"""
		@param
		space = starting space
		side = true if X (steps are decreasing), false if O (steps are increasing)
		steps = number of steps
		*** if you are trying to free a piece from jail, steps = 0
		@return
		tuple of true if move was made, false if not possible, and string with response
		"""
		if side:
			if (self.xJail > 0 and (steps != 0 or space < 18)):
				return (False, "Make sure you free your piece from jail first!")
			elif (self.xJail > 0 and steps == 0 and space > 17):
				if (self.myBoard[space] > 1):
					return (False, "Space is occupied")
				elif (self.myBoard[space] == 1):
					self.xJail = self.xJail - 1
					self.myBoard[space] = -1	
					self.oJail = self.oJail + 1
					self.oHome = self.oHome - 1
					return (True, "Piece released from jail and sent one to jail!")
				else:
					self.xJail = self.xJail - 1
					self.myBoard[space] = self.myBoard[space] - 1
					return (True, "Piece released from jail!")
			elif (self.myBoard[space] >= 0):
				return (False, "Space is either empty or wrong team")
			else:
				newSpace = space - steps
				if (newSpace < 0):
					if (self.xHome < 15):
						return (False, "Make sure all of your pieces are in home before clearing them!")
					else:
						self.myBoard[space] = self.myBoard[space] - 1
						self.xFree = self.xFree + 1
						return (True, "Piece cleared!")
				elif (self.myBoard[newSpace] > 1):
					return (False, "New space is occupied")
				elif (self.myBoard[newSpace] == 1):
					self.myBoard[space] = self.myBoard[space] + 1
					self.myBoard[newSpace] = -1
					self.oJail = self.oJail + 1
					if (newSpace >= 18):
						self.oHome = self.oHome - 1
					return (True, "Sent one to jail!")
				else:
					self.myBoard[space] = self.myBoard[space] + 1
					self.myBoard[newSpace] = self.myBoard[newSpace] - 1
					if (newSpace < 6):
						self.xHome = self.xHome + 1
					if (newSpace < 11):
						self.updateRows(True)
					else:
						self.updateRows(False)
					return (True, "Move made")
		else:
			if (self.oJail > 0 and (steps != 0 or space > 5)):
				return (False, "Make sure you free your piece from jail first!")
			elif (self.oJail > 0 and steps == 0 and space < 6):
				if (self.myBoard[space] < -1):
					return (False, "Space is occupied")
				elif (self.myBoard[space] == -1):
					self.oJail = self.oJail - 1
					self.myBoard[space] = 1
					self.xJail = self.xJail + 1
					self.xHome = self.xHome - 1
					return (True, "Piece released from jail and one sent to jail!")
				else:
					self.oJail = self.oJail - 1
					self.myBoard[space] = self.myBoard[space] + 1
					return (True, "Piece released from jail!")
			elif (self.myBoard[space] <= 0):
				return (False, "Space is either empty or wrong team")
			else:
				newSpace = space + steps
				if (newSpace > 23):
					if (self.oHome < 15):
						return (False, "Make sure all of your pieces are in home before clearing them!")
					else:
						self.myBoard[space] = self.myBoard[space] - 1
						self.oFree = self.oFree + 1
						return (True, "Piece cleared!")
				elif (self.myBoard[newSpace] < -1):
					return (False, "New space is occupied")
				elif (self.myBoard[newSpace] == -1):
					self.myBoard[space] = self.myBoard[space] - 1
					self.myBoard[newSpace] = 1
					self.xJail = self.xJail + 1
					if (newSpace < 6):
						self.xHome = self.xHome - 1
					return (True, "Sent one to jail!")
				else:
					self.myBoard[space] = self.myBoard[space] - 1
					self.myBoard[newSpace] = self.myBoard[newSpace] + 1
					if (newSpace > 17):
						self.oHome = self.oHome + 1
					if (newSpace < 11):
						self.updateRows(True)
					else:
						self.updateRows(False)
					return (True, "Move made")
				
	def updateRows(self, top):
		changed = False
		if top:
			for i in range(12):
				if (self.myBoard[i] > 5):
					self.maxRows = self.myBoard[i]
					changed = True
		else:
			for i in range(23,11,-1):
				if (self.myBoard[i] > 5):
					self.maxRows = self.myBoard[i]
					changed = True
		if not changed:
			self.maxRows = 5


	def __repr__(self):
		"""
		1 -> 1
		2 -> 5
		3 -> 9
		4 -> 13
		5 -> 17
		6 -> 21
		7 -> 28
		8 -> 32
		9 -> 36
		10 -> 40
		11 -> 44
		12 -> 48
		13 -> 1
		17 -> 17
		19 -> 28
		24 -> 48
		"""

		emptyline = "|                       | |                       |"
		if (self.oJail > 0):
			boardstring = "					O Jail: " + str(self.oJail) + "\n"
			boardstring += "				X HOME BOARD 	Freed:" + str(self.xFree) + "\n"
		else:
			boardstring = "				X HOME BOARD 	Freed:" + str(self.xFree) + "\n"
		boardstring += " -------------------------------------------------\n"
		boardstring += "|12  11  10  9   8   7  | | 6   5   4   3   2   1 |\n"
		for i in range(self.maxRows):
			boardstring += self.populateTop(i)
		boardstring += " ------------------------------------------------- \n"
		for i in range(self.maxRows-1,-1,-1):
			boardstring += self.populateBottom(i)
		boardstring += "|13  14  15  16  17  18 | | 19  20  21  22  23  24|\n"
		boardstring += " -------------------------------------------------\n"
		boardstring += "				O HOME BOARD 	Freed: " + str(self.oFree) + "\n"
		if (self.xJail > 0):
			boardstring += "					X Jail: " + str(self.xJail) + "\n"
		return boardstring
		

	def populateTop(self, lineNumber):
		"""
		1 -> 1
		2 -> 5
		3 -> 9
		4 -> 13
		5 -> 17
		6 -> 21
		7 -> 28
		8 -> 32
		9 -> 36
		10 -> 40
		11 -> 44
		12 -> 48
		"""
		line = "|                       | |                       |\n"
		boardtostring = {} 
		boardtostring[0] = 48
		boardtostring[1] = 44
		boardtostring[2] = 40
		boardtostring[3] = 36
		boardtostring[4] = 32
		boardtostring[5] = 28
		boardtostring[6] = 21
		boardtostring[7] = 17
		boardtostring[8] = 13
		boardtostring[9] = 9
		boardtostring[10] = 5
		boardtostring[11] = 1
		for i in range(12):
			if (self.myBoard[i] > lineNumber):
				line = line[:boardtostring[i]] + 'O' + line[boardtostring[i]+1:]
			elif (abs(self.myBoard[i]) > lineNumber and self.myBoard[i] < 0):
				line = line[:boardtostring[i]] + 'X' + line[boardtostring[i]+1:]
		return line

	def populateBottom(self, lineNumber):
		line = "|                       | |                       |\n"
		boardtostring = {}
		boardtostring[11] = 48
		boardtostring[10] = 44
		boardtostring[9] = 40
		boardtostring[8] = 36
		boardtostring[7] = 32
		boardtostring[6] = 28
		boardtostring[5] = 21
		boardtostring[4] = 17
		boardtostring[3] = 13
		boardtostring[2] = 9
		boardtostring[1] = 5
		boardtostring[0] = 1
		for i in range(12):
			if (self.myBoard[12+i] > lineNumber):
				line = line[:boardtostring[i]] + 'O' + line[boardtostring[i]+1:]
			elif (abs(self.myBoard[12+i]) > lineNumber and self.myBoard[12+i] < 0):
				line = line[:boardtostring[i]] + 'X' + line[boardtostring[i]+1:]
		return line


