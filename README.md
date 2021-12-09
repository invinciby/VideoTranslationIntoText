### 2021/12/9 
#### The project has been updated
#### Added a home screen
![image](https://user-images.githubusercontent.com/78719936/145416976-60716184-07f1-44e7-aad5-34650172ac70.png)
#### Just drag it onto the screen  
![image](https://user-images.githubusercontent.com/78719936/145417110-d1b97afd-6813-42cb-af7a-7977928f74df.png)
#### The final results  
![image](https://user-images.githubusercontent.com/78719936/145417255-9210fdc3-f3ff-4f04-9f40-f6a79fc53388.png)

\
\
\
\

### 2021/12/9 项目已更新
#### 添加了主界面
![image](https://user-images.githubusercontent.com/78719936/145416976-60716184-07f1-44e7-aad5-34650172ac70.png)
#### 拖到即可
![image](https://user-images.githubusercontent.com/78719936/145417110-d1b97afd-6813-42cb-af7a-7977928f74df.png)
#### 最后结果
![image](https://user-images.githubusercontent.com/78719936/145417255-9210fdc3-f3ff-4f04-9f40-f6a79fc53388.png)

\
\
\
\
\
\
\

#  Using the tutorial 

####  About the project creation process https://invinciby.github.io/

 How is this project used? 

Environment configuration:

Install this first:https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z 

```python
import re
from urllib import request, parse
import os
from pydub import AudioSegment
import math
import json
import random
import requests
from hashlib import md5
```

 Download the code and open it in the order shown below 

![step](https://user-images.githubusercontent.com/78719936/144977438-6d0a1437-9439-44ef-a1a0-c7ec36f850b1.png)

###### 1 BYBaiduapi,py

https://ai.baidu.com/tech/speech/asr Follow the instructions in the blog above to register for aipkey and password 

 Fill in the appropriate location in the code 

###### 2 translateByBAIDU.py

https://ai.baidu.com/ai-doc/SPEECH/pk38lxi60 Register for the aiPkey and password by following the steps in the above blog. （ Note: this is different from the AIP operation above, where the translation interface is implemented and the speech recognition interface is implemented in operation 1 ）

 Fill in the appropriate location in the code 

###### 3 mainMeun.py

 Run directly from here, input the video path, you can get the original audio file and translation file (currently only support English translation, you can also modify the relevant content to change the translation language) 



# 使用教程

#### 关于项目创建历程：https://invinciby.github.io/

如何使用该项目？

环境配置：

需要先安装ffmpeg https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z 

```python
import re
from urllib import request, parse
import os
from pydub import AudioSegment
import math
import json
import random
import requests
from hashlib import md5
```

下载代码，按照下面图片的顺序依次打开

![step](https://user-images.githubusercontent.com/78719936/144977438-6d0a1437-9439-44ef-a1a0-c7ec36f850b1.png)

###### 1 BYBaiduapi,py

https://ai.baidu.com/tech/speech/asr依照上面博客里面的操作进行注册，获取aipkey以及password

填入代码中相应位置

###### 2 translateByBAIDU.py

https://ai.baidu.com/ai-doc/SPEECH/pk38lxi60依照上面博客里面的操作进行注册，获取aipkey以及password（注意：这里与上面操作的aip不一样，此处实现的是翻译接口，操作1实现的是语音识别接口）

填入代码中相应位置

###### 3 mainMeun.py

从此处直接开始运行，输入视频路径，可获得原音频文件以及翻译文件（目前仅支持英译中，也可以修改相关内容改变翻译语言）




