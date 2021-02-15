start=1
end =50
sum=0
for n in range(start, end + 1):
	if n % 2 != 0:
		print(n, end = " ")
		sum=sum+n
print("\nsum:",sum)