import requests
import pyotp

IP = 'PUT IP OR NAME'
username = 'username'
password = 'password'
cookiec = 'YES' #YES OR NO if you want to save cookie : YES else : NO
otpauth_uri = "PUT THE otpauth path here starting with : otpauth://"

url = 'https://'+IP+'/auth/plain.html'
totp = pyotp.parse_uri(otpauth_uri)
otp_code = totp.now()

headers = {
    'Host': IP,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://'+IP+'/auth/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '100',
    'Origin': 'https://'+IP,
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
    'uid': username,
    'authnum': '0',
    'pswd': password,
    'totp': otp_code,
    'n_time': '240'
}

response = requests.post(url,verify=False ,headers=headers, data=data)
if cookiec == 'YES':
    f = open('cookie.txt','w')
    f.write(str(response.cookies))
    f.close()
