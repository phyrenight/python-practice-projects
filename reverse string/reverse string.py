strng = raw_input(' enter a string: ')
lst = strng.split(' ')
lst2 = []

for i in lst:
    word = ''
    counter = len(i) - 1
    while True:
        if counter == -1:
            lst2.append(word)
            break
        else:
            word += i[counter]
            counter -= 1
newString = ' '.join(lst2)
print newString