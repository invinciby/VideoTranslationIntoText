import re
import BYBaiduapi
import cutwav as sw
from pydub import AudioSegment
import mp4ChangeWav
import translateByBAIDU


def getlen(leng):
    L1 = int(leng + 0.5)
    if L1 < 60:
        return L1
    L2 = L1 / 60.0
    if L1 % 60 == 0:
        return 60
    else:
        L3 = int(L2 + 0.5)
        L4 = L1 / L3 + 1
        return L4


def main(interput):
    interput = interput.replace('/', '\\')
    filenames = mp4ChangeWav.getPath(interput)
    filePath = re.findall(r"(.*?)\.mp4", interput)
    wavpath = filenames
    path = filePath[0]

    if interput:
        second = AudioSegment.from_wav(wavpath).duration_seconds
        newlength = getlen(second)

        sw.cut_to_time(interput, path, newlength, wavpath)

    filePath = BYBaiduapi.dealmain(path)
    pathtxt = translateByBAIDU.trans_main(filePath, path)
    return pathtxt

# pyinstaller -F --icon=nm.ico -w dropFile.py -p BYBaiduapi.py -p cutwav.py -p mainMeun.py -p mp4ChangeWav.py -p translateByBAIDU.py
