#TrimTest 使用递归函数自定义trim，实现strip同样的效果
def trim(s):
	if s[0]== ' ':
		s = s[1:]
	if s[-1] == ' ':
		s = s[:-1]
	if s[0] != ' ' and s[-1]!=' ':
		return s 
	return trim(s) 
input_str = input("请输入测试字符串：")
print(trim(input_str))

