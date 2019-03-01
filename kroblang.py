#anything unrecognized is simply ignored
import random

lastNum = 0

def isNum(inp):
	try:
		return [True, int(inp)]
	except:
		return [False, 0]
		
commChars = ["*", #define function, named by the next character (definition includes whole input)
"&", #print the last character in stack to screen
"#", #Double the last value on the stack and add to stack
"@", #adds the last number from the stack to the next number, moves to stack
"?", #generates a random number an adds it to the stack
":", #calls the function named by the next character
";", #does nothing
"+", #adds the next character to the top of the stack
"/", #Halves the value on yhe stack and saves it to the stack
"~", #Squares the last value on the stack and saves it to stack
]

var = "b" #the "stack"
functions = {
	"b": "?&+h&+e&+l&+l&+o&"
}
		
fromfile = False
def execute():
	global var, functions, fromfile
	x = 0
	while x == 0:
		tempnum = 0
		script = input("$>")
		script = list(script)
		while tempnum < len(script):
			try:
				current = script[tempnum]
				nextChar = script[tempnum + 1]
			except:
				nextChar = "0"
			if isNum(nextChar)[0]:
				nextChar = int(nextChar)
			if current == ";":
				fromfile = True
			else:
				if current == "*":
					script.remove("*")
					functions[nextChar] = "".join(script)
					script = list("krob")
				elif current == "&":
					print(str(var))
				elif current == "#":
					var = var * 2
				elif current == "@":
					var = var + nextChar
				elif current == "?":
					var = random.randint(0, 99999)
				elif current == ":":
					script = list(functions[nextChar])
					tempnum = 0
				elif current == "+":
					var = nextChar
				elif current == "/":
					var = var / 2
				elif current == "~":
					var = var * var
				else:
					pass
					
				tempnum = tempnum + 1
					
					  
if __name__ == "__main__":
	execute()
		
