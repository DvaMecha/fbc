#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class QtView(QMainWindow):

    # noinspection PyArgumentList
    def __init__(self, eventmod):
        super().__init__()
        self.eventMod = eventmod
        self.initUI()

    def initMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAction)
        return menubar

    def outPutText(self, t, f=False):
        if f:
            self.textEdit.setText(t)
        else:
            self.textEdit.append(t + '\n')

    def initToobar(self):
        exitAction = QAction(QIcon('res/icon/quit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        initAction = QAction(QIcon('res/icon/init.png'), 'Start', self)
        initAction.setStatusTip('Get All Data!')
        initAction.triggered.connect(lambda: self.eventMod['getDatas']("odds"))

        testAction = QAction(QIcon('res/icon/test.png'), 'Help', self)
        testAction.setStatusTip('!')
        testAction.triggered.connect(self.eventMod['showHelp'])

        listAction = QAction(QIcon('res/icon/list.png'), 'List', self)
        listAction.setStatusTip('Get Teams List!')
        listAction.triggered.connect(lambda: self.eventMod['getDatas']("list"))

        saveAction = QAction(QIcon('res/icon/save.png'), 'Save', self)
        saveAction.setStatusTip('Save to Txt')
        saveAction.triggered.connect(self.eventMod['save'])

        toolbar = self.addToolBar('Tool')
        toolbar.addAction(initAction)
        toolbar.addAction(listAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(testAction)
        toolbar.addAction(exitAction)

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.initMenu()
        self.initToobar()
        self.setGeometry(300, 100, 1050, 800)
        self.setWindowTitle('Main window')
        self.setWindowIcon(QIcon('res/icon/icon.png'))
        self.show()
