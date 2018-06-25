#CalStatistics
#获取用户输入
def getNumbers():
	num = []
	iNumber = input("请输入数据（回车结束）")
	while iNumber != '':
		num.append(eval(iNumber))
		iNumber = input("请输入数据（回车结束）")
	return num
#遍历列表,取平均值
def mean(numbers):
	s = 0.0
	for num in numbers:
		s = s + num
	return s / len(numbers) 
#求得列表的数组
def dev(numbers,mean):
	sdev = 0.0
	for num in numbers:
		sdev += (num-mean)**2
	return pow( sdev/(len(numbers)-1),0.5)
#求得列表的中位数
def median(numbers, mean):
	sorted(numbers)
	size = len(numbers)
	if size % 2 == 0:
		med = (numbers[size/2]+numbers[size/2+1])/2
	else:
		med = numbers[size//2]
	return med
def main():
	n = getNumbers()
	m = mean(n)
	print("平均值：{},方差：{:.2f},中位数{:2f},".format(m,dev(n,m),median(n,m)))

main()







