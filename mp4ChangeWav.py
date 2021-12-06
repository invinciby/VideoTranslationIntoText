# -*- coding = utf-8 -*-
# @Time : 2021/11/19 12:22
# @Author : Vinci
# @File : mp4ChangeWav.py
# @Software: PyCharm
import os
import re


def mp4_to_wav(mp4_path, wav_path, sampling_rate):
    # 如果存在wav_path文件，先删除。
    if os.path.exists(wav_path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(wav_path)
        # 终端命令
    command = "ffmpeg -i {} -ac 1 -ar {} {} && y".format(mp4_path, sampling_rate, wav_path)
    print('命令是：', command)
    # 执行终端命令
    os.system(command)
    print("over")


def getPath(desPath):
    mp4_path = desPath
    # path = None
    mp4_pathdir = re.findall(r"(.*?)\.mp4", mp4_path)
    wav_path = mp4_pathdir[0]+'.wav'
    print(wav_path)
    # for each in os.listdir('.'):
    #     mp4_pathdir = re.findall(r"(.*?)\.mp4", each)
    #     if mp4_pathdir:
    #         wav_path += ("\\" + mp4_pathdir[0] + '.wav')
    #         mp4_pathdir[0] += '.mp4'
    #         path = mp4_path + "\\" + mp4_pathdir[0]
    #
    # print(path)
    # print(wav_path)
    sampling_rate = 16000  # 采样率
    mp4_to_wav(desPath, wav_path, sampling_rate)
    return wav_path


# wav = getPath(r"D:\ChengXurrrrrrrrrrrrrrrrrrrr\PythonFlie\EnglishChange\audio\aimaSpeech.mp4")