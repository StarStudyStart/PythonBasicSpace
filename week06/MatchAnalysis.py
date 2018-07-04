#-*- coding:utf-8 -*-
#MatchAnalysis.py
from random import random

def printIntro():
	print("这个程序模拟两个对手A和B之间的某种竞赛")
	print("程序运行需要A和B的能力值（0~1)之间")

def getInputs():
	a = eval(input("请输入选手A的能力值(0~1)之间):"))
	b = eval(input("请输入选手B的能力值(0~1)之间):"))
	n = eval(input("请输入模拟游戏次数："))
	return a,b,n

def gameOver(a,b):
	return a == 15 or b == 15

def simOneGame(proA,ProB):
	scoreA,scoreB = 0, 0
	serving = 'A'
	while not gameOver(scoreA,scoreB):
		if serving == 'A':
			if random() < proA:
				scoreA +=1
			else:
				serving = 'B'
		else :
			if random() < ProB:
				scoreB +=1
			else :
				serving = 'A'
	return scoreA,scoreB

def simNGames(n,proA,ProB):
	winsA,winsB = 0,0
	for i in range(n):
		scoreA, scoreB = simOneGame(proA,ProB)
		if scoreA > scoreB:
			winsA += 1
		else:
			winsB += 1
	return winsA,winsB


def printSummary(winsA,winsB):
	n = winsA + winsB
	print("竞技分析开始，共模拟{:}场比赛".format(n))
	print("选手A的胜场数为{},胜率为：{:0.1%}".format(winsA,winsA/n))
	print("选手B的胜场数为{},胜率为：{:0.1%}".format(winsB,winsB/n))

def main():
	printIntro()
	proA,ProB,n = getInputs()
	winsA,winsB = simNGames(n,proA,ProB)
	printSummary(winsA,winsB)

main()