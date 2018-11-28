#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# AppName.py.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/4/2018, 10:01:08 AM


# 程序入口文件


# 从其他目录导入库
import os,sys
print('当前文件位置：',os.path.abspath(__file__)) 
print("获得文件目录的上层目录：",os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 将当前文件的所在目录的上层目录添加到系统路径
import core # import 文件夹名字 == run __init__.py  ; 导入包

core.main.main_test() # 调用main的函数：目录.文件名.函数名()