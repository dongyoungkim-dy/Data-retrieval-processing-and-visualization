import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Read url
url = 'http://py4e-data.dr-chuck.net/comments_213805.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
data.decode()
# Read tree
tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum=0
for item in counts:
    sum = int(item.text)+sum
print(sum)
