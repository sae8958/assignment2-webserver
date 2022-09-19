from socket import AF_INET, SOCK_STREAM, socket
import sys

def webServer(port: int =13331):

  host: str = "127.0.0.1"
  server_socket: socket.SocketType = socket(AF_INET,SOCK_STREAM)
  server_socket.bind( (host, port) )

  while True:
    server_socket.listen(5)
    conn, address = server_socket.accept()

    try:

      message = conn.recv(1024).decode()
      filename = f'.{message.split()[1]}'
      with open(filename,"rb") as f:
        response = b'HTTP/1.1 200 OK\r\n'
        response += b"Content-Type: text/html; charset=UTF-8\r\n\r\n"
        response += f.read()
        conn.send(response.decode().encode("utf8"))
        conn.close()
    
    except FileNotFoundError:
      response = b'HTTP/1.1 404 File Not Found\r\n'
      conn.send(response.decode().encode("utf8"))
      conn.close()

    except Exception as e:
      break

  server_socket.close()
  sys.exit()


if __name__ == "__main__":
  webServer( port=13331 )
