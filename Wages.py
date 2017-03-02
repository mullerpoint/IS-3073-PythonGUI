#!/usr/bin/env python

#import
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql #import the wage gui app
from WageSearcherUI import Ui_WageSearcher

#controller class
class wageSearcherProgram(Ui_WageSearcher):
    def __init__(self, window):
        Ui_WageSearcher.__init__(self)
        self.setupUi(window)

        #connect Search button with function
        self.searchButton.clicked.connect(self.searchNow)

        #connect Quit button to Quit
        self.quitButton.clicked.connect(self.quitNow)

        #testing
        #self.spinBoxMaxSalary.valueChanged.connect

    def searchNow(self):
        #code to search for salaries in the range

        #temp code to show inputs
        tempstr = str(self.spinBoxMinSalary.value()) + " " + str(self.spinBoxMaxSalary.value())
        self.outputBox.setText(tempstr)

    def quitNow(self):
        print("something")
        sys.exit(app.exec_())


def createConnection():
    #db = QSqlDatabase.addDatabase("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:/Users/gmull_000/Documents/Python Projects/Qt GUI Testing/NW Testing/northwind testing 1.accdb")
    #db.setDatabaseName("C:/Users/gmull_000/Documents/Python Projects/Qt GUI Testing/NW Testing/northwind testing 1.accdb")
    #if not db.open():
        #print('failed')
        #return False

    filename = "C:/Users/gmull_000/Documents/Python Projects/Qt GUI Testing/NW Testing/northwind testing 1.accdb"
    #create = not QFile.exists(filename)
    db = QSqlDatabase.addDatabase("QODBC")
    db.setConnectOptions("SQL_ATTR_TRACE=SQL_OPT_TRACE_OFF")
    db.setDatabaseName("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};FIL={MS Access};DBQ=%s" % filename)
    if not db.open():
        print("failed")
        db.close()
        sys.exit(1)


from PyQt5.QtSql import QSqlDatabase, QSqlQuery
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    masterWindow = QtWidgets.QMainWindow()
    prog = wageSearcherProgram(masterWindow)
    #createConnection()
    masterWindow.show()
    sys.exit(app.exec_())

    #db = QSqlDatabase.addDatabase( 'QODBC' )
    #db.setDatabaseName('C:\Users\gmull_000\Documents\Python Projects\Qt GUI Testing\NW Testing\northwind testing 1.accdb')
