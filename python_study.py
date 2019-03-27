from collections import Iterable
sum = 0
for x in range(101):
	sum += x
print(sum)

sum = 0

n = 99
while n > 0 :
	sum += n
	n = n -2
print(sum)

n = 1
while n <= 100:
	if n > 10:
		break
	print(n)
	n += 1
print('END')

n = 0
while n < 10:
	n += 1
	if n % 2 == 0:
		continue
	print(n)

print("=============")

d = {'a':1, 'b':2, 'c':3}
for key in d:
	print(key,"->", d[key])

for value in d.values():
	print(value)

for k, v in d.items():
	print(k, v)

list(range(1, 11))


