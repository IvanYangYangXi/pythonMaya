#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/25/2018, 9:52:55 AM

import maya.mel as mel;
import maya.cmds as cmds;
print('aa')
mel.eval('python("import maya.cmds");');
class SphereWindow_eval(object):
    def __init__(self):
        self.win = 'arSphereSample';
        if cmds.window(self.win, exists = True):
            cmds.deleteUI(self.win);
        self.win = cmds.window(
            self.win,
            widthHeight = (300,100),
            menuBar = True,
        );
        self.menu = cmds.menu(label = 'Create',);
        cmds.menuItem(
            label = 'P Cube',
            command = 'maya.cmds.polyCube()',
        );
        cmds.menuItem(
            label = "P Sphere",
            command = 'maya.cmds.polySphere()'
        );
        cmds.showWindow();

win = SphereWindow_eval();


print('3')