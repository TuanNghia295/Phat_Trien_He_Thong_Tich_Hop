import socket

def calculate_sum(numbers):
    try:
        numbers = [int(num) for num in numbers]
        result = sum(numbers)
        return result
    except ValueError:
        return "Invalid input. Please enter valid integers."

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print(f"Server is listening on {server_ip}:{server_port}")

    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    while True:
        data = client_socket.recv(1024).decode()
        if data == ".":
            break
        lines = data.split('\n')
        for line in lines:
            numbers = line.split()
            result = calculate_sum(numbers)
            response = f"Tổng chuỗi vừa nhận là: {result}"
            client_socket.send(response.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
