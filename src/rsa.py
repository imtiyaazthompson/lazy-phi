import lazy_phi as lp
from extended_euclid import ex_euc as euc
from random import choice,seed
from sys import argv,exit

LIMIT = 25

def random_prime():
	print("Getting random prime")
	primes = [2]
	i = primes[0]
	c = 0

	while c < LIMIT:
		i = lp.get_next_prime(i)
		primes.append(i)
		c += 1
	
	# print(primes)
	return choice(primes)
		
# Generate a group of integers in modn
def gen_group_modn(n):
	print("Generating group of integers mod {}".format(n))
	i = 2
	group = [1]
	while i < n:
		group.append(i)
		i += 1

	return group

# For every element in integer mod n
# Check if a multiplicative inverse exist
# If it does add it to the group of units
def gen_unit_group(modn,group):
	print("Generating unit group, group of all elements in integer mod {} that have multiplicative inverses".format(modn))
	gunit = []
	for element in group:
		if element in gunit:
			continue
		element %= modn
		for i in range(1,modn):
			# element in integers modulo n *
			# has a multiplicative inverse
			# therefore belongs to group of units
			if ((element*i) % modn) == 1:
				if element not in gunit:
					gunit.append(element)
				if i not in gunit:
					gunit.append(i)

	return gunit
				

# To find the inverse of an element of a group
# more effecient way is Extended Eclidean algorithm
# To find x,y in integers mod n for gcd(a,b) = 1
def rsa_init(p,q,e=None,d=None):
	print("Setting up RSA")
	n = p*q
	group = gen_group_modn(n)
	gunit = sorted(gen_unit_group(n,group))
	print("LENGTH Zn: {}".format(len(gunit)))
	phi = lp.extended_phi(n)
	print("PHI(n={}): {}".format(n,phi))

	# encryption/decryption key
	if e == None and d != None:
		# Calculate encryption exponent
		if lp.gcd(d,phi) == 1:
			print("Decryption exp {} is suitable".format(d))
			print("Since gcd(d,phi) = 1, that is, d is invertible, has an inverse element in Zn")
			print("Extended Euclidean Algorithm")
			a,x,y = euc(phi,d)
			e = y
			print("ENCRYPTION EXPONENT: {}".format(e))

		else:
			print("Decryption exp {} is NOT suitable".format(d))

	elif d == None and e != None:
		# Calculate decryption exponent
		if lp.gcd(e,phi) == 1:
			print("Encryption exp {} is suitable".format(e))
			print("Since gcd(e,phi) = 1, that is, e is invertible, has an inverse element in Zn")
			print("Extended Euclidean Algorithm")
			a,x,y = euc(phi,e)
			d = y
			print("DECRYPTION EXPONENT: {}".format(d))
		else:
			print("Encryption exp {} is NOT suitable".format(e))
	else:
		# Find a suitable d and e
		print("Choosing random encryption exp from group of units, e <= phi")
		e = choice(gunit)
		while e == 1 or e > phi:
			e = choice(gunit)
		print("ENCRYPTION EXPONENT: {}".format(e))
		# EEA
		print("Extended Euclidean Algorithm")
		a,x,y = euc(phi,e)
		d = y
		print("DECRYPTION EXPONENT: {}".format(d))
		

	# If decryption exponent drops below zero
	# We cannot use negative numbers as cryption exp
	if d < 0:
		d += phi
	public_key = (e,n)
	# by = 1, therefore b = 1/y, therefore b^-1 = y
	private_key = (d,p,q)
		
	
	print("PUBLIC KEY: {}".format(public_key))
	print("PRIVATE KEY: {}".format(private_key))

	print((e,d,n))
	return (e,d,n)

def encrypt(msg,e,n):
	print("msg: {}".format(msg))
	print("e: {}".format(e))
	print("n: {}".format(n))
	return (msg**e) % n

def decrypt(msg,d,n):
	print("msg: {}".format(msg))
	print("d: {}".format(d))
	print("n: {}".format(n))
	return msg**d % n
		
def rsa_setup():
	key_flags = ["-e","-d","-n"]
	state_flags = ["init","preconf"]
	
	cnx = 0
	n = 0
	if argv[1] not in key_flags:
		print("Usage: python3 rsa.py [-d (d)|-e (e)|-n] [init|preconf (p) (q)]")
	elif argv[1] == "-e":
		e = int(argv[2])
		d = None
		cnx = 3
	elif argv[1] == "-d":
		d = int(argv[2])
		e = None
		cnx = 3
	elif argv[1] == "-n":
		e = None
		d = None
		cnx = 2

	if argv[cnx] == "init":
		p = random_prime()
		q = random_prime()
		e,d,n = rsa_init(p,q,e,d)
	elif argv[cnx] == "preconf":
		p = int(argv[cnx+1])
		q = int(argv[cnx+2])
		e,d,n = rsa_init(p,q,e,d)

	c = input("ENC/DEC: ")

	if c == "ENC":
		msg = int(input("message: "))
		print("{} ENCRYPTED AS: {}".format(msg,encrypt(msg,e,n)))
	elif c == "DEC":
		msg = int(input("ciphertext: "))
		print("{} DECRYPTED AS: {}".format(msg,decrypt(msg,d,n)))
	else:
		print("Completato!")

def main():
	rsa_setup()

if __name__ == "__main__":
	main()
