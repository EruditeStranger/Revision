import urllib.request,urllib.error,urllib.parse
import json

data = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_761571.json")

decoded_data = data.read().decode()
info = json.loads(decoded_data)

print("User count", len(decoded_data))
num = info["comments"]

totalsum = 0
for a in num:
    for i,k in a.items():
        if i == "name":
            continue
        else:
            totalsum += k
print(totalsum)
