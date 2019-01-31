#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# StartMayaPort.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : ivan.cgartech.com
# @Date   : 11/23/2018, 11:20:47 PM

# VS Code
import maya.cmds as cmds;

if not cmds.commandPort(':7001', q = True ):
    cmds.commandPort(name=":7001", sourceType="mel", echoOutput=True)
    cmds.warning('Mel port is open...')
else:
    cmds.commandPort(name = ':7001', cl = 1)
    cmds.warning('Mel port is close...')
if not cmds.commandPort(':7002', q = True):
    cmds.commandPort(name=":7002", sourceType="python", echoOutput=True)
    cmds.warning('Python port is open...')
else:
    cmds.commandPort(name = ':7002', cl = 1)
    cmds.warning('Python port is close...')

# PyCharm
import maya.cmds as cmds
if not cmds.commandPort(':4434', q=True):
    cmds.commandPort(n=':4434')
    cmds.warning('Python port is open...')
else:
    cmds.commandPort(n = ':4434', cl = 1)
    cmds.warning('Python port is close...')