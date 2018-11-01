import MyMath

base = 4 #1e4
#Get (n,d) : Private key
fi = open("PrivateKey.txt","r")
n = int(fi.readline())
d = int(fi.readline())
fi.close()

# Get Ciphertext
fi = open("Ciphertext.txt","r")
C = []
while True:
	m = fi.readline()
	if len(m) == 0:
		break
	C.append(int(m))
fi.close()
#print(C)

# Decode
fo = open("PlaintextDecode.txt","w")
for i in C:
	m = MyMath.powMod(i,d,n)
	c = str(m)
	while len(c) % base != 0:
		c = '0' + c
	x = 0
	while x != len(c):
		a = c[x:x+base]
		x+= base
		fo.write(chr(int(a)))
