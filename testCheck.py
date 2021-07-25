	# def openDB(self):
	# 	#self db = QtSql.SqlDatabase("QSQLITE")
	# 	self.db.setDatabaseName("data.sqlite")
	# 	if not self.db.open():
	# 		print("Error")
	# 	self.query = QtSql.SqlQuery()
	#
	# def checkUser(self):
	# 	username1 = self.lineEdit.text()
	# 	password1 = self.lineEdit.text()
	# 	print(username1, password1)
	# 	self.query.exec_("select * from userdata where username = '%s' and password = '%s;"(username1, password1))
	# 	if self.query.value("username") != None and self.query.value("password") != None:
	# 		print("Login Successful")
	# 	else:
	# 		print("Login failed")
