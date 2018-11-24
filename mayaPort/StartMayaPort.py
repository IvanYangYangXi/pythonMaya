#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# StartMayaPort.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : ivan.cgartech.com
# @Date   : 11/23/2018, 11:20:47 PM

import maya.cmds as cmds

# Open new ports

cmds.commandPort(name=":7001", sourceType="mel", echoOutput=True)

cmds.commandPort(name=":7002", sourceType="python", echoOutput=True)
