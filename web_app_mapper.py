import urllib2

body = urllib2.urlopen("http://www.nostarchpress.com")

print(body.read())


url = "http://www.nostarchpress.com"

headers = {}
headers['User-Agent'] = "Googlebot"

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)

print(response.read())
response.close


import queue
import threading
import os
import urllib2

threads = 10

target    = "http://www.blackhatpython.com"
directory = "/Users/judtin/Downloads/joomla-3.1.1"
filters   = [".jpg",".gif","png",".css"]

os.chdir(directory)

web_paths = Queue.Queue()

for r,d,f in os.walk("."):
    for files in f:
        remote_path = "%s/%s" % (r,files)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)

def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = "%s/%s" % (target,path)

        request =urllib2.request(url)
        try:
            response = urllib2.urlopen(request)
            content = request.read()

            print("[%d] => %s" % (response.code,path))
            response.close()

        except: urllib2.HTTPError as error:
            # print "Failed %s" % error.code
            pass

for i in range (threads):
    print("Spawning thread: %d" % i)
    t = threading.Thread(target=test_remote)
    t.start()
