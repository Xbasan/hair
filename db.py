import sqlite3


def db(recording):
    connection = sqlite3.connect('./db/hair_db')
    cursor = connection.cursor()

    cursor.execute(f'INSERT INTO publications (image, coment)'
                   f'VALUES ("{recording[0]}", "{recording[1]}")')

    cursor.execute('SELECT * FROM publications')

    results = cursor.fetchall()
    print(results)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    db(['6_publication/2023-07-27_08-24-27_UTC_1.jpg','КОМЕНТАРИЙ'])
