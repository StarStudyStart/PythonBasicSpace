#AutoTraceDraw
import turtle as t
t.title("自动绘制轨迹")
t.setup(800,600,0,0)
t.pencolor('red')
t.seth(36)
t.pensize(5)
#读取文件数据
datals = []
datatxt = open('data.txt','rt')
for line in datatxt:
	line = line.replace('\n',' ')
	datals.append(list(map(eval,line.split(","))))
datatxt.close()
# 轨迹绘制
for i in range(len(datals)):
	t.fd(datals[i][0])
	t.pencolor(datals[i][3],datals[i][4],datals[i][5])
	if datals[i][1]:
		t.right(datals[i][2])
	else:
		t.left(datals[i][2])
t.done()


