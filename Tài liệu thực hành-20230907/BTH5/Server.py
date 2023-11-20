import socket
try:
    # use TCP, ipver4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localhost = socket.gethostbyname(socket.gethostname())
    port= 2905
    sock.bind((localhost, port))
    sock.listen(2)
    while True:
        client_socket,client_address = sock.accept()
        print("Acceped client from ip",client_address)
        # Receive data from client and decode it
        receive_data = client_socket.recv(1024).decode('utf-8')
        if receive_data == '1':
            # Dịch vụ 1: Đảo ngược chuỗi và in hoa ký tự đầu
            data = client_socket.recv(1024).decode('utf-8')
            #  sử dụng slicing để trích xuất 1 phần của chuỗi
            #  ví dụ: ta có Hello thì [1:4] sẽ trả về "ello"
            #  suy ra, để đảo ngược chuỗi, ta sử dụng slicing với giá trị là -1 ở vị trí bắt đầu
            reversed_data = data[::-1]
            #  sử dụng phương thức .split(). Mặc định, nó chia chuỗi bằng dấu cách (space)
            title_case_data = ' '.join(word.capitalize() for word in reversed_data.split())        
            client_socket.send("Kết quả đảo ngược và in hoa ký tự đầu: {}\n".format(title_case_data).encode('utf-8'))
        elif receive_data == "2":
            client_socket.send("Mai Làm".encode("utf-8"))
        # send data to client
        client_socket.close()
except Exception as e:
    print("Could not connect to ClientSocket",e)