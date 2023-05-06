import requests
import fileinput
import time
import os

os.system ('cls')
TOKEN = 'OTI0NzMzMjkxNTExMzA4MzQw.Gu2LdX.9ZepE-uWZxn0JliqT8u5iz1AYHXcMkR0z7e4wY'
header = {"authorization" : TOKEN}
guildinfo = requests.get("https://discord.com/api/v9/channels/1104160339907575870", headers=header).json()
lastmessageid = guildinfo["last_message_id"]
guildmessage = requests.get("https://discord.com/api/v9/channels/1104160339907575870/messages", headers=header).text
fixed = (guildmessage.removeprefix('[{"id": "' + lastmessageid + '", "type": 0, "content": "'))
userinfo = requests.get("https://discordapp.com/api/v9/users/@me", headers=header).json()
payload = {
    'content' : "That's not my id so i answer"
}
f = open('lastmessage.txt', 'w')
f.write(fixed)
f.close()
with open('lastmessage.txt', 'r', encoding='utf-8') as file:
    contents = file.read()

    character = '"'

    result = contents.split('"')[0]
f = open('lastmessageauthor.txt', 'w')
f.write(fixed)
f.close()
with open('lastmessageauthor.txt', 'r', encoding='utf-8') as file:
    contents = file.read()

    character = '"'

    authorresult = contents.split('", "username":')[0]
tiramisuid = userinfo["id"]
print(authorresult)
if tiramisuid in authorresult:
    print("test")
else:
    hello = {
        'content' : result
    }
    r = requests.post("https://discord.com/api/v9/channels/1104160339907575870/messages", headers=header, data=hello)
os.system ('python main.py')