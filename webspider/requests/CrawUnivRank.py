#CrawUnivRank.py
#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4
import time

def getHTML(url):
	try:
		rq = requests.get(url,timeout=30)
		rq.raise_for_status()
		rq.encoding = rq.apparent_encoding
		return rq.text
	except:
		print("抓取失败！") 
		return " "

def fillUnivrList(html,ulist):
	soup = BeautifulSoup(html,"html.parser")
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds = tr("td")
			ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

def printUniverList(ulist,num):
	print("{:^10}\t{:^20}\t{:^10}\t{:^11}".format("排名","大学名称","省市","排名积分"))
	for n in range(num):
		time.sleep(0.1)
		print("{:^10}\t{:^20}\t{:^10}\t{:^11}".format(ulist[n][0],ulist[n][1],ulist[n][2],ulist[n][3]))

def main():
	unifo = []
	url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
	html = getHTML(url)
	fillUnivrList(html,unifo)
	printUniverList(unifo,601)
main()