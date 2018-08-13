#-*- coding：utf-8 -*-
from  urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
# 清理乱码数据
def cleanInput(input):
	input = re.sub('\n',' ',input)
	input = re.sub('\[[0-9]*\]',"",input)
	input = re.sub(' +'," ",input)
	input = bytes(input,'UTF-8')  #以UTF-8转化成字节类型
	input = input.decode('ascii','ignore') #重新编码
	cleanInput = []
	input = input.split(' ')
	for item in input:
		item = item.strip(string.punctuation) # 清理标点符号  string.punctuation 返回常用字符标点
		if len(item) > 1 or item =='a' or item =='i':
			cleanInput.append(item)
	return cleanInput
#以指定 n-grams 模型输出			
def ngrams(input,n):
#	input =input.split(' ')
	input = cleanInput(input) # 字符清理后输出结果反而变大了，因为字符中的'\n' 代提成了空格 所以字符多了
	output = []
	for i in range(len(input)-n+1): # 字符串的最后n个字符为 [l-n,l] 所以i的最大值为 l-n 即range的范围最大值为l-n+1   例 range(3) 的最大值为 2
		output.append(input[i:i+n])
	return output
		
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html,'html.parser')
content = bsObj.find('div',{'id':'mw-content-text'}).get_text()
ngrams = ngrams(content,2)
print(ngrams)
print('2-ngrams is {:}'.format(len(ngrams)))

