import socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localhost = socket.gethostbyname(socket.gethostname())
    port = 2905
    sock.connect((localhost, port))

    while True:
        # recieve data from socket
        print("Danh sách dịch vụ:")
        print("1. Đảo ngược chuỗi và in hoa ký tự đầu")
        print("2. Tính tổng các số nguyên")
        print("3. Thoát")
        a = input("Xin mời nhập lựa chọn của bạn:")
        sock.send(a.encode("utf-8"))
        if a == "1":
            value = input("Nhập chuỗi: ")
            sock.send(value.encode("utf-8"))
            result = sock.recv(1024).decode('utf-8')
            print(result)
        elif a == "2":
            result = sock.recv(1024).decode('utf-8')
            print(result)
        if a == "3":
            break
    sock.close()
except Exception as e:
    print("Exception in socket",e)