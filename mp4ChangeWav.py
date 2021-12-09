
import os
import re


def mp4_to_wav(mp4_path, wav_path, sampling_rate):
    if os.path.exists(wav_path):
        os.remove(wav_path)
    command = "ffmpeg -i {} -ac 1 -ar {} {} && y".format(mp4_path, sampling_rate, wav_path)
    os.system(command)


def getPath(desPath):
    mp4_path = desPath
    mp4_pathdir = re.findall(r"(.*?)\.mp4", mp4_path)
    wav_path = mp4_pathdir[0] + '.wav'
    sampling_rate = 16000
    mp4_to_wav(desPath, wav_path, sampling_rate)
    return wav_path
