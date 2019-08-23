#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lqs
# @Date:   2019-08-16 09:35:13
# @Last Modified by:   Lqs
# @Last Modified time: 2019-08-20 10:43:35
import uuid
import base64


def get_mac_address():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return "-".join([mac[e:e+2] for e in range(0,11,2)]).upper()


if __name__ == "__main__":
    print("本机Mac地址:", get_mac_address())