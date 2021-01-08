# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 9:53
# @Author  : lance
# @File    : aes_util.py
# @Software: PyCharm
import base64
from Crypto.Util.py3compat import *
from Crypto.Cipher import AES

__all__ = ['ValueError', 'pad', 'unpad']


def pad(data_to_pad, block_size, style='pkcs7'):
    """Apply standard padding.
    :Parameters:
      data_to_pad : byte string
        The data that needs to be padded.
      block_size : integer
        The block boundary to use for padding. The output length is guaranteed
        to be a multiple of ``block_size``.
      style : string
        Padding algorithm. It can be *'pkcs7'* (default), *'iso7816'* or *'x923'*.
    :Return:
      The original data with the appropriate padding added at the end.
    """

    padding_len = block_size - len(data_to_pad) % block_size
    if style == 'pkcs7':
        padding = bchr(padding_len) * padding_len
    elif style == 'x923':
        padding = bchr(0) * (padding_len - 1) + bchr(padding_len)
    elif style == 'iso7816':
        padding = bchr(128) + bchr(0) * (padding_len - 1)
    else:
        raise ValueError("Unknown padding style")
    return data_to_pad.encode() + padding


def unpad(padded_data, block_size, style='pkcs7'):
    """Remove standard padding.
    :Parameters:
      padded_data : byte string
        A piece of data with padding that needs to be stripped.
      block_size : integer
        The block boundary to use for padding. The input length
        must be a multiple of ``block_size``.
      style : string
        Padding algorithm. It can be *'pkcs7'* (default), *'iso7816'* or *'x923'*.
    :Return:
        Data without padding.
    :Raises ValueError:
        if the padding is incorrect.
    """

    pdata_len = len(padded_data)
    if pdata_len % block_size:
        raise ValueError("Input data is not padded")
    if style in ('pkcs7', 'x923'):
        padding_len = bord(padded_data[-1])
        if padding_len < 1 or padding_len > min(block_size, pdata_len):
            raise ValueError("Padding is incorrect.")
        if style == 'pkcs7':
            if padded_data[-padding_len:] != bchr(padding_len) * padding_len:
                raise ValueError("PKCS#7 padding is incorrect.")
        else:
            if padded_data[-padding_len:-1] != bchr(0) * (padding_len - 1):
                raise ValueError("ANSI X.923 padding is incorrect.")
    elif style == 'iso7816':
        padding_len = pdata_len - padded_data.rfind(bchr(128))
        if padding_len < 1 or padding_len > min(block_size, pdata_len):
            raise ValueError("Padding is incorrect.")
        if padding_len > 1 and padded_data[1 - padding_len:] != bchr(0) * (padding_len - 1):
            raise ValueError("ISO 7816-4 padding is incorrect.")
    else:
        raise ValueError("Unknown padding style")
    return padded_data[:-padding_len]


# aes加密
class AESCrypt(object):
    """
    AES加密
    算法密钥=接入密钥KEY,编码=UTF8，
    加密模式(CipherMode)=CBC，
    填充模式(PaddingMode)=PKCS7,
    数据块大小(BlockSize)=128，
    算法的初始化向量(IV)=接入密钥KEY的前16位字符，
    加密后的字节数组转为Base64字符串，
    需要加密的字段会在字段备注中添加‘AES’标记。
    算法：密文=Base64(AES(info, KEY))
    """

    def __init__(self, key, offset):
        """
        构造函数
        :param key:     [string] 私钥
        :param offset:  [string] 偏移量(16位)
        """
        self.key = key.encode('utf-8')
        self.offset = offset.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.block = 16
        self.pad_mode = 'pkcs7'

    def encrypt(self, text):
        """
        加密
        :param text: 明文 v
        :return: 返回位数（v<16:24,16<=v<32:44,32<v<=48:64）
        """
        cryptor = AES.new(self.key, self.mode, self.offset)
        pad_pkcs7 = pad(str(text), self.block, style=self.pad_mode)
        ciphertext = cryptor.encrypt(pad_pkcs7)
        return base64.standard_b64encode(ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.offset)
        text = cryptor.decrypt(base64.standard_b64decode(str(text)))
        return unpad(text, self.block, style=self.pad_mode)


if __name__ == '__main__':
    key = 'be2b0711cd4131e98b4e0c9d9s199f9b'
    offset = 'bb2c0c9sz229de9b'
    aesutils = AESCrypt(key, offset)
    print(aesutils.encrypt(text='wwueidjtisdert32wwueidjtisdert3').decode())
    print(aesutils.decrypt(text='tvaoSuoT5uZmpKGD5BkVriGTobGWlseieYA7JP7I5To=').decode())
