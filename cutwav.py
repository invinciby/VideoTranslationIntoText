# -*- coding = utf-8 -*-
# @Time : 2021/12/2 15:06
# @Author : Vinci
# @File : cutwav.py
# @Software: PyCharm

import os
import re
from pydub import AudioSegment


def cut_to_time(file_name, des_dir, split_length, wav_name):
    """
    :param file_name: 需要处理的视频路线
    :param des_dir:切割后文件存储文件夹
    :param split_length:切割后每个语音长度
    :param wav_name: wav音频文件名字
    :return:
    """
    if not os.path.exists(des_dir):
        os.mkdir(des_dir)

    filenames = wav_name
    print(filenames)
    if filenames:
        print("当前切割语音文件： ", filenames)
        sound = AudioSegment.from_wav(filenames)

        second_of_file = sound.duration_seconds
        print("该音频持续时间为：", int(second_of_file), "秒")

        times = int(int(second_of_file) / split_length)
        print("当前语音共可切割： ", times, "次")

        start_time = 0
        internal = split_length * 1000
        end_time = split_length * 1000
        name = re.split(r'[\\ .]', filenames)[-2]

        for i in range(times):
            part = sound[start_time:end_time]
            data_split_filename = os.path.join(des_dir, name + '_' + str(i) + '.wav')

            part.export(data_split_filename, format="wav")

            start_time += internal
            end_time += internal


# cut_to_time(r"D:\ChengXurrrrrrrrrrrrrrrrrrrr\PythonFlie\EnglishChange\audio\aimaSpeech.mp4", r"D:\ChengXurrrrrrrrrrrrrrrrrrrr\PythonFlie\EnglishChange\yu", 26)
