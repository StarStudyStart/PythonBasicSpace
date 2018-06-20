#BMITest.py
height = float(input("请输入你的身高/m："))
weight = float(input("请输入你的体重/kg："))
PSI = "您的身体处于"
bmi = weight/pow(height,2)
if bmi >= 32 :
    print(PSI+"过于肥胖状态")
elif bmi >= 28 :
    print(PSI+"肥胖状态")
elif bmi >= 25:
    print(PSI+"过重状态")
elif bmi >= 18.5:
    print(PSI+"正常状态")
else:
    print(PSI+"过轻状态")
    pass

