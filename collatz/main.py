
def collatz(number):
    result = 0
    if number % 2 == 0:
        result = number // 2
        print(str(result))
        return result
    else:
        result = 3*number + 1
        print(str(result))
        return result

quit = False
result = 0
user_input = ""

while quit == False: 
    user_input = input("Type a number shorter than 11 digits for collatz sequence or 'quit' to quit the program: ")
    
    if user_input.isdigit() and len(user_input) <= 10:
        result = int(user_input)

        if result == 0:
            continue

        while result != 1:
            result = collatz(result)
        print(str(result))
    elif user_input == "quit":
        quit = True
    else:
        continue