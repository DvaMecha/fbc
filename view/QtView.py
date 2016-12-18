#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction
from PyQt5.QtGui import QIcon


class QtView(QMainWindow):

    # noinspection PyArgumentList
    def __init__(self, eventsmod: object):
        super().__init__()
        self.textEdit = QTextEdit()
        self.eventMod=eventsmod
        self.initUI()

    def outPutText(self, t, f=False):
        if f:
            self.textEdit.setText(t)
        else:
            self.textEdit.append(t + '\n')

    # noinspection PyUnresolvedReferences
    def initToobar(self):
        exitAction = QAction(QIcon('res/icon/quit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        initAction = QAction(QIcon('res/icon/init.png'), 'Start', self)
        initAction.setStatusTip('Get All Data!')
        initAction.triggered.connect(self.eventMod["runCrawl"])

        testAction = QAction(QIcon('res/icon/test.png'), 'Help', self)
        testAction.setStatusTip('!')
        testAction.triggered.connect(self.eventMod["showHelp"])

        listAction = QAction(QIcon('res/icon/list.png'), 'List', self)
        listAction.setStatusTip('Get Teams List!')
        listAction.triggered.connect(self.eventMod["getMatchs"])

        saveAction = QAction(QIcon('res/icon/save.png'), 'Save', self)
        saveAction.setStatusTip('Save to Txt')
        saveAction.triggered.connect(self.eventMod["save"])

        toolbar = self.addToolBar('Tool')
        toolbar.addAction(initAction)
        toolbar.addAction(listAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(testAction)
        toolbar.addAction(exitAction)

    def initUI(self):
        """
        :rtype: object
        """
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.initToobar()
        self.setGeometry(300, 100, 1050, 800)
        self.setWindowTitle('Main window')
        self.setWindowIcon(QIcon('res/icon/icon.png'))
        self.show()
