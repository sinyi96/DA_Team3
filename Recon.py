import requests

# Set the target webpage
url = 'http://172.18.58.238/creative/'
r = requests.get(url)
headers = {
    'User-Agent': 'Mobile'
}
# Display Output Get and Ok
print("Status code:")
print("\t *", r.status_code,headers)

# Display Website Header
h = requests.head(url)
for x in h.headers:
    print("\t", x, '.', h.headers[x])

# Modify the headers user-agent
headers = {
    'User-Agent': 'Mobile'
}
url2 = 'http://172.18.58.238/creative/'
rh = requests.get(url2, headers=headers)
print(rh.text)
