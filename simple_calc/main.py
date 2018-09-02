import re

print("Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous ==0:
        equation = input('Enter equation: ')
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-z,.:()""]','',equation) #removes the given regex characters from string
        #the eval function can execute scripts from input otherwise

        if previous == 0:
            previous = eval(equation) #creates result from given equation in string format (crashes if it's not correct format)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()