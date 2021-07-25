from PyQt5 import QtWidgets, QtSql
from connection import createConnection
# this will import any classes from PyQt5_view script
from view import WebsitesWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.MDI = QtWidgets.QMdiArea()
        self.setCentralWidget(self.MDI)

        SubWindow1 = QtWidgets.QMdiSubWindow()
        SubWindow1.setWidget(WebsitesWidget())
        self.MDI.addSubWindow(SubWindow1)
        SubWindow1.show()
 # you can add more widgest
        #SubWindow2 = QtWidgets.QMdiSubWindow()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    if not createConnection():
        print("not connect")
        sys.exit(-1)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
