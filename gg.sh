#!/bin/bash
#
echo -e "\033[0;32mRemoving old proxy... \033[0;33mremoved httpnf.txt s5nf.txt\033[0m"
#
rm -rf httpnf.txt s5nf.txt 2>/dev/null
#
echo -e "\033[0;32mDownloading proxy... \033[0;33mhttp | http/s | socks5\033[0m"
#
wget "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true" -O httpnf.txt 2>/dev/null
#
wget "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all" -O http.txt 2>/dev/null
cat http.txt >> httpnf.txt 2>/dev/null
rm -rf http.txt 2>/dev/null
#
wget "https://www.proxy-list.download/api/v1/get?type=http" -O http.txt 2>/dev/null
cat http.txt >> httpnf.txt 2>/dev/null
rm -rf http.txt 2>/dev/null
#
wget "https://www.proxy-list.download/api/v1/get?type=https" -O http.txt 2>/dev/null
cat http.txt >> httpnf.txt 2>/dev/null
rm -rf http.txt 2>/dev/null
#
wget "https://www.proxyscan.io/download?type=http" -O http.txt 2>/dev/null
cat http.txt >> httpnf.txt 2>/dev/null
rm -rf http.txt 2>/dev/null
#
wget "https://www.proxyscan.io/download?type=https" -O http.txt 2>/dev/null
cat http.txt >> httpnf.txt 2>/dev/null
rm -rf http.txt 2>/dev/null
#
wget "https://sheesh.rip/http.txt" -O http.txt 2>/dev/null
cat http.txt >> httpnf.txt 2>/dev/null
rm -rf http.txt 2>/dev/null
#
wget "https://openproxylist.xyz/http.txt" -O http.txt 2>/dev/null
cat http.txt >> httpnf.txt 2>/dev/null
rm -rf http.txt 2>/dev/null
#
wget "https://proxyspace.pro/http.txt" -O http.txt 2>/dev/null
cat http.txt >> httpnf.txt 2>/dev/null
rm -rf http.txt 2>/dev/null

wget "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true" -O socks5.txt 2>/dev/null
#
wget "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all" -O socks5.txt 2>/dev/null
cat socks5.txt >> s5nf.txt 2>/dev/null
rm -rf socks5.txt 2>/dev/null
#
wget "https://www.proxy-list.download/api/v1/get?type=socks5" -O socks5.txt 2>/dev/null
cat socks5.txt >> s5nf.txt 2>/dev/null
rm -rf socks5.txt 2>/dev/null
#
wget "https://www.proxyscan.io/download?type=socks5" -O socks5.txt 2>/dev/null
cat socks5.txt >> s5nf.txt 2>/dev/null
rm -rf socks5.txt 2>/dev/null
#
wget "https://sheesh.rip/socks5.txt" -O socks5.txt 2>/dev/null
cat socks5.txt >> s5nf.txt 2>/dev/null
rm -rf socks5.txt 2>/dev/null
#
wget "https://openproxylist.xyz/socks5.txt" -O socks5.txt 2>/dev/null
cat socks5.txt >> s5nf.txt 2>/dev/null
rm -rf socks5.txt 2>/dev/null
#
wget "https://proxyspace.pro/socks5.txt" -O socks5.txt 2>/dev/null
cat socks5.txt >> s5nf.txt 2>/dev/null
rm -rf socks5.txt 2>/dev/null

#Github api but stupid

#wget "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
#wget "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
#wget "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
#wget "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
#wget "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
#wget "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
#wget "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
#wget "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
#wget "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
#wget "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
#wget "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt" -O http.txt 2>/dev/null
#cat http.txt >> httpnf.txt 2>/dev/null
#rm -rf http.txt 2>/dev/null
#
cat httpnf.txt | sort | uniq > http.txt 2>/dev/null
mv http.txt httpnf.txt 2>/dev/null

cat s5nf.txt | sort | uniq > s5.txt 2>/dev/null
mv s5.txt s5nf.txt 2>/dev/null
#
echo -e "\033[0;32mDone, \033[0;33msave as httpnf.txt, s5nf.txt\033[0m"
#