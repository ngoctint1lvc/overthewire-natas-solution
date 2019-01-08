import base64

data = base64.b64decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=").decode()
key = ""
jsonData = '{"showpassword":"no","bgcolor":"#ffffff"}'
print(len(data), len(jsonData))

for x in zip(data, jsonData):
    #print(ord(x[0]), ord(x[1]), ord(x[0]) ^ ord(x[1]))
    key += chr(ord(x[0]) ^ ord(x[1]))
print(key)