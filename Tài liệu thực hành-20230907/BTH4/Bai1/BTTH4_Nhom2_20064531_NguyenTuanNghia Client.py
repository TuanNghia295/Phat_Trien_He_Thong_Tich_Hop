# Bài 1
# CLIENT
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostnameIp = socket.gethostbyname(socket.gethostname())
port = 295

# Phương thức connect dùng để kết nối đến địa chỉ Ip của host
# và Port trùng khớp với server

s.connect((hostnameIp,port))
a = input("input numer:")
# gửi dữ liệu của a sang server
s.sendall(a.encode('utf8'))

# Phương thức recv (recieve) dùng để nhận dữ liệu từ Socket (TCP)
# buflen: số bytes tối đa có thể nhận giá trị trả về
response = s.recv(1024).decode('utf8')
print(response)
s.close()