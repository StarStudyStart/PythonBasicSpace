#OOPTest
class Student(object): 
	count = 0
	def __init__(self,name):
		self.name = name
		Student.count += 1

def main():
	stu = Student('Yabin')
	print(Student.count)
	stu2 = Student('Taocai')
	print(Student.count)
	stu3 = Student('Taocai')
	print(Student.count)
main()
