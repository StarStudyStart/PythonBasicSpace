#！/usr/bin/
#-*- coding:utf-8 -*-
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return "Student object (name:%s) " % self.name
	__repr__ = __str__

print(Student("YabinLi"))

# __iter__&&__next__()
class Fib():
	def __init__(self):
		self.a,self.b = 0,1

	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b = self.b,self.a+self.b
		# self.a +=1
		if self.a > 100:
			raise StopIteration()
		return self.a

	def  __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a+b
		return a
		
for n in Fib():
	print(n)

print(Fib()[6])


#__getattr__()
class Chain():
	def __init__(self,path=''):
		self.path = path
	def __getattr__(self,path):
		return Chain("%s/%s" % (self.path,path))

	def __str__(self):
		return self.path
	__repr__ = __str__

print(Chain().status.time.list)
