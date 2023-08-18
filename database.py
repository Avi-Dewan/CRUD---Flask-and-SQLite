import sqlite3

connect = sqlite3.connect('database.db')

connect.execute(
	'CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT, email TEXT, city TEXT, country TEXT, phone TEXT)')


def add_participent_to_DB(data):

    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO PARTICIPANTS \
        (name,email,city,country,phone) VALUES (?,?,?,?,?)",
                    (data['name'], data['email'], data['city'], data['country'], data['phone']))
        connection.commit()


def load_participents():
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM PARTICIPANTS')

        data = cursor.fetchall()
        return data