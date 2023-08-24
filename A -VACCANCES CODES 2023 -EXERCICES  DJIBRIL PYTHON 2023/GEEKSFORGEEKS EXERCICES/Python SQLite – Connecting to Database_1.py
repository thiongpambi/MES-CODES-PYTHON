import sqlite3
try:
    #Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')
    # Write a query and execute it with cursor
    query = 'select sqlite_version();'
    cursor.execute(query)
    #Fetch and out put result
    result = cursor.fetchall()
    print('SQlit version is {}'.format(result))
    #close cursor
    cursor.close()
    #handler errors
except sqlite3.Error as error:
    print('Error occured as-',error)
    #Close DB Connection irrespective of success
    #or failure
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQlite Connection closed')



