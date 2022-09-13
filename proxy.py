import aiohttp
import asyncio
import multiprocess
import socket
import socks
import random
import threading
import ssl
from datetime import *
import datetime
from shutil import which
from urllib import parse
from os import system
import subprocess
import random
import os
import sys
import time
import json
import re
import time
from time import *
from time import sleep
import colorama
import requests
import httpx
import getpass
import screen
from colorama import *
import progressbar
from tqdm import tqdm

#a1 = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=500&country=all&ssl=all&anonymity=all"
a2 = "https://www.proxy-list.download/api/v1/get?type=http" 
#a3 = "https://www.proxyscan.io/api/proxy?type=http&format=txt&limit=10" 
#a4 = "https://proxy11.com/api/proxy.txt?key=NDAzNg.YYHPVA.QB8moHDjsHJ_R_q8lkgkUV3wt2c" 
#5 = "https://proxylist.geonode.com/api/proxy-list?protocols=http" 
a6 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true" 
a7 = "https://www.proxy-list.download/api/v1/get?type=http" 
a8 = "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt" 
a9 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http" 
a10 = "https://raw.githubusercontent.com/chipsed/proxies/main/proxies.txt" 
a11 = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt" 
a12 = "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt" 
a13 = "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt" 
a14 = "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt" 
a15 = "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt" 
a16 = "https://raw.githubusercontent.com/proxiesmaster/Free-Proxy-List/main/proxies.txt" 
#a17 = "https://api.proxyscrape.com/v2/account/datacenter_shared/proxy-list?auth=8fo1gdqz21oamvso6zdy&type=getproxies&country[]=all&protocol=http&format=normal&status=all" 
a18 = "https://raw.githubusercontent.com/roma8ok/proxy-list/main/proxy-list-http.txt" 
a19 = "https://raw.githubusercontent.com/roma8ok/proxy-list/main/proxy-list-https.txt" 
a20 = "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt" 
a21 = "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt" 
a22 = "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt" 
a23 = "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt" 
a24 = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt" 
a25 = "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt"
a26 = "https://www.proxy-list.download/api/v1/get?type=http" 
a27 = "https://www.proxy-list.download/api/v1/get?type=https" 
#a28 = "https://www.proxyscan.io/download?type=http" 
with open("pr.txt", 'w') as p:  
     #     p.write(httpx.get(a1).text) 
          p.write(httpx.get(a2).text) 
          # p.write(httpx.get(a3).text) 
         # p.write(httpx.get(a4).text) 
         # p.write(httpx.get(a5).text) 
          p.write(httpx.get(a6).text)
          p.write(httpx.get(a7).text) 
          p.write(httpx.get(a8).text) 
          p.write(httpx.get(a9).text)
          p.write(httpx.get(a10).text) 
          p.write(httpx.get(a11).text) 
          p.write(httpx.get(a12).text)
          p.write(httpx.get(a13).text) 
          p.write(httpx.get(a14).text) 
          p.write(httpx.get(a15).text)
          p.write(httpx.get(a16).text) 
      #    p.write(httpx.get(a17).text) 
          p.write(httpx.get(a18).text)
          p.write(httpx.get(a19).text) 
          p.write(httpx.get(a20).text) 
          p.write(httpx.get(a21).text)
          p.write(httpx.get(a22).text) 
          p.write(httpx.get(a23).text) 
          p.write(httpx.get(a24).text)
          p.write(httpx.get(a25).text) 
          p.write(httpx.get(a26).text) 
          p.write(httpx.get(a27).text)
     #     p.write(httpx.get(a28).text) 
          os.system(f'node proxychecker.js pr.txt http proxys.txt 1')