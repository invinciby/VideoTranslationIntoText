# -*- coding = utf-8 -*-
# @Time : 2021/12/3 14:48
# @Author : INVinci
# @File : BYBaiduapi.py
# @Software: PyCharm
import json
import re
from urllib import request, parse
import os


def get_token():
    API_Key = "VKyf6rOzw3vmanBG4KArAs2X"  # 官网获取的API_Key
    Secret_Key = "Tm06ybF3PYlSvGl5PG4x3qd9tckaPpfX"  # 为官网获取的Secret_Key
    # 拼接得到Url
    Url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + API_Key + "&client_secret=" + Secret_Key
    try:
        resp = request.urlopen(Url)

        result = json.loads(resp.read().decode('utf-8'))
        # 打印access_token
        print("access_token:", result['access_token'])
        return result['access_token']
    except request.URLError as err:
        print('token http response http code : ' + str(err.code))


def getTXT(name):
    # 1、获取 access_token
    token = get_token()
    # 2、打开需要识别的语音文件
    speech_data = []
    with open(name, 'rb') as speech_file:
        speech_data = speech_file.read()
    length = len(speech_data)
    if length == 0:
        print(name + ' length read 0 bytes')

    # 3、设置Url里的参数
    params = {'cuid': "9E-29-76-BE-C1-98",  # 用户唯一标识，用来区分用户，长度为60字符以内。一般用MAC地址
              'token': token,  # 我们获取到的 Access Token
              'dev_pid': 1737}  # 1737表示英语 1537 表示识别普通话

    # 将参数编码
    params_query = parse.urlencode(params)

    # 拼接成一个我们需要的完整的完整的url
    Url = 'http://vop.baidu.com/server_api' + "?" + params_query

    # 4、设置请求头
    headers = {
        'Content-Type': 'audio/wav; rate=16000',  # 采样率和文件格式
        'Content-Length': length
    }

    # 5、发送请求，音频数据直接放在body中
    # 构建Request对象
    req = request.Request(Url, speech_data, headers)
    # 发送请求
    res_f = request.urlopen(req)
    result = json.loads(res_f.read().decode('utf-8'))
    print(result)
    print("识别结果为:", result['result'][0])
    return result['result'][0]


def dealmain(ls_name):
    txt = []
    file = open(ls_name + '\\EngLishTEST.txt', 'a', encoding='utf-8')
    for each in os.listdir(ls_name):
        wav_path = re.findall(r"(.*?)\.wav", each)
        if wav_path:
            wav_name = ls_name + '\\'+wav_path[0] + '.wav'
            temp_txt = getTXT(wav_name)
            file.write(temp_txt)
            txt.append(temp_txt)
    print(txt)
    file.close()
    return file.name

# dealmain("D:\ChengXurrrrrrrrrrrrrrrrrrrr\PythonFlie\EnglishChange\yu")