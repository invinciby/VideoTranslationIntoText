# 利用 百度API进行语音识别

## 前言

在某次翻墙学习算法的时候，发现了一个学习视频讲的挺不错的，但是没有字幕而且语音是英文，虽然YouTube有翻译的强大功能，现在市场上也有许多软件可以依据视频提取语音文本，但是自己还是想试一试能不能开发出来一个简单的软件。该文主要记录一下自己的学习开发历程。

## 首先准备

首先是根据需求规划大致开发路线：

最初资源：.MP4

最终需求结果：（有字幕且有译文的）.MP4



>  #### 视频  ——》》》提取音频文件 ——》》》提取文本 ——》》》翻译中文
>
>  ####           ——》》》传入视频形成字幕 ——》》》输出视频 

## 具体实现

### 一、提取音频文件

准备一段长视频(.MP4)，创建项目文件。利用**ffmpeg**将视频格式文件转换为.wav格式文件。

#### 关于ffmpeg的使用

```
ffmpeg {全局参数} {输入文件参数} -i {输入文件} {输出文件参数} {输出文件}
```

```
-c：指定编码器
-c copy：直接复制，不经过重新编码（这样比较快）
-c:v：指定视频编码器
-c:a：指定音频编码器
-i：指定输入文件
-an：去除音频流
-vn： 去除视频流
-preset：指定输出的视频质量，会影响文件的生成速度，有以下几个可用的值 ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow。
-y：不经过确认，输出时直接覆盖同名文件。
```

###### 常见用法

1. 查看文件信息

    查看视频文件的元信息

    ```
    ffmpeg -i (name).mp4
    ```

    ![1638588811724](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638588811724.png)

    加入-hide_banner参数可以减少冗余信息的输出，只显示元信息

    ![1638588944005](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638588944005.png)

2. 转换编码格式

    将视频文件从一种编码转成另一种编码。

    ```
    ffmpeg -i [input.file] -c:v libx264 output.mp4 
    ```

    ![1638589578958](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638589578958.png)

3. 转换容器格式

    将视频文件从一种容器转到另一种容器

    ```
    ffmpeg -i input.mp4 -c copy output.webm
    ```

    只是转一下容器，内部的编码格式不变，所以使用-c copy指定直接拷贝，不经过转码，这样比较快。 

4. 调整码率

     改变编码的比特率，一般用来将视频文件的体积变小。 

    ```
    ffmpeg -i input.mp4 -minrate 964K -maxrate 3856K -bufsize 2000K output.mp4
    ```

    ( 指定码率最小为964K，最大为3856K，缓冲区大小为 2000K。 )

5. 改变分辨率

    从1080p转为480p

    ```
    ffmpeg -i input.mp4 -vf scale=480:-1 output.mp4
    ```

6. 提取音频

    ```
    ffmpeg -i input.mp4 -vn -c:a copy output.aac
    ```

    -vn表示去掉视频，-c:a copy表示不改变音频编码，直接拷贝

    ```
    ffmpeg -i {input.mp4} -ac 1 -ar {采样率(16000)} {output.wav} && y
    ```

7. 添加音轨

    将外部音轨加入视频，比如添加背景音乐活旁白

    ```
    ffmpeg -i input.acc -i intput.mp4 output.mp4
    ```

8. 截图

    ```
    //从指定时间开始，连续对1秒视频进行截图
    ffmpeg -y -i input.mp4 -ss 00:01:45 -t 00:00:01 output_%3d.jpg
    ```

    ![1638590835916](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638590835916.png)

    截图显示：

    ![1638590859217](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638590859217.png)

    如果只需要一张截图

    ```
    ffmpeg -ss 00:02:10 -i aimaSpeech.mp4 -y -f image2 -frames:v 1 1.jpg
    ```

    -vframes 1 表示只取一帧  -q:v 2 表示输出图片的质量，一般是1~5（1的质量最高）

    ![1](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5C1.jpg)

