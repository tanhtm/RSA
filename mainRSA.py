import MyMath

fi = open("BigPrime.txt","r")
p = int(fi.readline())
q = int(fi.readline())
# print(p)
# print(q)

# p, q : Big Prime
n = p*q
#print(n)
phi = (p-1)*(q-1)
#print(phi)
# Fine e : (e,phi) = 1
e = 65537
while True:
	if MyMath.GCD(e,phi) == 1:
		break
	e+= 2
#print(e)

d = MyMath.GCD_extended(e,phi)[0] #[x,y,z] #d = x
if d < 0:
	d+= phi

#print(d)
#x = (d*e)%phi
#print(x)

fo = open("PublicKey.txt","w")
fo.write(str(n)+'\n'+str(e))
fo.close()
fo = open("PrivateKey.txt","w")
fo.write(str(n)+'\n'+str(d))
fo.close()