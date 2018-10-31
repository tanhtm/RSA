import MyMath

# Get (n,e) : Public key
fi = open("PublicKey.txt","r")
n = int(fi.readline())
e = int(fi.readline())
fi.close()
print(n,e)

# Get plaintext
fi = open("Plaintext.txt","r")
plaintext = fi.read()
print(plaintext)
fi.close()

# Encode
fo = open("Ciphertext.txt","w")
for i in plaintext:
	m = ord(i)
	#print(m)
	M = MyMath.powMod(m,e,n)
	fo.write(str(M)+'\n')
fo.close()

