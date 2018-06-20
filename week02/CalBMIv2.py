#CalBMIv2.py
height,weight = eval(input("请输入您的身高(米)和体重(千克)[逗号隔开]："))
bmi = weight/height**2
print('您的BMI数值为:{:.2f}'.format(bmi))
native,national  = " "," "
if bmi < 18.5:
    native,national = "偏瘦","偏瘦"
elif 18.5 <= bmi < 24:
    native,national = "正常","正常"
elif  24 <= bmi < 25:
    native,national = "偏胖","正常"
elif  25 <= bmi < 28:
    native,national = "偏胖","偏胖"
elif  28 <= bmi < 30:
    native,national = "肥胖","偏胖"
else 30 <= bmi :
    native,national = "肥胖","肥胖"
print("BMI指标,国际：{0}，国内：{1}".format(national,native))
