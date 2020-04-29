from sys import argv

def is_prime(n):
	i = 2
	while i <= n/2:
		if n == 1:
			return False
		elif n % i == 0:
			return False
	
		i += 1

	return True

def get_next_prime(n):
	current = n
	while True:
		current += 1
		if is_prime(current):
			return(current)

	return -1

def gcd(a,b):
	while (b != 0):
		t = b
		b = a % b
		a = t
	return a

# Find the number of numbers relatively prime to n
# Euler's totient function
def simple_phi(n):
	count = 0
	for i in range(n):
		if gcd(i,n) == 1:
			count += 1

	return count

def extended_phi(n):
	# Get product of primes
	pprod = prime_ladder(n)
	
	keys = pprod.keys()
	# Show next step
	print("phi({})".format(n))
	print("\t= ",end='')
	for key in keys:
		if pprod[key] != 1:
			print("phi({}^{})".format(key,pprod[key]),end='')
		else:
			print("phi({})".format(key),end='')
	
	print()
	print("\t= ",end='')
	for key in keys:
		if pprod[key] != 1:
			if pprod[key] - 1 != 1:
				print("({}^{})({} - 1)".format(key,pprod[key]-1,key),end='')
			else:
				print("({})({} - 1)".format(key,key),end='')
		else:
			print("({} - 1)".format(key),end='')

	print()
	answer = simple_phi(n)
	print("\t= {}".format(answer))
		 
	

def prime_ladder(n):
	stores = {}
	i = 2
	current = n
	while current != 1:
		mod = current % i
		if mod != 0:
			i = get_next_prime(i)
		else:
			current /= i
			if i in stores:
				stores[i] += 1
			else:
				stores[i] = 1

	return stores
	#print_ladder(stores)

def print_ladder(ladder):
	for key in ladder.keys():
		print("{:^5d}|{:^5d}".format(key,ladder[key]))
		print("-"*11)

def main():
	if argv[1] == "gcd":
		a = int(input("a: "))
		b = int(input("b: "))
		d = gcd(a,b)
		print("GCD({},{}) = {}".format(a,b,d))
	elif argv[1] == "sphi":
		n = int(input("n: "))
		print("phi({}) = {}".format(n,simple_phi(n)))
	elif argv[1] == "ladder":
		n = int(input("n: "))
		prime_ladder(n)
	elif argv[1] == "exphi":
		n = int(input("n: "))
		extended_phi(n)

if __name__ == "__main__":
	main()	
