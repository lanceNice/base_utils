import base64
import json
import hashlib
import urllib.request
import urllib.parse
from multiprocessing import Pool
import time


# 全局变量 返回结果
result=''

# TEXT 文本 OUTPUT_FILE  输出音频的保存路径
def init(TEXT,OUTPUT_FILE):
    p = Pool(1)
    p.apply_async(func=__change,args=(TEXT,OUTPUT_FILE,),callback=__returnRusult)
    p.close()  # 关闭进程池，关闭后，p不再接收新的请求。
    p.join()
    return result

# 异步执行的方法
def __change(TEXT,OUTPUT_FILE):
    # API请求地址、API_KEY、APP_ID等参数，提前填好备用
    api_url = "http://api.xfyun.cn/v1/service/v1/tts"
    API_KEY = "c01a79d98e75c415205150f5742c0c69"
    APP_ID = "5be0fe46"
    # 构造输出音频配置参数
    Param = {
        "auf": "audio/L16;rate=16000",    #音频采样率
        "aue": "raw",    #音频编码，raw(生成wav)或lame(生成mp3)
        "voice_name": "xiaoyan",
        "speed": "50",    #语速[0,100]
        "volume": "77",    #音量[0,100]
        "pitch": "50",    #音高[0,100]
        "engine_type": "aisound"    #引擎类型。aisound（普通效果），intp65（中文），intp65_en（英文）
    }
    # 配置参数编码为base64字符串，过程：字典→明文字符串→utf8编码→base64(bytes)→base64字符串
    Param_str = json.dumps(Param)    #得到明文字符串
    Param_utf8 = Param_str.encode('utf8')    #得到utf8编码(bytes类型)
    Param_b64 = base64.b64encode(Param_utf8)    #得到base64编码(bytes类型)
    Param_b64str = Param_b64.decode('utf8')    #得到base64字符串

    # 构造HTTP请求的头部
    time_now = str(int(time.time()))
    checksum = (API_KEY + time_now + Param_b64str).encode('utf8')
    checksum_md5 = hashlib.md5(checksum).hexdigest()
    header = {
        "X-Appid": APP_ID,
        "X-CurTime": time_now,
        "X-Param": Param_b64str,
        "X-CheckSum": checksum_md5
    }
    # 构造HTTP请求Body
    body = {
        "text": TEXT
    }
    body_urlencode = urllib.parse.urlencode(body)
    body_utf8 = body_urlencode.encode('utf8')
    # 发送HTTP POST请求
    print("ttv1")
    print(time.time())
    req = urllib.request.Request(api_url, data=body_utf8, headers=header)
    response = urllib.request.urlopen(req)
    # 读取结果
    response_head = response.headers['Content-Type']
    print("ttv2")
    print(time.time())
    if(response_head == "audio/mpeg"):
        out_file = open(OUTPUT_FILE, 'wb')
        data = response.read() # a 'bytes' object
        out_file.write(data)
        out_file.close()
        return '{"code":"0"}'
    else:
        return (response.read().decode('utf8'))

# callback 执行的方法
def __returnRusult(msg):
    global result
    result=msg





