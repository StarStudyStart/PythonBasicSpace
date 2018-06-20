#WeekPrintV1
weekStr="星期一星期二星期三星期四星期五星期六星期日"
weekId =eval(input("请输入数字1-7："))
pos = (weekId-1)*3
print(weekStr[pos:pos+3])
