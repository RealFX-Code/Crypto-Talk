import os
import PySimpleGUI as sg
from cryptography.fernet import Fernet

# Make Custon Theme.
sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {'BACKGROUND': '#7d7d7d',
                                        'TEXT': '#ffffff',
                                        'INPUT': '#545454',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('white', '#808080'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }

sg.theme('MyNewTheme')   # Set Theme For Window

# Make The Contents Of The Window.
layout = [  [sg.Text('What do you want to decrypt?')],
            [sg.Text('Enter Encrypted Message Here.'), sg.Multiline()],
            [sg.Text('Enter Key Here.'), sg.Multiline()],
            [sg.Text(' ')],
            [sg.OK(), sg.Cancel()]]


# Create the Window
window = sg.Window('Crypto-Talk Decryptor', layout)


# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        window.close()
        exit()
    if event in ('OK'):
        break

# Closes Window
#print('You entered', values[0])
#print('You entered', values[1])
window.close()

# Encrypts String
b = bytes(values[0], ('utf-8'))
a = bytes(values[1], ('utf-8'))
key = a
f = Fernet(key)
encryption_type = Fernet(key)
decrypted_message = encryption_type.decrypt(b)
DMSG = decrypted_message
DMSG2 = (DMSG.decode('utf-8'))
#print(DMSG2)

# Make The Contents Of The Box.
msgsa = [ [sg.Text('Decrypted message:')],
      [sg.Text(' ')],
          [sg.Text(DMSG2)],
          [sg.Text('Message also copied to clipboard.')],
          [sg.Text(' ')],
          [sg.Exit(),]]

os.system('echo %s | clip ' % DMSG2)

# Make The Box
windows = sg.Window('Finished Decryption', msgsa)

#Button Check Loop
while True:             
    event, values = windows.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

count = 0

while True:
    count = count+1
    print('\n')
    if count == 40:
        print('Crypto Talk (C) RealFX, 2020-2021')
        print('All Rights Reserved.')
        break

windows.close()