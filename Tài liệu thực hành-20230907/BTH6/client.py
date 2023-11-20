import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        data = input("Nhập chuỗi các số nguyên (hoặc '.' để dừng, nhấn Enter để xuống dòng):\n")
        if data == ".":
            client_socket.send(data.encode())
            break
        else:
            client_socket.send(data.encode())

        result = client_socket.recv(1024).decode()
        print(result)

    client_socket.close()

if __name__ == "__main__":
    main()
