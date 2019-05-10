#Kroblang Version 2

statements = {} #See statement class
variables = {}
allChars = [] #Contains every character in program
lastStrLiteral = "" #Used to set values

class KrobLang2Error(Exception):
	"Used for any errors raised by Kroblang 2."
	pass

class statement:
	"""
	Class for all statements. __call__() defines perimeters such as neighboring characters.
	It's best if all the functions used in statements are prefixed with stmt_
	"""
	
	def func(self):
		pass
	
	def __init__(self, symbol, func):
		self.symbol = symbol
		self.func = func
		
	def __call__(self, location=None):
		
		return self.func(location)
		
		
def register_statement(symbol, func):
	"Adds a statement object to the statements dict."
	statements[symbol] = statement(symbol, func)

#######################################Statement Functions#############################	
def stmt_str_start(loc):
	"starts a string literal. start and end string with $"
	retstr = "" 
	allChars.pop(loc)
	currentChar = allChars[loc]
	
	while currentChar != "$":
		retstr = retstr + currentChar
		allChars.pop(loc)
		currentChar = allChars[loc]
		
	lastStrLiteral = retstr
	return
	


###########################################################################################################
def setup_all_statements():
	"""
	This is the function where all of the statements are set up. Put all register_statement calls
	in here.
	"""
	register_statement("$", stmt_str_start)
	
def kroblang_exec(str):
	"Exactly waht you think, executes str"
	allChars = list(str)
	x = 0
	while x < len(allChars):
		try:
			statements[allChars[x]](location=x)
		except KeyError:
			raise KrobLang2Error("Unknown statement")	

def main():
	while True:
		s = input("OK~ ")
		kroblang_exec(s)
				
				
if __name__ == "__main__":
	main()
