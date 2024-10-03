import pyodbc
import stoke

# Sever and user information
server = 'NGUYENTIEN'
database = 'CRPYTO'
username = 'ndt'
password = '123'    

# connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'


# insert values in to database
def addValues(item):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cry = stoke.stokeCrypto(item)
    cursor.execute("INSERT INTO CRPYTO (nameCrp, datetimeStoke, priceCrp, changeCrp) VALUES (?, ?, ?, ?)", cry['name'], cry['time'], cry['price'],cry['change'])
    conn.commit()
    cursor.close()
    conn.close()
