#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 12:16:52 2025

@author: emir
"""

fiyat = float(input("Ürün fiyatı: "))
indirim_orani = float(input("İndirim oranı (%) : "))
indirimli_fiyat = fiyat * (1 - indirim_orani / 100)
print("İndirimli fiyat:", indirimli_fiyat)
