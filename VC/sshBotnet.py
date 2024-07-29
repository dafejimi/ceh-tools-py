import optparse
import pxxsh
class Client:
    def __init__(self, user, host, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()
    def connect(self):
        try:
            s = pxxsh.pxxsh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception, e:
            print(e)
            print("[-] Error connecting")
    def send_command(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before
def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print("[*] Output from " + client.host)
        print("[+] " + output + '\n')
def addClient(host, user, password):
    client = Client(host, user, password)
    botNot.append(client)
botNet = []
addClient('10.10.10.110', 'root','toor')
addClient('10.10.10.120', 'root','toor')
addClient('10.10.10.130', 'root','toor')

botnetCommand('uname -v')
botnetCommand('cat /etc/issue')
            
