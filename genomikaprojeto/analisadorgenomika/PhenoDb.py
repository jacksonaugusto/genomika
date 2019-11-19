import sqlite3

connection = sqlite3.connect('PhenoDb.db')
c = connection.cursor()

#SQL

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dados(id integer, gene text, disease text)')


create_table()


def dataentry():
    c.execute("INSERT INTO dados VALUES(1, 'EYA1', 'Branchiootic Syndrome')")
    c.execute("INSERT INTO dados VALUES(2, 'EYA1', 'Branchiootorenal Syndrome')")
    c.execute("INSERT INTO dados VALUES(3, 'BRCA1', 'Breast Cancer')")
    c.execute("INSERT INTO dados VALUES(4, 'BRCA2', 'Breast Cancer')")
    c.execute("INSERT INTO dados VALUES(5, 'CDH1', 'Breast Cancer')")
    c.execute("INSERT INTO dados VALUES(6, 'PALB2', 'Breast Cancer')")
    c.execute("INSERT INTO dados VALUES(7, 'PTEN', 'Breast Cancer')")
    c.execute("INSERT INTO dados VALUES(8, 'STK11', 'Breast Cancer')")
    c.execute("INSERT INTO dados VALUES(9, 'TP53', 'Breast Cancer')")
    c.execute("INSERT INTO dados VALUES(10, 'AARS', 'Brown-Vialetto-Van Laere Syndrome')")
    c.execute("INSERT INTO dados VALUES(11, 'ATL1', 'Brown-Vialetto-Van Laere Syndrome')")
    connection.commit()

dataentry()


#lendo dados

sql = 'SELECT * FROM dados WHERE disease = ?'

def read_data(wordUsed):
   for row in c.execute(sql, (wordUsed,)):
        print(row)

(read_data('doenca')
