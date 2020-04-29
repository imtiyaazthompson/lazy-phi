from math import sqrt,ceil
import extended_euclid as exgcd

def big_baby_step(a,b,mod):
	m = ceil(sqrt(mod))
	table = []
	for j in range(m):
		table.append((j,(a**j) % mod))

	d,x,y = exgcd.ex_euc(mod,a)
	alpha = (y**m) % mod
	gamma = [b]

	for i in range(m):
		for entry in table:
			if gamma[i] in entry:
				return i*m + entry[0]
		gamma.append((gamma[i]*alpha)%mod)

def main():
	b = int(input("Base: "))
	a = int(input("RHS: "))
	mod = int(input("Mod: "))
	log_x = big_baby_step(b,a,mod)
	print("Discrete Log: {}".format(log_x))

if __name__ == "__main__":
	main()
