def toBinary(a, bits):
	s = str(bin(a))
	#print(s)
	s.pop(1)
	while len(s) != bits:
		s = '0' + s
	return s
P = "Nguyễn Tú Anh"
print(P.encode())