index = 6

count = 0
def fibo(n:int,b,bb):
	global count
	count +=1
	if index <= 1:
		return 1

	if n == index - 1:
		return b+bb

	return fibo(n+1,b+bb,b)
print(fibo(1,1,0))
print(count)