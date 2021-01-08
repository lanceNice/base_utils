#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json
import asyncio
import aiohttp


async def json_general_get(url, headers=None):
    """
    通用get请求
    :param url: 请求的url
    :param headers: 请求头信息
    :return:
    """
    async with aiohttp.ClientSession() as session:
        if headers:
            async with session.get(url, headers=headers) as resp:
                try:
                    return await resp.json()
                except Exception as e:
                    return str(e)
        else:
            async with session.get(url) as resp:
                try:
                    return await resp.json()
                except Exception as e:
                    return str(e)


async def json_general_post(url, req_data, header_data):
    """
        post请求
        :param header_data: 请求头信息
        :param url: 请求地址
        :param req_data: body数据体 (dict格式)
        :return:
    """
    async with aiohttp.ClientSession() as session:
        req_data = json.dumps(req_data)
        if header_data:
            header_data.update({'Content-Type': 'application/json'})
            async with session.post(url, data=req_data, headers=header_data, verify_ssl=False) as resp:
                try:
                    return await resp.json()
                except Exception as e:
                    return str(e)
        else:
            async with session.post(url, data=req_data, verify_ssl=False) as resp:
                try:
                    return await resp.json()
                except Exception as e:
                    return str(e)


async def json_general_put(url, req_data, header_data):
    """
        put请求
        :param header_data: 请求头信息
        :param url: 请求地址
        :param req_data: body数据体 (dict格式)
        :return:
        """
    async with aiohttp.ClientSession() as session:
        req_data = json.dumps(req_data)
        if header_data:
            header_data.update({'Content-Type': 'application/json'})
            async with session.put(url, data=req_data, headers=header_data) as resp:
                try:
                    return await resp.json()
                except Exception as e:
                    return str(e)
        else:
            async with session.put(url, data=req_data) as resp:
                try:
                    return await resp.json()
                except Exception as e:
                    return str(e)


async def json_general_delete(url: str, header_data: dict) -> object:
    """
        沃土delete请求
        :param url: 请求地址
        :param header_data: body数据体 (dict格式)
        :return:
        """
    async with aiohttp.ClientSession() as session:
        if header_data:
            header_data.update({'Content-Type': 'application/json'})
            async with session.delete(url, headers=header_data) as resp:
                try:
                    return await resp.json()
                except Exception as e:
                    return str(e)
        else:
            async with session.delete(url) as resp:
                try:
                    return await resp.json()
                except Exception as e:
                    return str(e)


async def fromdata_general_post(url, req_data):
    """
        post请求
        :param header_data: 请求头信息
        :param url: 请求地址
        :param req_data: body数据体 (dict格式)
        :return:
    """
    async with aiohttp.ClientSession() as session:
        req_data = aio_dict_tuple(req_data)
        form_data = aiohttp.FormData()
        form_data.add_fields(*req_data)
        response = await session.post(url, data=form_data)
        print(await response.text())


def aio_dict_tuple(req_data):
    final_data = []

    for key, value in req_data.items():
        temporary_data = (key, value)
        final_data.append(temporary_data)
    return tuple(final_data)


async def do():
    url = "https://api.yooticloud.cn/middle/company_screen/device_status"

    print(await json_general_get(url))

    # url = "http://192.168.0.134:2873/api/v2/auth"
    # req_data = {
    #     "login": "15738854222",
    #     "password": "open11111",
    #     "db": "fjha"
    # }
    # await fromdata_general_post(url, req_data)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(do())
    loop.run_until_complete(task)
    loop.close()
