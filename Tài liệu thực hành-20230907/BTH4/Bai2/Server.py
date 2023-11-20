import socket
try:
    # Sử dụng kết nối ipv4,TCP,protocol = 0
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Lấy địa chỉ local host và đặt port
    localHost = socket.gethostbyname(socket.gethostname())
    port = 295
    # Gắn địa chỉ tới socket
    # Socket là điểm đầu cuối (endpoint) trong 1 kênh giao tiếp
    # Các socket có thể giao tiếp 
    # bên trong 1 tiến trình,giữa các tiến trình trong cùng 1 thiết bị
    # hoặc giữa các tiến trình khác nhau

    # Nói dễ hiểu thì khi ta có 2 máy, nó được nối với nhau qua 1 kênh giao tiếp
    # và Socket là điểm đầu, cuối (endpoint) của kênh đó
    # và 2 máy có thể giao tiếp dựa theo socket đó
    s.bind((localHost,port))

    # Lắng nghe tối đa 1 kết nối đồng thời
    s.listen(1)

    # Sử dụng vòng while là True để luôn chạy,
    # để lắng nghe kết nối từ Client
    while True:
        client_socket,client_address = s.accept()
        print("Connection accepted from",client_address)

        # Nhận dữ liệu là 1 chuỗi tối đa 1024 bytes từ client 
        recieveInfo = client_socket.recv(1024)

        # Xử lý dữ liệu nhận được bằng decode (giải mã) và gửi trả lại dưới dạng encode (mã hóa)
        recieveInfo = recieveInfo.decode("utf-8")
        client_socket.sendall(recieveInfo.upper().encode('utf-8'))
        client_socket.close()
except Exception as e:
    print("Connection Error",e)

