userNumber = raw_input("Pick a number to factorize:")
userNumber = int(userNumber)
original = userNumber
factor = []
i = userNumber - 1 # star from the top and work to 0(zero)
while i > 1:
    if(userNumber % i) == 0:
        num = userNumber/i
        factor.append(num)
        userNumber = i
		
        i -=1
    else:
        i -= 1
		
if i == 1:
    factor.append(userNumber)
for i in factor:
    print i ,