9. 剪裁

     截取原始视频里面的一个片段，输出为一个新视频。可以指定开始时间（start）和持续时间（duration），也可以指定结束时间（end）。 

    ```
    ffmpeg -ss [start] -i [input] -to [end] -c copy [output]
    ```

    ![1638592808467](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638592808467.png)

    

    ![1638592788135](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638592788135.png)

10. 为音频添加封面

    ```
    ffmpeg -loop 1 -i cover.jpg -i input.mp4 -c:v libx264 -c:a aac -b:a 192k -shortest output.mp4
    ```

     有两个输入文件，一个是封面图片`cover.jpg`，另一个是音频文件`input.mp3`。`-loop 1`参数表示图片无限循环，`-shortest`参数表示音频文件结束，输出视频就结束。 

    ![1638593466979](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638593466979.png)

    

### ![1638593444337](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638593444337.png)二、提取文本

我翻阅了多种资料，对于如何实现音频转文本的方法有三种，一种是通过使用 **TensorFlow** 框架利用模型训练，目前有三种模型**HMM**、**DNN**和**End-to-End**。但是由于该方法写代码耗时长工程量大且目前的训练集不够，因此在当前阶段难以实现。第二种方法是通过利用python自带库“speech_recognition”直接实现语音识别，Speech-Recognition 附带 Google Web Speech API 的默认 API 密钥，可直接使用它。 但是该方法准确度不高， 识别率很低 。最后一种也是本次功能实现的方法就是通过使用科大讯飞API或百度API/（SDK也可以）。

该项目使用的是百度API，这里有一个缺陷就是百度API每次连接只能识别一分钟以内的语音，因此我们需要对长语音进行裁剪缝合处理。

首先先连接百度API，测试实现代码。

先在[百度AI开发平台](https://ai.baidu.com/ai-doc/SPEECH/tk4o0bm3v)查看技术文档，查询接口要求。



![1638626932583](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638626932583.png)



![1638626967218](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638626967218.png)

![1638627030321](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638627030321.png)

大致使用方法就是，先获取url，设置请求头，发送请求，连接百度语音识别平台传入音频文件，最后获取对应识别结果数据。

![1638627262914](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638627262914.png)

代码如下：

```python
# -*- coding = utf-8 -*-
# @Time : 2021/12/3 14:48
# @Author : INVinci
# @File : BYBaiduapi.py
# @Software: PyCharm
import json
from urllib import request, parse


def get_token():
    API_Key = "VKyf6r*******X"  # 官网获取的API_Key
    Secret_Key = "Tm****************PfX"  # 为官网获取的Secret_Key
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


def main():
    # 1、获取 access_token
    token = get_token()

    
    # 2、打开需要识别的语音文件
    speech_data = []
    with open("a2.wav", 'rb') as speech_file:
        speech_data = speech_file.read()
    length = len(speech_data)
    if length == 0:
        print('file 0.wav length read 0 bytes')

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
    print(result['result'])

if __name__ == '__main__':
    main()
```

成功实现完语音识别之后，就可以对音频文件进行处理了。将音频文件分为多个一分钟文件然后多次上传得出数据文本。

#### · 关于裁剪音频文件的

需要注意的是，如果音频文件时间长度仅仅是除以一分钟的数值会自动四舍五入，这样容易导致音频文件缺失。因此我们需要找到数值的公因数，找到最适宜的数值（使生成文件数量最少最佳）。

```python
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
```

在百度接口语音识别翻译时，利用遍历剪裁生成的目录进行修改。

最后生成的结果放入txt文本文档。

最后利用百度的文本翻译接口（免费）进行文本翻译实现新的文本文件。

![1638783802082](D:%5CChengXurrrrrrrrrrrrrrrrrrrr%5CPythonFlie%5CEnglishChange%5Cread%5C1638783802082.png)

```python
def translate_api(text):
    appid = '202********473'
    secretKey = '4*****9'
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

```

最后依据以上的过程打包，结构如下：

```python
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
```



## 三、结合QT实现界面打包

待补充

