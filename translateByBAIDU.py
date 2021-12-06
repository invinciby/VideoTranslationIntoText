# -*- coding = utf-8 -*-
# @Time : 2021/12/5 13:33
# @Author : Vinci
# @File : translateByBAIDU.py
# @Software: PyCharm

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
    # text = 'This gene encodes a cytokine distantly related to type I interferons and the IL-10 family. This gene
    # interleukin 28A (IL28A) and interleukin 29 (IL29) are three closely related cytokine genes that form a cytokine
    # gene cluster on a chromosomal region mapped to 19q13. Expression of the cytokines encoded by the three genes
    # can be induced by viral infection. All three cytokines have been shown to interact with a heterodimeric class
    # II cytokine receptor that consists of interleukin 10 receptor beta (IL10RB) and interleukin 28 receptor alpha (
    # IL28RA). [provided by RefSeq Jul 2008]'
    data = []
    with open(path, "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        print(data)
    myurl = translate_api(data)
    response = requests.get(myurl)
    rans_result = json.loads(response.text)['trans_result'][0]['dst']
    print(rans_result)

    with open(lsname+ "\\ChinsesTEST.txt", 'w') as f1:
        f1.write(rans_result)
