# !/user/bin/
#wcTest.py
import jieba
import wordcloud
from scipy.misc import imread
mk = imread('fivestar.jpg')
txt = '落叶堆积了好几层\
而我踩过青春听见\
前世谁在泪语纷纷\
一次缘份结一次绳\
我今生还在等一世\
就只能有一次的认真\
确认过眼神 我遇上对的人\
我挥剑转身 而鲜血如红唇\
前朝记忆渡红尘 伤人的不是刀刃\
是你转世而来的魂\
确认过眼神 我遇上对的人\
我策马出征 马蹄声如泪奔\
青石板上的月光照进这山城\
我一路的跟 你轮回声 我对你用情极深\
洛阳城旁的老树根\
像回忆般延伸你问\
经过是谁的心跳声\
我拿醇酒一坛饮恨\
你那千年眼神是我\
醉醉坠入赤壁的 伤痕\
确认过眼神 我遇上对的人\
我挥剑转身 而鲜血如红唇\
前朝记忆渡红尘 伤人的不是刀刃\
是你转世而来的魂\
确认过眼神 我遇上对的人\
我策马出征 马蹄声如泪奔\
青石板上的月光照进这山城\
我一路的跟 你轮回声 我对你用情极深\
确认过眼神 我遇上对的人\
我策马出征 马蹄声如泪奔\
青石板上的月光照进这山城\
我一路的跟 你轮回声 我对你用情极深\
我一路的跟 你轮回声 我对你用情极深'
w = wordcloud.WordCloud(font_path='msyh.ttc',background_color='white',width = 1000,height = 600,mask = mk)
w.generate(' '.join(jieba.lcut(txt)))
w.to_file('wordcloud.jpg')
