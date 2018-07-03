#！/usr/bin/
# -*- coding:utf-8 -*-
class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		self._width = value
	@property
	def heigth(self):
		return self._heigth
	@heigth.setter
	def heigth(self,value):
		self._heigth = value
	@property
	def resolution(self):
		return self._width*self._heigth
screen = Screen()
screen.width = 1024
screen.heigth = 768
#screen.resolution = 500
print(screen.resolution,end=" ")

