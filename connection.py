from PyQt5 import QtWidgets, QtSql
from PyQt5.QtSql import *

def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(":memory:")
    if not db.open():
        QtWidgets.QMessageBox.critical(None, "Cannot open memory database",
                             "Unable to establish a database connection.\n\n"
                             "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
        return False
    query = QtSql.QSqlQuery()
    #print (os.listdir("."))
    query.exec("DROP TABLE IF EXISTS USERNAME")
    query.exec("CREATE TABLE USERNAME (ID INTEGER PRIMARY KEY NOT NULL, " +     "username VARCHAR(20))")
    query.exec("INSERT INTO USERNAME (username) VALUES('Drew')")
    query.exec("INSERT INTO USERNAME (username) VALUES('Michael')")
    query.exec("INSERT INTO USERNAME (username) VALUES('Billy')")
    query.exec("INSERT INTO USERNAME (username) VALUES('Joe')")
    query.exec("INSERT INTO USERNAME (username) VALUES('Jared')")
    return True
