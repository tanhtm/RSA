Bài tập lớn - Số học thuật toán
=============================
# Mã hóa RSA

## 1. Giới thiệu chung

  - **Tác giả**:
    - Sinh viên: *Nguyễn Tú Anh*
    - MSV: A29888
    - Trường: Đại học Thăng Long
  - **Môn học và đề tài**:
    - Môn học: Số học thuật toán
    - Giảng viên: GS. Hà Huy Khoái
    - Chủ đề: Mã hóa RSA
    - Ngôn ngữ lập trình: Python
    - Tài nguyên sử dụng: Tính toán trên số lớn có sẵn của python
    - Nội dung chính: Mã hóa văn bản (Tiếng Việt có dấu) với RSA và khóa tự sinh (1024 bits)

## 2. Giới thiệu chung cấu trúc bài tâp lớn

  - ***MyMath.py***:  Chứa hàm toán học

    - **powMod(a, b, m)**: Trả về kết quả phép tính a^b mod m
    - **GCD(a, b)**:Trả về UCLN(a, b)
    - **GCD_extended(a, b)**: Trả về 3 số x,y,z thỏa mãn x*a + y*b = z = UCLN(a, b)

  - ***PrimeTest.py***: Chứa hàm kiểm tra tính nguyên tố

    - **Preprocessor(a)**: Kiểm tra loại bỏ các số chia hết cho 1000 số nguyên tố đầu tiên (Tiền xử lý)
    - **Fermat(p,x)**: Kiểm tra số p sử dụng định lý Fermat nhỏ với x cơ sở
    - **Miller_Rabin(p, x)**: Kiểm tra Miller- Rabin với x cơ sở

  - ***GenePrime.py***: Chương trình sinh nguyên tố xác suất

    - **Random (b)**: Hàm trả về số lẻ ngẫu nhiên b bits
    - **getPrime(b)**: Hàm trả về số nguyên tố xác suất b bits
    - **main(b)**: Hàm chạy chương trình sinh 2 số nguyên tố xác suất b bits

  - ***CreateKey.py***: Tạo khóa cho mã hóa RSA

    - **getPQ(file)**: Lấy 2 số nguyên tố xác suất p q từ file
    - **getE(phi)**: Sinh số e là số  nguyên tố cùng nhau với phi = (p-1)(q-1)
    - **getD(e, phi)**: Lấy số d là số nghich đảo mudulo của phi của e
    - **main()**: Hàm chạy chương trình sinh khóa công khai(n,e) và khóa bí mật (n, d)
  - ***MyBase.py***:  Đổi cơ số
    - **toBase(a, base)**: Đổi từ số a cơ 10 sang cơ base
    - **toInt(r, base)**: Đổi từ số r cơ base sang cơ 10

  - ***encode.py***: Chương trình mã hóa văn bản

    - **getPublicKey (file)**: Hàm lấy khóa công khai (n,e) từ file
    - **getPlaintext (file)**: Hàm lấy bản P rõ từ file
    - **convertStringToInt(P, base)**: Chuyển đổi các ký tự trong P thành số theo mã UTF- 8
    - **createBigInt(R, size_n)**: Ghép các số trong R với nhau thành 1 số  có số các chữ số nhỏ hơn size_n
    - **encode(n, e, P, file)**: Mã hóa bản rõ P với khóa (n, e) lưu vào file với cơ 64
    - **main()**: Hàm chạy chương trình mã hóa

  - ***decode.py***: Chương trình giải mã văn bản

    - **getPrivateKey (file)**: Lấy khóa mật (n,d) từ file
    - **getCiphertext(file)**: Lấy văn bản mã hóa từ file
    - **decode(n, d, C, base, fileOut)**: Giải mã bản mã C xuất ra bản rõ vào fileOut
    - **main()**: Chạy chương trình

## 3. MyMath - Hàm toán học
  - **powMod(a, b, m)**
    - Ý nghĩa:  Trả về kết quả phép tính `a^b mod m`
    - Kiến thức: **Bình phương liên tiếp**
    - Code:

      ```python
      def powMod(a, b, m):
      	x = []
      	while b != 0:
      		x.append(b & 1)
      		b = b >> 1
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
      ```
  - **GCD(a, b)**
    - Ý nghĩa: Trả về `UCLN(a, b)`
    - Kiến thức: **UCLN(a, b)= UCLN(b, a% b)**, Giải thuật **Euclid**
    - Code:
    ```python
    def GCD(a, b):
    	if b == 0:
    		return a
    	return GCD(b, a%b)
    ```
  - **GCD_extended(a, b)**
    - Ý nghĩa: Trả về 3 số x,y,z thỏa mãn `x*a + y*b = z = UCLN(a, b)`
    - Kiến thức: Giải thuật **Euclid mở rộng**
    - Code:
    ```python
    def GCD_extended(a, b):
    	u1, u2, u3 = 1, 0, a
    	v1, v2, v3 = 0, 1, b
    	while v3 != 0:
    		q = u3//v3
    		t1, t2, t3 = u1 - q*v1, u2 - q*v2, u3 - q*v3
    		u1, u2, u3 = v1, v2, v3
    		v1, v2, v3 = t1, t2, t3
    	return u1, u2, u3
    ```

