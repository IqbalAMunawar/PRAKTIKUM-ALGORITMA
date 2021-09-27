# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:59:53 2021

@author: Iqbal

NAMA :IQBAL.A.MUNAWAR
NIM : 064002100007

"""
import math

a = float(input("Masukan nilai a : "))
b = float(input("Masukan nilai b : "))

hasil = a + b
print("Jumlah a ditambah b adalah",hasil)

hasil = a - b
print("Selisih antara a dan b adalah",abs(hasil))

hasil = a * b
print("Jumlah a dikali b adalah",hasil)

hasil = a % b
print("Jumlah sisa pembagian a dan b",hasil)

hasil = a / b
print("Jumlah pembagian a dan b",hasil)

hasil = math.log10(a)
print("Jumlah log a",hasil)

hasil = a ** b
print("Jumlah dari a pangkat b",hasil)
