# file handling

# 1) without using with statement
file = open('foo.txt', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('foo.txt', 'w')
try:
	file.write('hello world')
finally:
	file.close()
