import sqlite3

connect = sqlite3.connect('database.db')

connect.execute(
	'CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT, email TEXT, city TEXT, country TEXT, phone TEXT)')


#  CREATE

def add_participent_to_DB(data):

    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO PARTICIPANTS \
        (name,email,city,country,phone) VALUES (?,?,?,?,?)",
                    (data['name'], data['email'], data['city'], data['country'], data['phone']))
        connection.commit()

# READ

def load_participents():
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM PARTICIPANTS')
 
        data = cursor.fetchall()
        return data
    
def load_participent(name):
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM PARTICIPANTS WHERE name = ?', (name,))
 
        data = cursor.fetchall()
        if(len(data) == 0):
            return None
        
        return data[0]


# UPDATE 

def update_participant(name, updates):
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()

        update_query = "UPDATE PARTICIPANTS SET "
        update_data = []
        
        # List of fields that can be updated
        allowed_fields = ["email", "city", "country", "phone"]

        for field, value in updates.items():
            if field in allowed_fields:
                update_query += f"{field} = ?, "
                update_data.append(value)

        if not update_data:
            return False  # No valid fields to update
        
        update_query = update_query.rstrip(', ') + " WHERE name = ?"
        update_data.append(name)

        cursor.execute(update_query, update_data)
        connection.commit()
        return True

# DELETE

def delete_participant(name):
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM PARTICIPANTS WHERE name = ?', (name,))
        connection.commit()