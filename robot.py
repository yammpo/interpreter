import random
class Cell:
	def __init__(self, x, y, cell_type):
		self.x = x
		self.y = y
		self.type = cell_type

	def __repr__(self):
		return f'{self.x} {self.y} : {self.type}'
class Robot:
	def __init__(self, file, drons = 1000): #переделать с файлом
		self.life = True
		s = file.readline()
		b=[]
		self.x=int(s[0])
		self.y=int(s[2])
		c=file.read()
		b=c.split('\n')
		for i in range(len(b)):
			#b[i] = b[i].split(',')
			b[i] = list(b[i])
			for j in range(len(b[i])):
				if b[i][j] == '#':	b[i][j] = 1
				if b[i][j] == '.':	b[i][j] = 2
				if b[i][j] == '$':	b[i][j] = 3
				if b[i][j] == '?':	b[i][j] = 0
		print(b)
		self.map = b
		self.drons = drons
	
	def show_map(self):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				if i == self.x and j == self.y: #ROBOT
					print("R", end='')
				elif self.map[i][j] == 1: #WALL
					print("#", end='')	
				elif self.map[i][j] == 2: #EMPTY
					print(".", end='')
				elif self.map[i][j] == 3: #EXIT
					print("$", end='')
				else: #UNDEF
					print("?", end='')
			print()
			
	def up(self, n): #можно в функцию вынести
		for i in range(n):
			if self.life:
				self.x-=1
				if self.x<0 or self.x>=len(self.map):
					self.life=False
				elif self.map[self.x][self.y] == 1:
					self.life=False
		self.show_map()

	def down(self, n):
		for i in range(n):
			if self.life:
				self.x+=1
				if self.x<0 or self.x>=len(self.map):
					self.life=False
				elif self.map[self.x][self.y] == 1:
					self.life=False
		self.show_map()

	def left(self, n):
		for i in range(n):
			if self.life:
				self.y-=1
				if self.y<0 or self.y>=len(self.map[0]):
					self.life=False
				if self.map[self.x][self.y] == 1:
					self.life=False
		self.show_map()

	def right(self, n):
		for i in range(n):
			if self.life:
				self.y+=1
				if self.y<0 or self.y>=len(self.map[0]):
					self.life=False
				if self.map[self.x][self.y] == 1:
					self.life=False
		self.show_map()
		
	def send_drons(self, n):
		self.drons-=n
		new_map=[]
		array=[0]*121
		for i in range(n):
			a=Satellite(self.x, self.y, self.map)
			new_map.append(a.exploring())    
		for row in new_map:
			for cell in row:
				a=cell.x-self.x+5
				b=cell.y-self.y+5
				array[a*len(self.map[0])+b]=cell.type
		return array

class Satellite:
	def __init__(self, x, y, _map):
		self.life = True
		self.x = x
		self.y = y
		self.map = _map
		self.new_map = []

	def up(self):
		self.x-=1
		if (self.x<0 or self.x>=len(self.map)):
			self.life=False
			self.new_map.append(Cell(self.x,self.y,1))
		else:
			if self.map[self.x][self.y] == 1:
				self.life=False
			self.new_map.append(Cell(self.x,self.y,self.map[self.x][self.y]))

	def down(self):
		self.x+=1
		if (self.x<0 or self.x>=len(self.map)):
			self.life=False
			self.new_map.append(Cell(self.x,self.y,1))
		else:
			if self.map[self.x][self.y] == 1:
				self.life=False
			self.new_map.append(Cell(self.x,self.y,self.map[self.x][self.y]))

	def left(self):
		self.y-=1
		if (self.y<0 or self.y>=len(self.map)):
			self.life=False
			self.new_map.append(Cell(self.x,self.y,1))
		else:
			if self.map[self.x][self.y] == 1:
				self.life=False
			self.new_map.append(Cell(self.x,self.y,self.map[self.x][self.y]))

	def right(self):
		self.y+=1
		if (self.y<0 or self.y>=len(self.map)):
			self.life=False
			self.new_map.append(Cell(self.x,self.y,1))
		else:
			if self.map[self.x][self.y] == 1:
				self.life=False
			self.new_map.append(Cell(self.x,self.y,self.map[self.x][self.y]))

	def exploring(self):
		steps=random.randint(1,5)
		for i in range(steps):
			if self.life:
				step=random.randint(1,4)
				if step == 1:
					self.up()
				elif step == 2:
					self.up()
				elif step == 3:
					self.left()
				else:
					self.right()
			else:
				break
		return self.new_map	
			
