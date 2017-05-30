import matplotlib.pyplot as pyplot

def generateCollatzPlot(n): 
	x_value = list(range(1,n))
	num_iterations = []

	for val in x_value:
		num_iterations.append(numToFinishCollatz(val))

	pyplot.plot(num_iterations)	
	pyplot.ylabel('some numbers')
	pyplot.show()

def numToFinishCollatz(n):
	# Only print out every 1000 numbers
	if (n % 1000 == 0):
		print("Starting collatz for number: " + str(n) )
	
	count = 0
	while n != 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3*n + 1
		count = count + 1
	return count


generateCollatzPlot(1000000)