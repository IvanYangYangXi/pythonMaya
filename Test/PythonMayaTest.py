#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PythonMayaTest.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : ivan.cgartech.com
# @Date   : 11/24/2018, 9:26:54 AM

import maya.cmds as cmds;

# cmds.deleteUI(win,window=True)
win = cmds.window(
    'arg',
    title='My First Window',
    widthHeight= (546,350)
)
cmds.showWindow(win)

print('aaab')