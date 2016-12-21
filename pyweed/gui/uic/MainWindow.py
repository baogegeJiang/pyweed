# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/uic/MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1085, 922)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.getButtonsWidget = QtGui.QWidget(self.centralwidget)
        self.getButtonsWidget.setObjectName(_fromUtf8("getButtonsWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.getButtonsWidget)
        self.horizontalLayout_2.setMargin(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.getWaveformsButton = QtGui.QPushButton(self.getButtonsWidget)
        self.getWaveformsButton.setObjectName(_fromUtf8("getWaveformsButton"))
        self.horizontalLayout_2.addWidget(self.getWaveformsButton)
        self.verticalLayout.addWidget(self.getButtonsWidget)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.mapFrame = QtGui.QFrame(self.splitter)
        self.mapFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mapFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mapFrame.setObjectName(_fromUtf8("mapFrame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.mapFrame)
        self.verticalLayout_2.setMargin(2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.map_canvas = MyQt4MplCanvas(self.mapFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_canvas.sizePolicy().hasHeightForWidth())
        self.map_canvas.setSizePolicy(sizePolicy)
        self.map_canvas.setObjectName(_fromUtf8("map_canvas"))
        self.verticalLayout_2.addWidget(self.map_canvas)
        self.eventAndStationFrame = QtGui.QFrame(self.splitter)
        self.eventAndStationFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.eventAndStationFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.eventAndStationFrame.setObjectName(_fromUtf8("eventAndStationFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.eventAndStationFrame)
        self.horizontalLayout.setMargin(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.eventsFrame = QtGui.QFrame(self.eventAndStationFrame)
        self.eventsFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.eventsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.eventsFrame.setObjectName(_fromUtf8("eventsFrame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.eventsFrame)
        self.verticalLayout_3.setMargin(2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.getEventsButton = QtGui.QPushButton(self.eventsFrame)
        self.getEventsButton.setObjectName(_fromUtf8("getEventsButton"))
        self.verticalLayout_3.addWidget(self.getEventsButton)
        self.eventsTable = QtGui.QTableWidget(self.eventsFrame)
        self.eventsTable.setStyleSheet(_fromUtf8(""))
        self.eventsTable.setShowGrid(False)
        self.eventsTable.setGridStyle(QtCore.Qt.NoPen)
        self.eventsTable.setObjectName(_fromUtf8("eventsTable"))
        self.eventsTable.setColumnCount(0)
        self.eventsTable.setRowCount(0)
        self.verticalLayout_3.addWidget(self.eventsTable)
        self.horizontalLayout.addWidget(self.eventsFrame)
        self.stationsFrame = QtGui.QFrame(self.eventAndStationFrame)
        self.stationsFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.stationsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.stationsFrame.setObjectName(_fromUtf8("stationsFrame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.stationsFrame)
        self.verticalLayout_4.setMargin(2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.getStationsButton = QtGui.QPushButton(self.stationsFrame)
        self.getStationsButton.setStyleSheet(_fromUtf8(""))
        self.getStationsButton.setObjectName(_fromUtf8("getStationsButton"))
        self.verticalLayout_4.addWidget(self.getStationsButton)
        self.stationsTable = QtGui.QTableWidget(self.stationsFrame)
        self.stationsTable.setStyleSheet(_fromUtf8(""))
        self.stationsTable.setShowGrid(False)
        self.stationsTable.setGridStyle(QtCore.Qt.NoPen)
        self.stationsTable.setObjectName(_fromUtf8("stationsTable"))
        self.stationsTable.setColumnCount(0)
        self.stationsTable.setRowCount(0)
        self.verticalLayout_4.addWidget(self.stationsTable)
        self.horizontalLayout.addWidget(self.stationsFrame)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.getWaveformsButton.setText(_translate("MainWindow", "Get Waveforms", None))
        self.getEventsButton.setText(_translate("MainWindow", "Get Events", None))
        self.getStationsButton.setText(_translate("MainWindow", "Get Stations", None))

from MyQt4MplCanvas import MyQt4MplCanvas