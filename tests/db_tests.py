import sqlite3


def test_data_addition():

    connection = sqlite3.connect("./passman.db")

    cursor = connection.cursor()

    passwords = [
                ("hh.ee", "haha", "12345678", "this password's description"),
                ("asdfg.com", "asdfg", "123412", "other description")
            ]

    cursor.executemany("INSERT INTO passman (password_address, password_name, password, password_description) VALUES (?,?,?,?)", passwords)

    connection.commit()

    print("Data added.")

    connection.close()


def test_data_presence():

    connection = sqlite3.connect("./passman.db")

    cursor = connection.cursor()

    for row in cursor.execute("SELECT * FROM password;"):

        print(row)

    connection.close()

# test_data_addition()

test_data_presence()