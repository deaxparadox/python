class Student:
	def __init__(self, name: str = None):
		self.__name = name 

	@property
	def name(self):
		return self.__name

	@name.setter 
	def name(self, value):
		self.__name = value 

	@name.deleter
	def name(self, value: str = None):
		del self.__name

def main():
	s = Student()
	s.name = 'nitish'
	del s.name
	s.name = "kushwaha"
	print(s.name)

if __name__ == "__main__":
	main()