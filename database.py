import mysql.connector

def open_db():
    return mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='root', password='', database='ma-dbpy',
                                   buffered=True, autocommit=True)

db_connection = open_db()

def save_game_db(pseudo, exercise, date_hour, duration, nbtrials, nbsuccess):
    query = "insert into result (name, exercise, date_hour, duration, nbtrials, nbsuccess) values (%s,%s,%s,%s,%s,%s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (pseudo, exercise, date_hour, duration, nbtrials, nbsuccess))
