number = int(input('How many numbersin the Fibonacci sequence would you like to print? '))
if number < 2:
    number = int(input("Really? Dude, I'm a computer. Give me a number bigger than 1: ")) # Everyone was shocked that Sabrina made her programs snarky AF
a = b = 1
c = 0
fib_list = [a, b] # Creates list of actual sequence
dif_list = [c, c] # Creates the list of differences. Needs to have 0 listed twice before it starts subtracting; otherwise it doesn't add up right.
while True:
    if len(fib_list) < number: # Check to see if it's calculated the right number yet
        a, b = a + b, a
        c = a - b
        fib_list.append(a)
        dif_list.append(c)
    else:
        break
for i, item in enumerate(fib_list, 1):
    print (i, item)
for dif in dif_list:
    print(dif)

        
        
    
