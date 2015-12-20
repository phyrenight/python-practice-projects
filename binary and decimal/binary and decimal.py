# converts a binary number to a decimal number 
# and a decimal number to a binary number

def binary_convert():
    decimal = 0
    sum = 0
    number = raw_input("Your binary number: ")
    convert = []
    length = len(number)
    dueces = 1 # temp name
    counter = length -1
    while counter > 0:
        if(number[counter] == '1'):
            sum += dueces
        counter -= 1
        dueces = dueces * 2
    print "Decimal value of %s is %s "% (number, sum)

def decimal_convert():
    number = raw_input("Enter a decimal number: ")
    number = int(number)
    divisor = 2
    list = []
    #used to find the largest number
    while True:# need to fix divisor is to low 
        if (number / divisor) < divisor:
            number = number - divisor
            divisor /= 2
            list.append(1)
            break
        elif(number > 0):
            divisor = divisor * 2
        else:
            print "number is zero"

    while number > 0:
	print number , divisor
        if ( number % divisor) == 0:# need to fix tries to divide by zero
            list.append(1)
            number = number - divisor
            divisor = divisor / 2
        elif(number == 1):
            list.append(1)
			break
        else: 
            list.append(0)
            divisor = divisor / 2
    for i in list:
        print i,

print "Would you like to convert a (b)inary or (d)ecimal number?"
choice = raw_input("> ")

if (choice == 'b'):
    binary_convert()
elif(choice == 'd'):
    decimal_convert()
else:
    print "Invalid choice"
    print "Your choice must be either 'd' for decimal or 'b' for binary"
	

	