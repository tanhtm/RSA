import MyMath

base = 4 #1e4
sz = 75

# Get (n,e) : Public key
fi = open("PublicKey.txt","r")
n = int(fi.readline())
e = int(fi.readline())
fi.close()
print(n,e)

fi = open("Plaintext.txt","r")
s = fi.read()
fi.close()

r = []
for i in s:
	c = str(ord(i))
	while len(c) != base:
		c = '0' + c
	r.append(c)

d = 0
A = []
x = ""
for i in r:
	if d < sz:
		x+= i
		d+= 1
	else:
		d = 1
		A.append(int(x))
		x = i
A.append(int(x))
print(A)

fo = open("Ciphertext.txt","w")
for i in A:
	m = i
	M = MyMath.powMod(m,e,n)
	fo.write(str(M)+'\n')
fo.close()