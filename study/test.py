#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/25/2018, 9:52:55 AM

import maya.mel as mel;
import maya.cmds as cmds;

import os

def chDisk():
    cd = cmds.optionMenu(op, v=1, q=1)
    mls = os.listdir(cd)
    # 列表间的切换
    cmds.textScrollList(directoryList, e=1, removeAll=1)
    cmds.textScrollList(directoryList, e=1, append=mls)    
# 获取任意目录列表    
def click(diskName):
    diskN = os.listdir(diskName)
    listSize = len( diskN )
    for i in range(0, listSize, 1):
        print diskN[i].decode('gbk')        
# 窗体   
cmds.window(title =('cpck').decode('gbk'), height=600)
cmds.columnLayout()
# 添加下拉菜单
op = cmds.optionMenu( label=('mulu').decode('gbk'), cc = "chDisk()")
# 菜单内的选项
cmds.menuItem(label = 'C:\\')
cmds.menuItem(label = 'D:\\')
cmds.menuItem(label = 'F:\\')
# 获取目录列表
dirList1 = cmds.textScrollList(numberOfRows = 1, append = os.listdir("C:\\"))
dirList2 = cmds.textScrollList(numberOfRows = 1, append = os.listdir("D:\\"))
dirList3 = cmds.textScrollList(numberOfRows = 1, append = os.listdir("F:\\"))
# 测试打印F盘列表
click("F:\\")
cmds.showWindow()