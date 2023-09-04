# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 09:23:29 2023

@author: marku
"""

sekunder = int(input("Skriv inn antall sekunder:"))
minutter = sekunder//60
timer = minutter//60
dager = timer//24
aar = dager//365
sekunder_rest = sekunder%60
minutter_rest = minutter%60
timer_rest = timer%24
dager_rest = dager%365

if sekunder<60:
    print(f"Dette blir {sekunder} sekund(er).")
    
elif minutter<60:
    print(f"Dette blir {minutter} minutt(er) og {sekunder_rest} sekund(er).")

elif timer<24:
    print(f"Dette blir {timer} time(r), {minutter_rest} minutt(er) og {sekunder_rest} sekund(er).")
    
elif dager<365:
    print(f"Dette blir {dager} dag(er), {timer_rest} tim(er), {minutter_rest} minutt(er) og {sekunder_rest} sekund(er).")
    
else:
    print(f"Dette blir {aar} år, {dager_rest} dag(er), {timer_rest} tim(er), {minutter_rest} minutt(er) og {sekunder_rest} sekund(er).")
    