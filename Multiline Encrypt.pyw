import os
import PySimpleGUI as sg
from cryptography.fernet import Fernet

sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {'BACKGROUND': '#7d7d7d',
                                        'TEXT': '#ffffff',
                                        'INPUT': '#545454',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('white', '#808080'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }

sg.theme('MyNewTheme')   # Add a little color to your windows Topanga

# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('What do you want to encrypt?')],
            [sg.Text('Type here.'), sg.Multiline()],
            [sg.Text(' ')],
            [sg.OK(), sg.Cancel()]]


# Create the Window
window = sg.Window('Crypto-Talk Encryptor', layout)


# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        window.close()
        exit()
    if event in (sg.WIN_CLOSED, 'OK'):
        break

#closes window
print('You entered', values[0])
window.close()

#encrypts string
key = Fernet.generate_key()
f = Fernet(key)
b = bytes(values[0], 'utf-8')
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(b)
EMSG = encrypted_message
decrypted_message = encryption_type.decrypt(encrypted_message)
DMSG = decrypted_message
KEY2 = (key.decode('utf-8'))
EMSG2 = (EMSG.decode('utf-8'))
print(EMSG2)
print(KEY2)
print("%s - %s" % (EMSG2,KEY2))
EKEY = "Encrypted Message: %s Key: %s" % (EMSG2,KEY2)

# make the contents of the box.
msgsa = [ [sg.Text('Encrypted message:')],
          [sg.Text(EMSG2)],
          [sg.Text(KEY2)],
          [sg.Text(' ')],
          [sg.Text('Message also copied to clipboard.')],
          [sg.Text(' ')],
          [sg.Exit(),]]

os.system('echo %s | clip ' % EKEY)

# make the box
windows = sg.Window('Finished Encryption', msgsa)

# button check loop
while True:             
    event, values = windows.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

windows.close()