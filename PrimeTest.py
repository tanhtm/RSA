import math
import MyMath

def isPrime(a):
	if a == 2 :
		return True
	b = int(math.sqrt(a))
	for i in range(2,b+1):
		if a % i == 0:
			return False
	return True

fi  = open("SmallPrime.txt","r")
sprime = fi.readlines()
fi.close()

def Preprocessor(a):
	for i in sprime:
		if a % int(i) == 0:
			return False
	return True

# Fermat's little theorem
def Fermat(p,x):
	for i in range(x): #check x base
		a = int(sprime[i])
		if MyMath.powMod(a,p-1,p) != 1:
			return False
	return True

# Miller–Rabin primality test
def Q(a, p, m, s):
	x = MyMath.powMod(a,m,p)
	if x == 1:
		return True
	for i in range(0,s+1):
		if x == p - 1:
			return True
		x *= x
		x %= p
	return False

def Miller_Rabin(p, x):
	# x : the number of bases
	# p - 1 = m*2^s (m is odd)
	n = p - 1
	s = 0
	while n & 1 == 0:
		n = n >> 1
		s+= 1
	m = n
	for i in range(x):
		a = int(sprime[i])
		if Q(a,p,m,s) == False:
			return False
	return True
