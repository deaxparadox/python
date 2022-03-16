def execute(func):
	def wrapper(*args, **kwargs):
		return func(*args, **kwargs)
	return wrapper 

@execute
def func():
	return "nitish"

def main():
	func()

if __name__ == "__main__":
	main()