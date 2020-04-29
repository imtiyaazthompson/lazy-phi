from math import floor

# a >= b
def ex_euc(a,b):
	r = [a,b]
	x = [1,0]
	y = [0,1]
	q = [None,None]

	i = 1
	while r[i] != 0:
		i += 1
		q.append(floor(r[i-2]/r[i-1]))
		r.append(r[i-2] - q[i]*r[i-1])
		x.append(x[i-2] - q[i]*x[i-1])
		y.append(y[i-2] - q[i]*y[i-1])

	d = r[i-1]
	xr = x[i-1]
	yr = y[i-1]

	print_table(q,r,x,y)
	return (d,xr,yr)


def print_table(q,r,x,y):
	size = len(r)
	print("i\tq[i]\tr[i]\tx[i]\ty[i]")
	print()
	for i in range(size):
		print("{}\t{}\t{}\t{}\t{}".format(i,q[i],r[i],x[i],y[i]))
		print()

def main():
	a = int(input("a: "))
	b = int(input("b: "))

	d,x,y = ex_euc(a,b)
	print("d: {}\nx: {}\ny: {}".format(d,x,y))

if __name__ == "__main__":
	main()
