import GenePrime

p = GenePrime.getPrime(1024)
q = GenePrime.getPrime(1024)
fo = open("BigPrime.txt","w")
fo.write(str(p)+'\n')
fo.write(str(q))
fo.close()
# print(p)
# print(q)


