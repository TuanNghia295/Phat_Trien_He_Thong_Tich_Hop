import socket

def menu():
    print("Menu:")
    print("1. Count words in a string")
    print("2. Count words in each line of a file")
    print("EXIT to quit")

def main():
    host = '127.0.0.1'
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter a string: ")
            client_socket.send(text.encode())
            word_count = client_socket.recv(1024).decode()
            print("Number of words in the string: {}".format(word_count))
        elif choice == '2':
            filename = input("Enter the filename: ")
            client_socket.send(filename.encode())
            file_content = ""
            print("Enter the file content (type '.' to end):")
            while True:
                line = input()
                if line == '.':
                    break
                file_content += line + '\n'
            client_socket.send(file_content.encode())
            line_counts = client_socket.recv(1024).decode()
            print("Number of words in each line of the file:")
            print(line_counts)
        elif choice == 'EXIT':
            break

    client_socket.close()

if __name__ == '__main__':
    main()
