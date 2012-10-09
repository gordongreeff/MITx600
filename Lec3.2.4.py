#simple script to figure of the cube root of a number
#first example of using guess and check alogorithms

x = int(raw_input ('Enter an integer: '))
ans = 0

while x > ans ** 3:
	ans = ans + 1

if ans**3 != x:
	print (str(x) + ' is not a perfect cube')
else:
	print ('The cube of ' + str(x) + ' is ' + str(ans))
