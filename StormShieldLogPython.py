import requests
import pyotp

otpauth_uri = "otpauth://"
url = 'https://10.15.254.254/auth/plain.html'
totp = pyotp.parse_uri(otpauth_uri)
otp_code = totp.now()
headers = {
    'Host': '10.15.254.254',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://10.15.254.254/auth/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '100',
    'Origin': 'https://10.15.254.254',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
    'Connection': 'close'
}
data = {
    'url': '',
    'logout': '',
    'uid': 'username',
    'authnum': '0',
    'pswd': 'mdp',
    'totp': otp_code,
    'n_time': '240'
}

response = requests.post(url,verify=False ,headers=headers, data=data)

print(response.text)
f = open('cookie.txt','w')
f.write(str(response.cookies))
f.close()
