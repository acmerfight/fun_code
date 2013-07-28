#coding=utf-8
import requests
import json


KUAIPAN_URL = "https://www.kuaipan.cn/account_login.html"
LOGIN_URL = "https://www.kuaipan.cn/index.php?ac=account&op=login"
SIGN_URL = "http://www.kuaipan.cn/index.php?ac=common&op=usersign"


payload = {'username': 'acmerfight@gmail.com', 'userpwd': '19881214', "isajax": "yes"}
webRequest = requests.get(KUAIPAN_URL)
cookies = webRequest.cookies
r = requests.post(LOGIN_URL, data=payload, cookies=cookies)
cookies = r.cookies
webRequest = requests.get(SIGN_URL, cookies=cookies)
response = json.loads(webRequest.text)
if response["state"] == -102:
    print "already signed"
elif response["state"] == 1:
    print "sign successful add {num}M space".format(num=response["rewardsize"])
