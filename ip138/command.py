#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-11 23:01:51
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)
# @Link    : https://github.com/KellyHwong/ip138
# @Version : $0.0.0$

from __future__ import unicode_literals, print_function

from ip138.cmdline import banner, cmd_parser
from ip138.logger import logger
from ip138.ip138 import ip138


def main():
    banner()
    # ip = "172.217.161.164"
    options = cmd_parser()
    ip_info = ip138(options.ip)
    for _ in ip_info.keys():
        logger.info("%s: %s" % (_, ip_info[_]))


if __name__ == '__main__':
    main()
