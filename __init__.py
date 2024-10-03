import stoke
import sqlserver

import csv
import os

list = ['Bitcoin','Ethereum','BNB','Solana','USD Coin','XRP','Dogecoin','Tron','Toncoin']

# Save to SQL
def saveToSQLServer():
    for item in list:
        sqlserver.addValues(item)
# Save to CSV
def saveToCSVFile():
    if os.path.exists('D:\Python\Stock_Price_Crypto\stokeData.csv'):
        exit
    else:
        with open('D:\Python\Stock_Price_Crypto\stokeData.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name','Time','Price','Change'])
    for item in list:
        data = stoke.stokeCrypto(item)
        with open('D:\Python\Stock_Price_Crypto\stokeData.csv', mode='a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data['name'],data['time'],data['price'],data['change']])

saveToCSVFile()
# saveToSQLServer()