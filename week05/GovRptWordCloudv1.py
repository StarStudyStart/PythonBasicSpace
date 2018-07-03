#！/user/bin/env 
#-*- coding:utf-8 -*-
#GovRptWordCloudv1.py
import jieba
import wordcloud
from scipy.misc import imread
mk = imread('fivestar.jpg')
fo = open('年轮.txt','r',encoding='utf-8')
f = fo.read()
fo.close()
ls = jieba.lcut(f)
txt = ' '.join(ls)
wc = wordcloud.WordCloud(font_path='msyh.ttc',\
 	width = 1000,height = 600,background_color='white',\
 	mask = mk)
wc.generate(txt)
wc.to_file('nianlun.png')
