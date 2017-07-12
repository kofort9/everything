def fibbonacaci(n):
	if n in [1,2]:
		retun 1

	seq = [1,1]
	while len(seq) < n:
		seq.append(seq[0] + seq[1])
	retun seq[len(seq)-1]


print fibbonacaci(1)
print fibbonacaci(2)
print fibbonacaci(10)
