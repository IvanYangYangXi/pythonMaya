#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# main.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/4/2018, 10:10:51 AM


# 主函数

import os
import string
import maya.cmds as cmds


qtVersion = cmds.about(qtVersion=True)
print (qtVersion)
if qtVersion.startswith("4") or type(qtVersion) not in [str, unicode]:
    from PySide import QtGui
    from PySide import QtCore
    from PySide import QtWidgets
    from PySide import QtUiTools
else:
    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets
    from PySide2 import QtUiTools


def main_test():
    print("这是主函数")


a = ['3', '11', '1', '31', '12', '13', '2', '21', '22', '23']

# load UI
# dia1 = cmds.loadUI(uiFile='/Volumes/mac2/Git/PythonMaya/ContentBrowser/UI/UI_main.ui')
# cmds.showWindow(dia1)
# uiFile_Path = "/Volumes/mac2/Git/PythonMaya/ContentBrowser/UI/UI_main.ui"
uiFile_Path = "E:\\YJL_2018\\pythonMaya\\ContentBrowser\\UI\\UI_main.ui"

def loadui(uiFile_Path):
    uiFile = QtCore.QFile(uiFile_Path)
    print (uiFile)
    uiFile.open(QtCore.QFile.ReadOnly)
    uiWindow = QtUiTools.QUiLoader().load(uiFile)
    uiFile.close()
    print "load ui"
    return uiWindow


# get workspace
def getWorkspace_Path():
    workspace_Path = cmds.workspace(q=True, rd=True)
    return workspace_Path


# class
class MainWindow(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = loadui(uiFile_Path)
        self.ui.show()
        # UI窗口前置（存在Bug，不建议使用）
        # self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.directoryLabel = QtWidgets.QLabel()
        # treeWidget
        self.ui.treeWidget_folder.clear()
        for i in range(len(a)):
            if len(a[i]) == 1:
                self.root = QtWidgets.QTreeWidgetItem(self.ui.treeWidget_folder)
                self.root.setText(0, a[i])
                self.root.setText(1, a[i])
            elif len(a[i]) == 2:
                child = QtWidgets.QTreeWidgetItem(self.root)
                child.setText(0, a[i])


        # Treeview
        self.model = QtGui.QStandardItemModel()
        self.ui.treeView_folder.setModel(self.model)

        # create slot
        self.ui.actionasSetProject.triggered.connect(self.SetProject)
        self.ui.pushButton.clicked.connect(self.BTTest)
        # 实现 treeWidget item 信号和槽连接
        self.ui.treeWidget_folder.itemClicked['QTreeWidgetItem*', 'int'].connect(self.treeWidget_item_click)

    # add Item
    # def addItem(self):
        # self.model.appendRow(item)

    # menu
    def SetProject(self):
        print ("SetProject")
        cmds.SetProject()
        # self.ui.treeWidget_folder.setRootIndex(getWorkspace_Path)

    # Button
    def BTTest(self):
        print("bt test")
        self.setExistingDirectory()

    # treeWidget item slot
    def treeWidget_item_click(self, item, n):
        print(item.text(n))

    def setExistingDirectory(self):
        options = QtWidgets.QFileDialog.DontResolveSymlinks | QtWidgets.QFileDialog.ShowDirsOnly
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "select", "E:\\YJL_2018\\pythonMaya")


if __name__ == "__main__":
    mainWindow = MainWindow()

