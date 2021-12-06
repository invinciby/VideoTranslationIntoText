# -*- coding = utf-8 -*-
# @Time : 2021/12/6 12:37
# @Author : Vinci
# @File : mainMeun.py
# @Software: PyCharm
import math
import re
import BYBaiduapi
import cutwav as sw
from pydub import AudioSegment
import mp4ChangeWav
import translateByBAIDU


def getlen(leng):
    leng = int(leng)  # leng表示视频原长度，此处省去小数点能够减少下面的误差
    if leng > 60:
        dlen = math.sqrt(leng)
        ilen = int(dlen)
        while ilen > 1:
            if leng % ilen * 1.0 == 0 and ilen < 60:  # 注意这里要确保最后每一个视频长度要小于一分钟，这也是该步的目的
                if ilen >= leng / ilen:
                    return ilen
                else:
                    return leng / ilen
            else:
                ilen = ilen - 1
    else:
        return leng


if __name__ == '__main__':
    interput = input("请输入需要转化的视频路径：")  # 需要处理的视频路线
    filenames = mp4ChangeWav.getPath(interput)
    filePath = re.findall(r"(.*?)\.mp4", interput)  # 切割后文件存储文件夹
    wavpath = filenames  # wav音频文件名字
    # 裁剪视频，进行处理
    if interput:
        second = AudioSegment.from_wav(wavpath).duration_seconds
        newlength = getlen(second)  # 切割后每个语音长度
        sw.cut_to_time(interput, filePath[0], newlength, wavpath)

    # 连接百度进行翻译
    filePath = BYBaiduapi.dealmain(filePath[0])
    translateByBAIDU.trans_main(filePath, filePath[0])
    print("翻译完成")