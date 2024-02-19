# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:58:40 2020

@author: vicky
"""

import json
import pandas as pd

Tom = pd.read_csv("Tom_csv all.csv")
filename = []
LEX, LEY,REX, REY, NX, NY, LMX, LMY, RMX, RMY = [], [], [], [], [], [], [], [], [], []

index = 0
for i in Tom["region_shape_attributes"]:
    mark = json.loads(i)
    if mark == {}:
        break
    cx = mark['cx']
    cy = mark['cy']
    if (index)%5 == 0:
        filename.append(Tom["filename"][index])
        if (cx <= 10 and cy <= 10):
            LEX.append(-1)
            LEY.append(-1)
        else:
            LEX.append(cx)
            LEY.append(cy)
    elif (index)%5 == 1:
        if (cx <= 10 and cy <= 10):
            REX.append(-1)
            REY.append(-1)
        else:
            REX.append(cx)
            REY.append(cy)
    elif (index)%5 == 2:
        if (cx <= 10 and cy <= 10):
            NX.append(-1)
            NY.append(-1)
        else:
            NX.append(cx)
            NY.append(cy)
    elif (index)%5 == 3:
        if (cx <= 10 and cy <= 10):
            LMX.append(-1)
            LMY.append(-1)
        else:
            LMX.append(cx)
            LMY.append(cy)
    elif (index)%5 == 4:
        if (cx <= 15 and cy <= 15):
            RMX.append(-1)
            RMY.append(-1)
        else:
            RMX.append(cx)
            RMY.append(cy)
    index += 1


adjust = pd.DataFrame({
        'filename':filename,
        'LEX':LEX, 
        'LEY':LEY,
        'REX':REX, 
        'REY':REY, 
        'NX':NX, 
        'NY':NY, 
        'LMX':LMX, 
        'LMY':LMY, 
        'RMX':RMX,
        'RMY':RMY
        })

adjust.to_csv("Tom_adj.csv",index=False)
    






