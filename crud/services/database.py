import pyodbc;

server = 'DESKTOP-6AJCIJ8\SQLEXPRESS' 
database = 'posto' 
cnxn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()
 