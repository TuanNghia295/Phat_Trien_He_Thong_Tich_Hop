import socket
try:
    #  Tạo kết nối sử dụng ipv4,TCP,protocol = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # lấy localhost, tạo port
    localHost = socket.gethostbyname(socket.gethostname())
    port = 295
    #  kết nối tới server
    s.connect((localHost,port))
    a = input("Input and it will be Uppercase: ")
    # gửi dữ liệu vừa nhập tới server
    # encode: mã hóa kí tự khi gửi đi
    s.sendall(a.encode('utf8'))
    # in dữ liệu trả về từ Server với tối đa 1024 bytes và giải mã
    print(s.recv(1024).decode('utf8'))
except:
    print("connection failed")
