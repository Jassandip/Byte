import sqlite3

connection = sqlite3.connect("game.db",check_same_thread=False)
cursor = connection.cursor()

def create_table(table_name):
		cursor.execute(
		"""CREATE TABLE {}(
			pk INTEGER PRIMARY KEY AUTOINCREMENT);""".format(table_name))

def add_column(column_name):
    cursor.execute(
			"""ALTER TABLE {table_name}
				ADD COLUMN {column_name}
			;""".format(
				table_name=table_name,
				column_name=column_name
			)
			))


















connection.commit()
cursor.close()
connection.close()