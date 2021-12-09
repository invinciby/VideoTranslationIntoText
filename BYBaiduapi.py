import json
import re
from urllib import request, parse
import os


def get_token():
    API_Key = "VKyf6rOzw3vmanBG4KArAs2X"
    Secret_Key = "Tm06ybF3PYlSvGl5PG4x3qd9tckaPpfX"
    Url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + API_Key + "&client_secret=" + Secret_Key
    try:
        resp = request.urlopen(Url)

        result = json.loads(resp.read().decode('utf-8'))

        return result['access_token']
    except request.URLError as err:
        None


def getTXT(name):
    token = get_token()

    speech_data = []
    with open(name, 'rb') as speech_file:
        speech_data = speech_file.read()
    length = len(speech_data)
    if length == 0:
        None

    params = {'cuid': "9E-29-76-BE-C1-98",
              'token': token,
              'dev_pid': 1737}

    params_query = parse.urlencode(params)

    Url = 'http://vop.baidu.com/server_api' + "?" + params_query

    headers = {
        'Content-Type': 'audio/wav; rate=16000',
        'Content-Length': length
    }

    req = request.Request(Url, speech_data, headers)

    res_f = request.urlopen(req)
    result = json.loads(res_f.read().decode('utf-8'))
    return result['result'][0]


def dealmain(ls_name):
    txt = []
    file = open(ls_name + '\\EngLishTEST.txt', 'a', encoding='utf-8', errors='ignore')
    for each in os.listdir(ls_name):
        wav_path = re.findall(r"(.*?)\.wav", each)
        if wav_path:
            wav_name = ls_name + '\\'+wav_path[0] + '.wav'
            temp_txt = getTXT(wav_name)
            file.write(temp_txt)
            txt.append(temp_txt)
    file.close()
    return file.name

