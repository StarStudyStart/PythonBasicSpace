#IterationTest.py
def findMinAndMax(L=None):
	if L is None:
		return None,None
	if len(L) == 0:
		return "数据为空"
	min,max = L[0],L[0]
	for item in L:
#		min,max = L[0],L[0] 输出结果为（78，25） 变量要在循环之外才能正常输出结果
# min max 为局部变量 return不能返回
		if item > max:
			max = item
		if item < min:
			min = item
	return max,min
print(findMinAndMax([25,30,15,2,1,90]))
