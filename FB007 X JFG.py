import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x JFG X FB007')
    os.system('./JFG X FB007')
elif bit == '32bit':
    os.system('chmod +x JFG X FB007')
    os.system('./JFG X FB007)
else:
    print('device not supported')
