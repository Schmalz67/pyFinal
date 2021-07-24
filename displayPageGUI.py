import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import Qt
import pandas as pd
from gui import *
from main import *
class balance(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Balance')
		self.resize(500, 200)

		layout = QGridLayout()

		label_balance = QLabel('<font size="4"> Balance </font>')
		self.lineEdit_balance = QLineEdit()

		self.lineEdit_balance.setPlaceholderText('You have money')
		layout.addWidget(label_balance, 1, 0)
		layout.addWidget(self.lineEdit_balance, 1, 1)

		self.button = QPushButton('&Load Data')
		self.button.clicked.connect(self.loadExcelData)
		layout.addWidget(self.button)

		self.setLayout(layout)

		self.table = QTableWidget()
		layout.addWidget(self.table)

	def loadExcelData(self, excel_file_dir, worksheet_name):
		df = pd.read_excel(excel_file_dir, worksheet_name)
		if df.size == 0:
			return

		df.fillna('', inplace=True)
		self.table.setRowCount(df.shape[0])
		self.table.setColumnCount(df.shape[1])
		self.table.setHorizontalHeaderLabels(df.columns)

		for row in df.iterrows():
			print(row)
			break


#	def check_password(self):
#		msg = QMessageBox()
#
#		if self.lineEdit_username.text() == 'admin' and self.lineEdit_password.text() == 'password':
#			msg.setText('Welcome Drew, you have $3,094.98 in your account. ')
#			msg.exec_()
#			app.quit()
#		else:
#			msg.setText('Incorrect Password')
#			msg.exec_()



if __name__ == '__main__':
	app = QApplication(sys.argv)

	excel_file_path = 'banking.xlsx'
	worksheet_name = 'Balancesheet'
	form = balance()
	form.show()

	sys.exit(app.exec_())
