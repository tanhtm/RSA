import MyMath

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
	fo.write(chr(m))
