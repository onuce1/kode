# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 14:51:53 2022

@author: onuca001
"""

def funksjons1():
    tall=1 #lokal variabel
        
    tall==1  #her kan vi bruke variabelen tall
print("5")
        
# her kan vi _ikke_ bruke variabelen volum

eksempel = "utenfor funksjon"  # en global variabel

def funksjon2():
  eksempel = "inni funksjon"  # en lokal variabel 
  print(eksempel)             # skriver ut: inni funksjon

funksjon2()
print(eksempel)  # skriver ut: utenfor funksjon