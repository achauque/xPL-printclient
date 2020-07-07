# python xPL-printclient.py IP_ADDRESS PORT PRINT_PORT

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_port = sys.argv[2]
print_port = sys.argv[3]

print server_name, server_port, print_port

server_address = (server_name, server_port)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    lpt = open(print_port + ':', 'w')
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            lpt.write(data)
            
            if data:
                print data
            else:
                lpt.close()
                break
    finally:
        connection.close()