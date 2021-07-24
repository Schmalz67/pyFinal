import sys
from sqlite3 import Error
qtCreatorFile = "pyloginpagegui.ui", "mainpagegui.ui"
from gui import *
#
# """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#
#
def create_connection( db ):

    conn = None
    try:
        conn = sqlite3.connect( db )
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(create_table_sql):
    """ create a table from the create_table_sql statement
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)
#
#
# def user_to_str(user):
#     return "Username: " + user[0] + " Password: " + user[1] + " Balance: " + str(user[2])
#
#
# def get_user():
#     get_user_query = """
#         SELECT * FROM users
#     """
#
#     if conn is not None:
#         c = conn.cursor()
#         return c.execute(get_user_query).fetchall()
#     else:
#         print("bad conn")
#
# #w = Text(tkWindow, height=1, width=50)
# #w.grid(row=0, column=4, rowspan=5)
#
#
def insert_user(username=None, password=None, balance=None):
    #if all(attr is None for attr in [username, password, balance]:
    #     username = username.get()
    #     password = password.get()

    if conn is not None:
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, password, balance))
    else:
        print("bad conn")


def read_one_user(username=None, password=None):
    #if all(attr is None for attr in [username, password]:
    #     username = username.get()
    #     password = password.get()
    "SELECT * FROM users WHERE password='password'"
    if conn is not None:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        return c.fetchone()
    else:
        print("bad conn")
    # read_user = """
    #     SELECT * FROM users WHERE name = ? AND password = ?
    # """
    #
    # user = ""
    #
    # if conn is not None:
    #     c = conn.cursor()
    #     # user = user_to_str(c.execute(read_user, (username.get(), password.get())).fetchone())
    #     user = user_to_str(c.execute(read_user, ('admin', 'password')).fetchone())
    # else:
    #     print("bad conn")
    #
    # w.delete("1.0", "end")
    #
    # w.insert(INSERT, user)
#
#
# conn = create_connection()
#
#
# def main():
#     sql_create_user_database = """
#         CREATE TABLE users (
#             name varchar(255),
#             password varchar(255),
#             balance int
#         )
#     """
#
#     # create tables
#     if conn is not None:
#         # create projects table
#         create_table(sql_create_user_database)
#         conn.commit()
#
#     else:
#         print("Error! cannot create the database connection.")
#
# main()
#c = conn.cursor()
# c.execute("INSERT INTO users VALUES ('admin','password',5000)")

import sqlite3

conn = create_connection('login.db')
create_table("""CREATE TABLE users (
             username text,
             password text,
             balance integer)""")

c = conn.cursor()

insert_user(username='admin', password='password')
insert_user(username='Drew', password='Schmalz')
insert_user(username='Michael', password='Myers')
insert_user(username='Michael', password='Tusic')
insert_user(username='Jared', password='Blatt')
insert_user(username='Steve', password='Ross')
insert_user(username='Billy', password='Madison')
insert_user(username='Captain', password='Morgan')
u = read_one_user(username='Drew', password='Schmalz')
print(u)
# print(c.fetchall())
conn.close()
