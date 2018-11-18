Bài tập lớn - Số học thuật toán
=============================
## Mã hóa RSA

1. Giới thiệu chung

  - Tác giả:
    - Sinh viên: **Nguyễn Tú Anh**
    - MSV: A29888
    - Trường: Đại học Thăng Long
  - Bài tập lớn:
    - Môn học: Số học thuật toán
    - Giảng viên: GS. Hà Huy Khoái
    - Chủ đề: Mã hóa RSA
    - Ngôn ngữ lập trình: Python
    - Nội dung chính: Mã hóa văn bản (Tiếng Việt có dấu) với RSA và khóa tự sinh (1024 bits)

2. Cấu trúc file

  - ***MyMath.py*** Chứa hàm toán học

    - **powMod(a, b, m)**: Trả về kết quả phép tính a^b mod m
    - **GCD(a, b)**:Trả về UCLN(a, b)
    - **GCD_extended(a, b)**: Trả về 3 số x,y,z thỏa mãn x*a + y*b = z = UCLN(a, b)

  - ***PrimeTest.py*** Chứa hàm kiểm tra tính nguyên tố

    - **Preprocessor(a)**: Kiểm tra loại bỏ các số chia hết cho 1000 số nguyên tố đầu tiên (Tiền xử lý)
    - **Fermat(p,x)**: Kiểm tra số p sử dụng định lý Fermat nhỏ với x cơ sở
    - **Miller_Rabin(p, x)**: Kiểm tra Miller- Rabin với x cơ sở

  - ***GeneFrime.py*** Chương trình sinh nguyên tố xác suất

    - **Random (b)**: Hàm trả về số lẻ ngẫu nhiên b bits
    - **getPrime(b)**: Hàm trả về số nguyên tố xác suất b bits
    - **main(b)**: Hàm chạy chương trình sinh 2 số nguyên tố xác suất b bits

  - ***CreateKey.py*** Tạo khóa cho mã hóa RSA

    - **getPQ(file)**: Lấy 2 số nguyên tố xác suất p q từ file
    - **getE(phi)**: Sinh số e là số  nguyên tố cùng nhau với phi = (p-1)(q-1)
    - **getD(e, phi)**: Lấy số d là số nghich đảo mudulo của phi của e
    - **main()**: Hàm chạy chương trình sinh khóa công khai(n,e) và khóa bí mật (n, d)
  - ***MyBase.py***  Đổi cơ số
    - **toBase(a, base)**: Đổi từ số a cơ 10 sang cơ base
    - **toInt(r, base)**: Đổi từ số r cơ base sang cơ 10
    
  - ***encode.py*** Chương trình mã hóa văn bản

    - **getPublicKey (file)**: Hàm lấy khóa công khai (n,e) từ file
    - **getPlaintext (file)**: Hàm lấy bản P rõ từ file
    - **convertStringToInt(P, base)**: Chuyển đổi các ký tự trong P thành số theo mã UTF- 8
    - **createBigInt(R, size_n)**: Ghép các số trong R với nhau thành 1 số  có số các chữ số nhỏ hơn size_n
    - **encode(n, e, P, file)**: Mã hóa bản rõ P với khóa (n, e) lưu vào file với cơ 64
    - **main()**: Hàm chạy chương trình mã hóa

  - ***decode.py*** Chương trình giải mã văn bản

    - **getPrivateKey (file)**: Lấy khóa mật (n,d) từ file
    - **getCiphertext(file)**: Lấy văn bản mã hóa từ file
    - **decode(n, d, C, base, fileOut)**: Giải mã bản mã C xuất ra bản rõ vào fileOut
    - **main()**: Chạy chương trình
