import random 
import math

def Random (bit):
	a = random.getrandbits(bit)
	a = a | 1 << (bit-1)
	a = a | 1 
	#print(bin(a)) 
	return a;

def isPrime(a):
	if a == 2 :
		return True
	b = int(math.sqrt(a))
	for i in range(2,b+1):
		if a % i == 0:
			return False
	return True

def powMod(a, b, m):
	x = []
	while b != 0:
		x.append(b & 1)
		b = b >> 1
	#print(x)
	sz = len(x)
	po = [a%m]
	for i in range(1,sz):
		p = (po[i-1]*po[i-1])%m
		po.append(p)
	r = 1
	for i in range(sz):
		if(x[i] != 0):
			r*= po[i]
			r%= m
	return r

fi  = open("smallprime.txt","r")
sprime = fi.readlines()
fi.close()

def pre(a):
	for i in sprime:
		if a % int(i) == 0:
			return False
	return True

def Fermat(p,x):
	for i in range(x): #check x base
		a = int(sprime[i])
		if powMod(a,p-1,p) != 1:
			return False
		# if pow(a,p-1,p) != 1:
		# 	return False
	return True

def Q(a, p, m, s):
	# p - 1 = m*2^s (m is odd)
	x = powMod(a,m,p)
	if x == 1:
		return True
	for i in range(0,s+1):
		if x == p - 1:
			return True
		x *= x
		x %= p
	return False

def Miller_Rabin(p, x):
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

def geneBigPrime(bit):
	p = Random(bit)
	d1 = 0
	d2 = 0
	d3 = 0
	while True:
		d1+= 1
		if pre(p) == False:
			p+= 2
			continue
		d2+=1
		if Fermat(p,20) == False:
			p+= 2
			continue
		d3+=1
		if Miller_Rabin(p,20) == False:
			p+= 2
			continue
		break
	print(d1)
	print(d2)
	print(d3)
	return p

#main
# print(Miller_Rabin(7916,20))
# print(isPrime(7918))
p = geneBigPrime(1024)
q = geneBigPrime(1024)
fo = open("BigPrime.txt","w")
fo.writeln(str(p))
fo.writeln(str(q))
print(p)
print(q)


