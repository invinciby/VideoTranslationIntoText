
import json
import random
import requests
import urllib.parse
from hashlib import md5


def translate_api(text):
    appid = '20211205001019473'
    secretKey = '4VbeK9ZWhvz9zGzr1rM9'
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    q = text
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = md5()
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()

    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    return myurl


def trans_main(path, lsname):
    data = []
    with open(path, "r", encoding='utf-8', errors='ignore') as f:
        data = f.read()

    myurl = translate_api(data)
    response = requests.get(myurl)
    rans_result = json.loads(response.text)['trans_result'][0]['dst']

    with open(lsname + "\\ChinsesTEST.txt", 'w', encoding='utf-8', errors='ignore') as f1:
        f1.write(rans_result)
    return lsname + "\\ChinsesTEST.txt"
