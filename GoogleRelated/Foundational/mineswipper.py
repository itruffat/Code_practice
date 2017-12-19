#https://techdevguide.withgoogle.com/paths/foundational/sequence-2/coding-question-minesweeper/#code-challenge

from random import randrange

class mineswipper:
	def __init__(self):
		self.table = []
		self.nonDefined = []
		self.x = 0
		self.y = 0
	
	def definetablesize(self,_x,_y):
		self.x = _x
		self.y = _y
		for y_val in range(0,_y):
			self.table.append([0 for _ in range(0,_x)])
			for x_val in range(0,_x):
				self.nonDefined.append(tuple((y_val, x_val)))

	def setBomb(self, _x, _y):
		self.table[_y][_x] =  9
		for t_y in range(max(0,_y-1),min(self.y, _y + 1 + 1)):
			for t_x in range(max(0,_x-1),min(self.x, _x + 1 + 1)):
				self.table[t_y][t_x] = min(self.table[t_y][t_x] +1, 9)

	def pickRandomBomb(self):
		index = randrange(0,len(self.nonDefined))
		val_y, val_x = self.nonDefined.pop(index)
		self.setBomb(val_x, val_y)

	def __str__(self):
		i = ""
		for t in self.table:
			i+= " ".join(list(map(lambda x: str(x),t)))
			i+= "\n"
		return i



mine = mineswipper()

mine.definetablesize(10,8)

mine.pickRandomBomb()
mine.pickRandomBomb()
mine.pickRandomBomb()
mine.pickRandomBomb()
mine.pickRandomBomb()
mine.pickRandomBomb()
mine.pickRandomBomb()

print mine