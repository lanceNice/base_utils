# -*- coding: UTF-8 -*-
import json
from xfutils import text_tovoice
from xfutils import voice_totext
from xfutils import text_tovoice_totext
import time


def test1():
    print("---start---")
    start = time.time()
    voiceResultStr = text_tovoice.init('百度传来了喜讯',
                                      "E:/jianguocloud/learn/Python/pythonTest/pythonUtils/datas/chat/output.mp3")
    print(voiceResultStr)
    voiceResultJson = json.loads(voiceResultStr)
    code = voiceResultJson['code']
    if code == "0":
        print("文字转音频成功")
    else:
        print("文字转音频失败：" + voiceResultStr)
    textResultStr = voice_totext.init("E:/jianguocloud/learn/Python/pythonTest/pythonUtils/datas/chat/output.mp3")
    textResultJson = json.loads(textResultStr)
    code = textResultJson['code']
    if code == "0":
        print("音频转文字成功" + textResultStr)
    else:
        print("音频转文字失败：" + textResultStr)
    end = time.time()
    print(end - start)
    print("---end---")


def test2():
    start = time.time()
    text_tovoice_totext.change("摆渡船来")
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    test2()
