class shape:
	def_init_(self, l=1, h=1):
		self.l=1
		self.h=h

	def define(self):
		print('Length of this shape is: ',self.l, 'and height is: ', self.h)

	def setvalues(self, h, l):
		self.h=h
		self.l=l