#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 12:17:37 2025

@author: emir
"""

u1 = float(input("1. ürün fiyatı: "))
u2 = float(input("2. ürün fiyatı: "))
u3 = float(input("3. ürün fiyatı: "))
toplam = u1 + u2 + u3
if toplam > 200:
    son_fiyat = toplam * 0.90  # %10 indirim
else:
    son_fiyat = toplam
print("Toplam:", toplam, "- Ödenecek:", son_fiyat)