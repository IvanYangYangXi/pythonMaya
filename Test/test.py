#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/25/2018, 9:52:55 AM

import maya.mel as mel;
import maya.cmds as cmds;


cmds.window()
cmds.shelfTabLayout( 'mainShelfTab', image='smallTrash.png', imageVisible=True )
cmds.shelfLayout( 'Dynamics' )
cmds.setParent( '..' )
cmds.shelfLayout( 'Rendering' )
cmds.setParent( '..' )
cmds.shelfLayout( 'Animation' )
cmds.setParent( '..' )
cmds.showWindow()