#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# std_GUI01.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/25/2018, 4:48:19 PM


import maya.cmds as cmds
import os

# # 临时添加环境变量
# import sys
# sys.path.append('E:\\YJL_2018\\pythonMaya\\study') 
# print(sys.path) # sys.path 环境变量

# 1 按钮和文字

def printer(aa):
    print(aa)

## 1.1 按钮 button
cmds.window(title="ButtenTest",w=300,)
cmds.columnLayout() # 垂直排列
cmds.button(
    label = 'Hello World',  # 添加按钮标签
    w = 100, h = 100, # 添加宽度和高度参数
    command = 'print("Hello World")' # 使用command参数执行些命令，比如打印一句话
)
cmds.button(
    label = 'do Func',
    bgc = [1, 0, 1], # bgc就是BackGroundColor
    command = 'printer(123)', # 使用command参数执行一个函数
    # 更多的参数请参考帮助文档。
)
cmds.showWindow()

## 1.2 文字 text
cmds.window(title="Text Test",w=300,)
cmds.columnLayout()
cmds.text(
    label="Hello World",
    fn = 'boldLabelFont', # 字体-黑体
)
cmds.showWindow()

# 2 输入框 textField
cmds.window(title="textField Test",w=300,)
cmds.columnLayout()
a = cmds.textField(tx='default') # 文本输入框，我们定义了默认文本default
cmds.button(
    label = 'print Text',
    command = 'b=cmds.textField(a, q=1, tx=1);print(b)', # 获取并打印文本，cmds.textField（a, q = 1, tx = 1）表示询问实例对象a关于参数tx的值
);
cmds.showWindow()

# 3 选项菜单 optionMenu
cmds.window(title="optionMenu Test",w=300,)
cmds.columnLayout()
o = cmds.optionMenu(label='default') # 创建选项菜单
cmds.menuItem(label='cat') # 加入菜单内容cat
cmds.menuItem(label='dog') # 加入菜单内容dog
cmds.button(
    label = 'print Option',
    command = 'b=cmds.optionMenu(o, q=1, v=1);print(b)', # 获取菜单中的值;cmds.optionMenu（o, q = 1, v = 1）的意思就是询问实例o的v参数，v参数就是value的意思，也就是指当前optionMenu的值。
);
cmds.showWindow()

# 4 列表框 textScrollList (获取文件列表)
def changeList(): # 定义函数
    cdir = cmds.optionMenu(op, v=1, q=1) # 询问op选项菜单的V值，也就是当前所选的内容，把这个值给cdir
    myls = os.listdir(cdir)
    cmds.textScrollList(directoryList, e=1, removeAll=1) # 删除directoryList列表里的所有内容，注意：我们这里用到了参数e，说明我们的操作是“编辑”directoryList实例
    cmds.textScrollList(directoryList, e=1, append=myls) # append一个列表myls，mysl是cdir目录下的所有文件名和文件夹名组成的列表

cmds.window(title="textScrollList Test", w=300,)
cmds.columnLayout()
op = cmds.optionMenu(label='Directory', cc='changeList()') # 创建选项菜单，CC就是changeCommand的缩写。这个参数的在你改变选项菜单中的选项时起作用，也就是说：一旦你改变菜单中的选项，CC后面的语句就会执行。
cmds.menuItem(label='C:\\') # 
cmds.menuItem(label='D:\\') # 
# 定义列表，这个列表可以显示8行，一旦超过8行就会自动出现滚动条。append的值是这个列表的初始信息（这个参数需要列表作为其数据类型）
directoryList = cmds.textScrollList(numberOfRows=8, append=os.listdir('C:\\')) # os.listdir('C:\\')，返回的是一个列表，其中包含了C盘根目录下的文件名和文件夹名。
cmds.showWindow()

# 5 进度条 progressBar
cmds.window(title="ProgressBar Test", w=300,)
cmds.columnLayout()
bar = cmds.progressBar(maxValue=10, width=300) # 定义了一个进度条：最大值10，宽300。
cmds.button(
    label='Progress Bar Test',
    command='cmds.progressBar(bar, edit=True, step=1)' # 每执行一次，进度条前进一格
)
cmds.showWindow()

# 6 勾选框 checkBox
#
# 以下定义3个初始值
v1 = 0
v2 = 0
v3 = 0
def checkValueTest():
    print ("value 1 is" + str(v1))
    print ('value 2 is' + str(v2))
    print ('value 3 is' + str(v3))
    print ('--------------------')
cmds.window(title='CheckBox Test', w=300)
cmds.columnLayout(adjustableColumn=True)
# 三个勾选框
cmds.checkBox(label='value 1', align='left', v=v1, onCommand='v1=1', offCommand='v1=0')
cmds.checkBox(label='value 2', align='left', v=v2, onCommand='v2=2', offCommand='v2=0')
cmds.checkBox(label='value 3', align='left', v=v3, onCommand='v3=3', offCommand='v3=0')
cmds.button(label='CheckedValue', command='checkValueTest()')
cmds.showWindow()