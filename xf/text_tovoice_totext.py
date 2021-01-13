import base64
import json
import hashlib
import urllib.request
import urllib.parse
import time

# 文字转音频
def change(TEXT):
    print("2")
    print(time.time())
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
    print("3")
    print(time.time())
    req = urllib.request.Request(api_url, data=body_utf8, headers=header)
    response = urllib.request.urlopen(req)
    print("4")
    print(time.time())
    # 读取结果
    response_head = response.headers['Content-Type']
    if(response_head == "audio/mpeg"):
        data = response.read() # a 'bytes' object
        nextChange(data)
    else:
        return (response.read().decode('utf8'))

# 音频转文字
def nextChange(file_content):
    # f = open(INPUT_FILE, 'rb')  # rb表示二进制格式只读打开文件
    # file_content = f.read()
    # # file_content 是二进制内容，bytes类型
    # # 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
    # # 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
    # # 以Unicode表示的str通过encode()方法可以编码为指定的bytes
    base64_audio = base64.b64encode(file_content)  # base64.b64encode()参数是bytes类型，返回也是bytes类型
    body = urllib.parse.urlencode({'audio': base64_audio})
    url = 'http://api.xfyun.cn/v1/service/v1/iat'
    api_key = '362edff2073436726fab819822a344cf' #API_KEY
    param = {"engine_type": "sms16k", "aue": "raw"}
    x_appid = '5be0fe46' # APP_ID
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))  # 改('''')
    # 这是3.x的用法，因为3.x中字符都为unicode编码，而b64encode函数的参数为byte类型，
    # 所以必须先转码为utf-8的bytes
    x_param = str(x_param, 'utf-8')
    x_time = int(int(round(time.time() * 1000)) / 1000)
    x_checksum = hashlib.md5((api_key + str(x_time) + x_param).encode('utf-8')).hexdigest()  # 改
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    # 不要忘记url = ??, datas = ??, headers = ??, method = ?? 中的“ = ”，这是python3
    print("5")
    print(time.time())
    req = urllib.request.Request(url=url, data=body.encode('utf-8'), headers=x_header, method='POST')
    result = urllib.request.urlopen(req)
    print("6")
    print(time.time())
    result = result.read().decode('utf-8')
    print(result)