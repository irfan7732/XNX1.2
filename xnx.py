import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('rm -rf XNX1.2')
    print('\033[91mTool is Coming For Your Device Soon')
elif bit == '32bit':
    os.system('clear')
    os.system('rm -rf XNX1.2')
    from xx32 import xnx
    xnx()
