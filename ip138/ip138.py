#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-11 23:44:26
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)
# @Link    : https://github.com/KellyHwong/ip138
# @Version : $0.0.0$

import requests
from bs4 import BeautifulSoup
from ip138.constant import HEADERS


def ip138(ip):
    '''
    ip138 IP geometry infomation API
    :@param ip (str): query ip address (str)
    :@return (dict): 
    '''
    url = "http://www.ip138.com/ips1388.asp?ip=%s&action=2" % ip
    query_html = requests.get(url, headers=HEADERS).content
    query_html = query_html.decode("gb2312")
    with open("debug.html", "w", encoding="gb2312") as f:
        f.write(query_html)
    query_soup = BeautifulSoup(query_html, "lxml")
    # div_info_block = query_soup.find("div", {"id": "info-block"})
    ul1 = query_soup.find("ul", {"class": "ul1"})
    li_items = ul1.find_all("li")
    ret = dict()
    for item in li_items:
        _ = item.text.split("：")  # 这个是中文冒号
        ret[_[0]] = _[1]
    return ret
