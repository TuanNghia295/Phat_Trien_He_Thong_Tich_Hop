import socket
import threading
import os

def count_words(text):
    words = text.split()
    return len(words)

def handle_client(client_socket):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        if data.endswith('.'):
            # Count words in the string
            word_count = count_words(data[:-1])
            client_socket.send(str(word_count).encode())
        else:
            # Count words in each line
            lines = data.split('\n')
            line_counts = [str(count_words(line)) for line in lines]
            response = '\n'.join(line_counts)
            client_socket.send(response.encode())
            filename = client_socket.recv(1024).decode()
            data_to_save = client_socket.recv(1024).decode()
            dataLength = len(data_to_save)
            file_path = os.path.join(script_dir, filename + ".txt")
            with open(file_path, "w") as file:
                file.write(data_to_save)
            client_socket.send(f"Data saved to {filename}.txt".encode())
    client_socket.close()

def main():
    host = '127.0.0.1'
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server is listening on {}:{}".format(host, port))

    while True:
        client_socket, addr = server_socket.accept()
        print("Connected to: {}".format(addr))

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    main()
