import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from fucku import menu
    menu()
elif bit == '32bit':
    print(Tool is Coming For Your Device Soon)
