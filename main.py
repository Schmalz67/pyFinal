
import sqlite3
from sqlite3 import Error
from gui import *

""" create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """


def create_connection():

    conn = None
    try:
        conn = sqlite3.connect('login.db')
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


def user_to_str(user):
    return "Username: " + user[0] + " Password: " + user[1] + " Balance: " + str(user[2])


def get_user():
    get_user_query = """
        SELECT * FROM users
    """

    if conn is not None:
        c = conn.cursor()
        return c.execute(get_user_query).fetchall()
    else:
        print("bad conn")

#w = Text(tkWindow, height=1, width=50)
#w.grid(row=0, column=4, rowspan=5)


def insert_user():
    create_user_query = """INSERT INTO users (name, password, balance) VALUES (%s, %s, 1000)"""

    if conn is not None:
        c = conn.cursor()
        # c.execute(create_user_query, (username.get(), password.get()))
        c.execute(create_user_query % ('admin', 'password'))
    else:
        print("bad conn")


def read_one_user():
    read_user = """
        SELECT * FROM users WHERE name = ? AND password = ?
    """

    user = ""

    if conn is not None:
        c = conn.cursor()
        # user = user_to_str(c.execute(read_user, (username.get(), password.get())).fetchone())
        user = user_to_str(c.execute(read_user, ('admin', 'password')).fetchone())
    else:
        print("bad conn")

    w.delete("1.0", "end")

    w.insert(INSERT, user)


conn = create_connection()


def main():
    sql_create_user_database = """
        CREATE TABLE users (
            name varchar(255),
            password varchar(255),
            balance int
        )
    """

    # create tables
    if conn is not None:
        # create projects table
        create_table(sql_create_user_database)
        conn.commit()

    else:
        print("Error! cannot create the database connection.")

main()
c = conn.cursor()
c.e
