import math
from ctypes import c_int32
from typing import List

def charAt(msg, idx):
    return 0 if idx >= len(msg) else ord(msg[idx])


def s(a, b):
    c = len(a)
    v = []
    for i in range(0, c, 4):
        v.append(
            charAt(a, i) | charAt(a, i + 1) << 8 | charAt(a, i + 2) << 16 | charAt(a, i + 3) << 24
        )
    if b:
        v.append(c)
    return v


def l(a, b):
    d = len(a)
    c = (d - 1) << 2
    if b:
        m = a[d - 1]
        if (m < c - 3) or (m > c):
            return None
        c = m
    for i in range(0, d):
        a[i] = chr(a[i] & 0xff) + chr(a[i] >> 8 & 0xff) + chr(a[i] >> 16 & 0xff) + chr(
            a[i] >> 24 & 0xff)
    if b:
        return ''.join(a)[0:c]
    else:
        return ''.join(a)

def xEncode(str, key):
    if str == "":
        return ""
    v = s(str, True)
    k = s(key, False)
    if len(k) < 4:
        k = k + [0] * (4 - len(k))
    n = len(v) - 1
    z = v[n]
    y = v[0]
    c = 0x86014019 | 0x183639A0
    m = 0
    e = 0
    p = 0
    q = math.floor(6 + 52 / (n + 1))
    d = 0
    while 0 < q:
        d = d + c & (0x8CE0D9BF | 0x731F2640)
        d = d & 0xFFFFFFFF
        e = d >> 2 & 3
        e = e & 0xFFFFFFFF
        p = 0
        while p < n:
            y = v[p + 1] & 0xFFFFFFFF
            m = z >> 5 ^ y << 2
            m = m + (((y >> 3)&0xFFFFFFFF ^ (z << 4)&0xFFFFFFFF)&0xFFFFFFFF ^ (d ^ y))
            m = m & 0xFFFFFFFF
            m = m + (k[(p & 3) ^ e] ^ z)
            m = m & 0xFFFFFFFF
            v[p] = v[p] + m & (0xEFB8D130 | 0x10472ECF)
            v[p] = v[p] & 0xFFFFFFFF
            z = v[p]
            z = z & 0xFFFFFFFF
            p = p + 1
        y = v[0]&0xFFFFFFFF
        m = z >> 5 ^ y << 2
        m = m & 0xFFFFFFFF
        z = z & 0xFFFFFFFF
        m = m + ((y >> 3 ^ z << 4) ^ (d ^ y))
        m = m & 0xFFFFFFFF
        m = m + (k[(p & 3) ^ e] ^ z)
        m = m & 0xFFFFFFFF
        v[n] = v[n] + m & (0xBB390742 | 0x44C6F8BD)
        v[n] = v[n] & 0xFFFFFFFF
        z = v[n]
        q = q - 1
    return l(v, False)
