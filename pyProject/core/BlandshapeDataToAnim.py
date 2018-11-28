#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CastToAnimData.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Date   : 11/23/2018, 10:22:18 AM


import sys,os,json,re

info = {}
frame = {}
keysX = ''
keyX = '' 
frameX = 0
ValueX = 0.0
blandshapeX = ''

# 取字符串中两个符号之间的内容
def textWrapBy(start_str,end_str,textIn = ''):
    startNum = textIn.find(start_str);
    if startNum >=0:
        startNum += len(start_str)
        endNum = textIn.find(end_str, startNum)
        if endNum >= 0:
            return textIn[startNum:endNum].strip()



f = open("data/RecordedSequence_KiteBoyHead_Proto.COPY", 'r', encoding='utf-8')
f_new = open('KiteBoyData.json', 'w', encoding='utf-8')

for line in f:
    if 'Keys=' in line:
        line = line.split('(FloatCurve=(Keys=(')
        for keysX in line:
            blandshapeX = textWrapBy('DisplayName="','"),',keysX)
            keysX = keysX.split('(')
            for keyX in keysX:
                if 'Time' in keyX or 'Value' in keyX:
                    m1 = re.search(r'(Time=) (\d+\.\d+)',keyX)
                    if m1==None:
                        frameX = 0
                    else:
                        frameX = int(float(m1.group(2))*30+0.5)
                    m2 = re.search(r'(Value=) (\d+\.\d+)',keyX)
                    if m2==None:
                        ValueX = 0.0
                    else:
                        ValueX = float(m2.group(2))
                if frameX not in info:
                    info[frameX] = {blandshapeX:ValueX}
                else:
                    frame = info[frameX]
                    frame[blandshapeX] = ValueX

f_new.write(json.dumps(info))
f.close()
f_new.close()


# frame = {
#     blandshapeX:ValueX,
# }
# info = {
#     frameX:{
#         blandshapeX:ValueX,
#     },
#     '0':{
#         'browDownLeft':'0.020302',
#         'browDownRight':'0.223950',
#         'browInnerUp':'0',
#     },
#     '1':{
#         'browDownLeft':'0.020302',
#         'browDownRight':'0.223950',
#         'browInnerUp':'0',
#     },
# }

# jf = open("json_test.json",'w')
# jf.write(json.dumps(info)) 
# jf.close()