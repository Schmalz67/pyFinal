from PyQt5 import QtWidgets, QtSql

from PyQt5 import QtWidgets, QtSql

class WebsitesWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WebsitesWidget, self).__init__(parent)
 # this layout_box can be used if you need more widgets
 # I used just one named WebsitesWidget
        layout_box = QtWidgets.QVBoxLayout(self)
 #
        my_view = QtWidgets.QTableView()
 # put viwe in layout_box area
        layout_box.addWidget(my_view)
 # create a table model
        my_model = QtSql.QSqlTableModel(self)
        my_model.setTable("Username")
        my_model.select()
 #show the view with model
        my_view.setModel(my_model)
        my_view.setItemDelegate(QtSql.QSqlRelationalDelegate(my_view))
