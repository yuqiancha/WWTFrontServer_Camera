# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(982, 576)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(240, 70, 731, 491))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 961, 68))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_ReScan = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ReScan.setObjectName("pushButton_ReScan")
        self.verticalLayout_9.addWidget(self.pushButton_ReScan)
        self.pushButton_handleAll = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_handleAll.setObjectName("pushButton_handleAll")
        self.verticalLayout_9.addWidget(self.pushButton_handleAll)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_Reset = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.verticalLayout_5.addWidget(self.pushButton_Reset)
        self.pushButton_LockDownRest = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_LockDownRest.setObjectName("pushButton_LockDownRest")
        self.verticalLayout_5.addWidget(self.pushButton_LockDownRest)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_EnableAlarm = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_EnableAlarm.setObjectName("pushButton_EnableAlarm")
        self.verticalLayout_2.addWidget(self.pushButton_EnableAlarm)
        self.pushButton_DisableAlarm = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_DisableAlarm.setObjectName("pushButton_DisableAlarm")
        self.verticalLayout_2.addWidget(self.pushButton_DisableAlarm)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_LockUp = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_LockUp.setObjectName("pushButton_LockUp")
        self.verticalLayout_3.addWidget(self.pushButton_LockUp)
        self.pushButton_LockDown = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_LockDown.setObjectName("pushButton_LockDown")
        self.verticalLayout_3.addWidget(self.pushButton_LockDown)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_LightOn = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_LightOn.setObjectName("pushButton_LightOn")
        self.verticalLayout_4.addWidget(self.pushButton_LightOn)
        self.pushButton_LightOff = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_LightOff.setObjectName("pushButton_LightOff")
        self.verticalLayout_4.addWidget(self.pushButton_LightOff)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_LockPowerOn = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_LockPowerOn.setObjectName("pushButton_LockPowerOn")
        self.verticalLayout.addWidget(self.pushButton_LockPowerOn)
        self.pushButton_LockPowerOff = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_LockPowerOff.setObjectName("pushButton_LockPowerOff")
        self.verticalLayout.addWidget(self.pushButton_LockPowerOff)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_ChaoShengTest = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ChaoShengTest.setObjectName("pushButton_ChaoShengTest")
        self.verticalLayout_7.addWidget(self.pushButton_ChaoShengTest)
        self.pushButton_QuitTest = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_QuitTest.setObjectName("pushButton_QuitTest")
        self.verticalLayout_7.addWidget(self.pushButton_QuitTest)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_4GReboot = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4GReboot.setObjectName("pushButton_4GReboot")
        self.verticalLayout_6.addWidget(self.pushButton_4GReboot)
        self.pushButton_webstatus = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_webstatus.setObjectName("pushButton_webstatus")
        self.verticalLayout_6.addWidget(self.pushButton_webstatus)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_8.addWidget(self.comboBox)
        self.pushButton_exit = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout_8.addWidget(self.pushButton_exit)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.textBrowser_Cam = QtWidgets.QTextBrowser(Form)
        self.textBrowser_Cam.setGeometry(QtCore.QRect(10, 70, 221, 491))
        self.textBrowser_Cam.setObjectName("textBrowser_Cam")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_ReScan.setText(_translate("Form", "重新扫描"))
        self.pushButton_handleAll.setText(_translate("Form", "切换统一操作"))
        self.pushButton_Reset.setText(_translate("Form", "复位"))
        self.pushButton_LockDownRest.setText(_translate("Form", "降锁休眠"))
        self.pushButton_EnableAlarm.setText(_translate("Form", "报警"))
        self.pushButton_DisableAlarm.setText(_translate("Form", "取消报警"))
        self.pushButton_LockUp.setText(_translate("Form", "升锁"))
        self.pushButton_LockDown.setText(_translate("Form", "降锁"))
        self.pushButton_LightOn.setText(_translate("Form", "灯闪烁"))
        self.pushButton_LightOff.setText(_translate("Form", "停止闪烁"))
        self.pushButton_LockPowerOn.setText(_translate("Form", "上电"))
        self.pushButton_LockPowerOff.setText(_translate("Form", "断电"))
        self.pushButton_ChaoShengTest.setText(_translate("Form", "超声测试"))
        self.pushButton_QuitTest.setText(_translate("Form", "退出测试"))
        self.pushButton_4GReboot.setText(_translate("Form", "重启4G路由器"))
        self.pushButton_webstatus.setText(_translate("Form", "WebServiceOff"))
        self.pushButton_exit.setText(_translate("Form", "Exit"))

