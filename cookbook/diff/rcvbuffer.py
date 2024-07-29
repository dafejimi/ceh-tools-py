import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buf_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # get the size of the sockets send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKNET, socket.SO_SNDBUF)
    print("buffer size [Before]:%d" % bufsize)
    
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_SNDBUF,
            SEND__BUF_SIZE)
    sock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_RCVBUF,
            RECV_BUF_SIZE)
    
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print(("Buffer size [After]:%d" % bufsize)
    
modify_buf_size()    