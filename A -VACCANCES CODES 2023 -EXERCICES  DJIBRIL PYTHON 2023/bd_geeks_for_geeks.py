import sqlite3
#create connection by using object to
#connect with college_details database
connection = sqlite3.connect('college.bd')

#sqlite execute queryto create a table
connection.execute("""create table college(
    geek_id
    geek_name,
    adresse
);""")
print("Table created successfully")
connection.close()