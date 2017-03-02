# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wage-Searcher.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WageSearcher(object):
    def setupUi(self, WageSearcher):
        WageSearcher.setObjectName("WageSearcher")
        WageSearcher.resize(682, 468)
        WageSearcher.setMinimumSize(QtCore.QSize(450, 325))
        self.centralwidget = QtWidgets.QWidget(WageSearcher)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.minLabel = QtWidgets.QLabel(self.centralwidget)
        self.minLabel.setObjectName("minLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minLabel)
        self.spinBoxMinSalary = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxMinSalary.setSuffix("")
        self.spinBoxMinSalary.setMinimum(1)
        self.spinBoxMinSalary.setMaximum(10000000)
        self.spinBoxMinSalary.setObjectName("spinBoxMinSalary")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBoxMinSalary)
        self.maxLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxLabel.setObjectName("maxLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxLabel)
        self.spinBoxMaxSalary = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxMaxSalary.setSuffix("")
        self.spinBoxMaxSalary.setMaximum(100000000)
        self.spinBoxMaxSalary.setProperty("value", 9999999)
        self.spinBoxMaxSalary.setObjectName("spinBoxMaxSalary")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxMaxSalary)
        self.verticalLayout.addLayout(self.formLayout)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.verticalLayout.addWidget(self.searchButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.verticalLayout.addWidget(self.quitButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.outputBox = QtWidgets.QTextEdit(self.centralwidget)
        self.outputBox.setReadOnly(True)
        self.outputBox.setObjectName("outputBox")
        self.horizontalLayout.addWidget(self.outputBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        WageSearcher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WageSearcher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 21))
        self.menubar.setObjectName("menubar")
        WageSearcher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WageSearcher)
        self.statusbar.setObjectName("statusbar")
        WageSearcher.setStatusBar(self.statusbar)

        self.retranslateUi(WageSearcher)
        QtCore.QMetaObject.connectSlotsByName(WageSearcher)

    def retranslateUi(self, WageSearcher):
        _translate = QtCore.QCoreApplication.translate
        WageSearcher.setWindowTitle(_translate("WageSearcher", "Wage Searcher"))
        self.minLabel.setText(_translate("WageSearcher", "Minimum Salary"))
        self.maxLabel.setText(_translate("WageSearcher", "Maxumum Salary"))
        self.searchButton.setText(_translate("WageSearcher", "Search"))
        self.quitButton.setText(_translate("WageSearcher", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WageSearcher = QtWidgets.QMainWindow()
    ui = Ui_WageSearcher()
    ui.setupUi(WageSearcher)
    WageSearcher.show()
    sys.exit(app.exec_())

