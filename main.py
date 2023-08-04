from requests import get, post
from colorama import Fore
import os, json, time



class DisposableMail():
    def __init__(self):
        self.version = 0.1
        self.name = "[==DisposableMail - Waker - Version %s==]" % str(self.version)
        self.description = "Create free disposable mail, and receivre verification code easily."
        self.prefix = f"{Fore.LIGHTMAGENTA_EX}[WakerLogs]{Fore.WHITE}"
        self.url = "https://api.internal.temp-mail.io/api/v3/email/"
        self.origin = "https://api.internal.temp-mail.io/api/v3/email/new"
        self.config = json.loads(open('config.json','r').read())
        self.email = self.config['email']
        
    def getEmail(self):
        if self.email == "":
            self.email = str(post(self.origin).json()['email'])
        print(self.prefix + Fore.LIGHTYELLOW_EX + " Your email address is : " + Fore.WHITE + self.email)
        print(self.prefix + Fore.LIGHTYELLOW_EX + " Listening on : " + Fore.WHITE + self.url + self.email + '/messages')
        received = []
        while True:
            i = 0
            for e in get(self.url + self.email + '/messages').json():
                if not i in received:
                    print("\n" + self.prefix + Fore.LIGHTYELLOW_EX + " New email from : " + Fore.WHITE + e['from'] + f' {Fore.LIGHTRED_EX} => {Fore.WHITE} [{e["subject"]}]' + " \n\n")
                    print(e['body_text'])
                    received.append(i)
                i += 1
            time.sleep(2)
        

theClass = DisposableMail()
os.system("title " + theClass.name)
theClass.getEmail()