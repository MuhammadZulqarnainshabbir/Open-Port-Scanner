import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE ports(id integer identity  PRIMARY KEY,networkIp message_text ,NmapVersion message_text ,Ip Status message_text ,Open Ports message_text )"
cursor.execute(create_table)
ports = (
    (1, 'text1', 'text2', 'text3','text 4'))
insert_query = "INSERT INTO ports VALUES (?,?,?,?,?)"
ports = [
    (2, 'text1', 'text2', 'text3','text4'),
    (3, 'text1', 'text2', 'text3','text4')

]
cursor.executemany(insert_query, ports)
select_query = "SELECT * FROM ports"
for row in cursor.execute(select_query):
    print(row)
connection.commit()
connection.close()
