import base64

key = 'qw8J'
jsonData = '{"showpassword":"yes","bgcolor":"#ffffff"}'

data = ""
for i in range(len(jsonData)):
    data += chr(ord(jsonData[i]) ^ ord(key[i % len(key)]))

cookie = base64.b64encode(data.encode()).decode()
print(cookie)