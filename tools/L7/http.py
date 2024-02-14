_IllIIllIIllIlIIII ='no-cache'
import requests ,random ,tools .randomData as randomData 
from colorama import Fore 
IlIIIIIlIllIlIIlI =[]
for _ in range (30 ):IlIIIIIlIllIlIIlI .append (randomData .random_useragent ())
IlIllIIIIIlllIlll ={'X-Requested-With':'XMLHttpRequest','Connection':'keep-alive','Pragma':_IllIIllIIllIlIIII ,'Cache-Control':_IllIIllIIllIlIIII ,'Accept-Encoding':'gzip, deflate, br','User-agent':random .choice (IlIIIIIlIllIlIIlI )}
def IlllIllllIIlIllIl (IlIIIIIllIlIlIIIl ):
	IIlIIllIIlIlIlIII =str (random ._urandom (random .randint (10 ,150 )))
	try :IIllIlllIllIlIlll =requests .get (IlIIIIIllIlIlIIIl ,params =IIlIIllIIlIlIlIII ,headers =IlIllIIIIIlllIlll ,timeout =40 )
	except requests .exceptions .ConnectTimeout :print (f"{Fore.RED}[!] {Fore.MAGENTA}Timed out{Fore.RESET}")
	except Exception as IlIllIIlllllIIlll :print (f"{Fore.MAGENTA}Error while sending GET request\n{Fore.MAGENTA}{IlIllIIlllllIIlll}{Fore.RESET}")
	else :print (f"{Fore.GREEN}[{IIllIlllIllIlIlll.status_code}] {Fore.YELLOW}Request sent! Payload size: {len(IIlIIllIIlIlIlIII)}.{Fore.RESET}")