import crypt
def testPass(cryptpass):
    salt = cryptpass[0:2]
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypr.crypt(word,salt)
        if (cryptWord == cryptPass):
            print("[+] Found Password: "+word+"\n")
            return
   print("[-] Password not Found.\n")
   return
def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in passFile.readlines():
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip( )
            print("[+] Cracking Password For: "+user)
            tesPass(cryptPass)

if __name__ = "__main__":
    main()
