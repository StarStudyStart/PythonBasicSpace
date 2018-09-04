#-*- coding:utf-8 -*-
import requests
import re
import logging
import csv
logging.basicConfig(level=logging.INFO)

#获取网页
def getHtmlText(url,code='utf-8'):
	try:
		rq = requests.get(url,headers = {"user-agent":"Mozilla/5.0"},timeout=30)
		rq.raise_for_status()
		rq.encoding = code
		return rq.text
	except:
		return 'something error'
		
#获取单页影片信息
def get_one_page(url,tlst):
	pageText = getHtmlText(url)
	#print(pageText)
	film_names = re.findall(r'\}\">.+?</a>',pageText)
	#print(film_names)
	film_infos = re.findall(r'star\">\n.*?\n',pageText) #star\">\n.*?\n</p> 获取不到信息  这样才是正确的star\">\n.*?\n.*？</p>
	#print(film_infos)
	for i in range(len(film_names)):
		name = film_names[i][3:-4]
		info = film_infos[i][6:-1].strip() #正确的写法应该是这样 film_infos[i][7:-1].strip() 但是由于strip()方法 自动去掉了开头的\n 所以 6和7 实现的意义同等
		tlst.append([name,info])
	print(tlst)
#数据处理，存储在csv中
def data_handle(tlst):
	try:
		with open('./top100.csv','w+',newline='') as f:
			csvWriter = csv.writer(f)
			csvWriter.writerow(['电影名称','主演'])
			for star in tlst:
				csvWriter.writerow(star)
	except:
		return 'error'
			
#主函数 循环遍历前10页电影信息
def main():
	url = 'http://maoyan.com/board/4?offset=0'
	tlst = []
	get_one_page(url,tlst)
	data_handle(tlst)
main()
