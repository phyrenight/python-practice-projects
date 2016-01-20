strng = raw_input("enter a string: ")
if strng > 0:
    lst = strng.split(' ')
    print "There are {} words in the string.".format(len(lst))
else:
    print "No string entered!"