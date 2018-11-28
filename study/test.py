#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/25/2018, 9:52:55 AM

import maya.mel as mel;
import maya.cmds as cmds;


window = cmds.window()
cmds.columnLayout()
cmds.floatSliderButtonGrp( label='Label', field=True, buttonLabel='Button', symbolButtonDisplay=True, columnWidth=(5, 23), image='cmdWndIcon.xpm' )
cmds.showWindow( window )