import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    print('\033[91mTool is Coming For Your Device Soon')
elif bit == '32bit':
    from xx32 import xnx
    xnx()
