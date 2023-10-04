# Bài 1: 
# SERVER
import socket
# Khởi tạo socket
# AF_UNIX: ip ver 6
# AF_INET: ip ver 4
# SOCK_STREAM: dùng giao thức TCP
# SOCK_DGRAM: dùng giao thức UDP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# lấy local host
hostnameIp = socket.gethostbyname(socket.gethostname())

port = 295

# Phương thức bind(hostname, port) chỉ định socket lắng nghe với địa 
# chỉ IP của máy lấy từ phương thức gethostname() trên port xác định. 
s.bind((hostnameIp,port))
# Phương thức listen() cho python biết socket này là một server, 
# tham số của phuong thức này là số lượng các kết nối có thể có trong 
# hàng đợi

s.listen(1) # chỉ có 1 kết nối có thể có trong hàng đợi

# Phương thức accept(data[,flag]) đưa server vào trạng thái chờ đợi cho đến khi 
# có một client kết nối tới port mà bạn đã xác định, phương thức này 
# trả về một đối tượng connection biểu diễn kết nối tới client đó.

while True:
    #  tạo biến c và address để truyền việc chờ client vào
    c,address = s.accept()
    print("Connection accepted from",address)
    
    # Nhận dữ liệu từ CLient
    data = c.recv(1024).decode("utf-8")
   
    # Phương thức sendall() truyền dữ liệu tới socket
    # Phương thức này tiếp tục gửi dữ liệu từ chuỗi cho tới khi
    # tất cả dữ liệu được gửi hoặc có lỗi
    # trả về None khi thành công
    print("received data: ", data)
    c.sendall(data.encode("utf-8"))
    c.close()