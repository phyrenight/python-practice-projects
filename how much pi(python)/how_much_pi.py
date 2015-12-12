my_pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164"
print "How many decimal places in pi do you want displayed( upto 70 places)?"
length = raw_input()
i = int(length) + 2 # add 2 to print the 3. and  extra 1 to get the last decimal place the user wanted
print my_pi[:i]
