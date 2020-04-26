import requests

url = "http://127.0.0.1:5000/automated_testing"
files = {'upload_file': open('file.txt','rb')}
print(files)

r = requests.post(url, files=files)
#
print(r)
print(r.text)
data = r.json()
print(data)