## 4. PrimeTest - Các hàm kiểm tra tính nguyên tố
  - **Fermat(p,x)**:
    - Ý nghĩa: Kiểm tra số p sử dụng định lý Fermat nhỏ với x cơ sở.
    - Kiến thức:
      - Định lý Fermat nhỏ: `a^(p-1) ≡ 1(mod p)` (p: số nguyên tố và a không chia hết cho p)
      - Số giả nguyên tố cơ sở
    - Code:
    ```python
    def Fermat(p,x):
    	for i in range(x):
    		a = sprime[i]
    		if MyMath.powMod(a,p-1,p) != 1:
    			return False
    	return True
    ```
  - **Miller_Rabin(p, x)**:
    - Ý nghĩa: Kiểm tra Miller- Rabin với x cơ sở
    - Kiến thức: n là số nguyên dương lẻ, `n-1 =2^s*m`, n trải qua Miller cơ sở b nếu `b^t ≡ 1 mod n` hoặc `b^((2^j)t) ≡ -1 mod n` với j nào đó 0 ≤ j ≤ s-1
    - Code:

    ```python
    # Q(a,p,m,s) = 1 nếu p trải qua Miller-Rabin cơ sở a
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
    		a = sprime[i]
    		if Q(a,p,m,s) == False:
    			return False
    	return True
    ```

## 5. Mã hóa RSA
  - **Tạo khóa**
    - Lấy 2 số `p,q`
    - Gắn `n = p*q`, `φ(n) = (p-1)(q-1)`
    - Lấy e sao cho `(e, φ(n)) = 1`
    - Gắn d là nghịch đảo modulo phi của e, xử dụng **GCD_extended**
    ```python
    def getD(e, phi):
    	d = MyMath.GCD_extended(e,phi)[0] #[x,y,z] #d = x
    	if d < 0:
    		d+= phi
    	return d
    ```
    - In kết quả ra file
  - **Mã hóa**
    - Lấy khóa công khai `(n, e)`
    - Lấy bản rõ `P`
    - Chuyển các kí tự trong P về số theo bản mã `UTF-8` tạo thành mảng các số R
    - Ghép các số trong R thành số lớn nhỏ hơn n thành số `Pi` rồi mã hóa nó thành `Ci` với công thức: `Ci ≡ Pi^e mod n`
    ```python
    def encode(n, e, P, file):
    	fo = open(file,"w")
    	C = ""
    	R = convertStringToInt(P, 4)
    	A = createBigInt(R, len(str(n)))
    	for i in A:
    		M = MyMath.powMod(i,e,n)
    		M = MyBase.toBase(M,64)
    		C+= M + ' '
    		fo.write(M+' ')
    	fo.close()
    	return C
    ```
    - In mảng số mới ra file với `cơ số 64`
  - **Giải mã**
    - Lấy khóa bảo mật `(n, d)`
    - Lấy bản mã C trong file chuyển về `cơ số 10`
    - Lấy từ số trong C là `Ci` giải mã được `Pi` với công thức: `Pi ≡ Ci^d mod n`
    - Lấy kết quả tách số rồi chuyển về dạng kí tự
    - In kết quả ra file
    ```python
    def decode(n, d, C, base, fileOut): # file PlanintextDecode
    	fo = open(fileOut,"w")
    	P = ""
    	for i in C:
    		m = MyMath.powMod(MyBase.toInt(i,64),d,n)
    		c = str(m)
    		while len(c) % base != 0:
    			c = '0' + c
    		x = 0
    		while x != len(c):
    			a = c[x:x+base]
    			x+= base
    			P+= chr(int(a))
    			fo.write(chr(int(a)))
    	fo.close()
    	return P
    ```

  - **Kiến thức**
    - Tính nghịch đảo modulo bằng giải thuật *Euclid mở rộng*
    - Định lý Euler: `a^φ(n) ≡ 1 mod n` với (a,n) = 1
