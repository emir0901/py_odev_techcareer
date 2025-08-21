#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 12:18:07 2025

@author: emir
"""

from datetime import date
current_year = date.today().year
dogum_yili = int(input("Doğum yılınız: "))
yasiniz = current_year - dogum_yili
print("Yaşınız:", yasiniz)

if 0 <= yasiniz <= 12:
    print("Çocuksunuz")
elif 13 <= yasiniz <= 17:
    print("Ergensiniz")
else:
    print("Yetişkinsiniz")