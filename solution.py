import socket
import sys

def run(port: int =13331):

  host: str = socket.gethostname()

  server_socket: socket.SocketType = socket.socket()
  server_socket.bind( (host, port) )
  server_socket.listen(2)
  
  conn, address = server_socket.accept()

  while True:
    print('Ready to serve...')

    try:

      message = conn.recv(1024).decode()
      print(f'Message: {message}\n Address: {address}')
    
    except Exception as e:
      print(e)
      break

  server_socket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  run( port=13331 )
