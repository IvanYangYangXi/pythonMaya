#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PythonMayaTest.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : ivan.cgartech.com
# @Date   : 11/24/2018, 9:26:54 AM

import maya.cmds as cmds;
import maya.mel as mel;


# 简单窗口实现
win = cmds.window(
    'arg_window', # 给窗口分配句柄，句柄是唯一的
    title='My First Window',
    widthHeight= (546,350)
)
cmds.showWindow(win)

# 销毁UI
cmds.deleteUI(win,window = True)

#==========================================#

# 通过类创建窗口
class Ar_OptionsWindow(object):
    def __init__(self):
        self.window = 'ar_optionsWindow';
        self.title = 'Options Window';
        self.size = (546,350);
        self.supportsToolAction = False; # 用于禁用某些菜单项
    def create(self):
        if cmds.window(self.window, exists = True): # 窗口是否存在
            cmds.deleteUI(self.window, window = True);
        self.window = cmds.window(
            self.window,
            title = self.title,
            widthHeight = self.size,
            menuBar = True, # 菜单栏标志
        );
        self.commonMenu(); 
        cmds.showWindow();

    # 此方法将添加maya工具中的通用菜单
    def commonMenu(self):
        self.editMenu = cmds.menu(label = 'Edit'); # 创建一个标签为“Edit”的菜单
        # 将maya的普通菜单添加到“Edit”菜单中：Save Settings、Reset Setting、一个分隔符、两个单选按钮
        self.editMenuSave = cmds.menuItem(
            label = 'Save Settings'
        );
        self.editMenuReset = cmds.menuItem(
            label = 'Reset Setting'
        ) ;
        self.editMenuDiv = cmds.menuItem(d= True); # 这是一个分隔符
        self.editMenuRadio = cmds.radioMenuItemCollection(); # radioMenuItemCollection命令，用于在一个单选按钮组件中建立一个菜单项序列
        self.editMenuTool = cmds.menuItem(
            label = 'As Tool',
            radioButton = True,
            enable = self.supportsToolAction # 默认使用之前声明的supportsToolAction数据属性来禁用菜单项
        );
        self.editMenuAction = cmds.menuItem(
            label = 'As Action',
            radioButton = False,
            enable = self.supportsToolAction
        );
        self.helpMenu = cmds.menu(label = 'Help')
        self.helpMenuItem = cmds.menuItem(
            label = 'Help on %s'%self.title,
            command = self.helpMenuCmd, # 指针方式执行事件
        );

    # 添加按钮事件函数,传递指针方式
    def helpMenuCmd(self, *args):
        cmds.launch(web = 'https://ivan.cgartech.com');


testWindow = Ar_OptionsWindow();
testWindow.create()

print('win2')
#===============================================#

# 使用mel模块的 eval() 函数来执行python命令
import maya.cmds as cmds;
import maya.mel as mel;

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

win = SphereWindow_eval()

print('win3')
#======================================================#

'''
# functools模块--partial
from functools import partial;
import maya.cmds as cmds;

class LocatorWindow(object):
    def __init__(self):
        self.win = 'ar_locSample';
        if cmds.window(self.win, exists = True):
            cmds.deleteUI(self.win);
        self.win = cmds.window(
            self.win,
            widthHeight = (300,100),
            menuBar = True,
        );
        self.menu = cmds.menu(
            label = 'Make Location',
        );
        for i in range(5):
            cmds.menuItem(
                label = 'Make %i'%(i+1),
                command = partial(self.makeLocCmd, i+1),
            );
        cmds.showWindow();
    def makeLocCmd(self, numLocators, *args):
        locs = []
        for i in range(numLocators):
            locs.append(
                cmds.spaceLocator(
                    p= [-(numLocators)*0.5 +i+1,0,0]
                )[0]
            );
        cmds.select(locs);        
    
wina = LocatorWindow()

print('win4')
'''

#==============================================#



print('win5')