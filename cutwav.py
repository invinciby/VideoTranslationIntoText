
import os
import re
from pydub import AudioSegment


def cut_to_time(file_name, des_dir, split_length, wav_name):

    if not os.path.exists(des_dir):
        os.mkdir(des_dir)

    filenames = wav_name

    if filenames:

        sound = AudioSegment.from_wav(filenames)

        second_of_file = sound.duration_seconds

        times = int(int(second_of_file) / split_length)
        while times * 60 < second_of_file:
            times += 1

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
