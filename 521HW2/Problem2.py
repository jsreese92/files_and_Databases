'''
Created on Sep 20, 2012

@author: jsreese
'''
import sqlite3

db = sqlite3.connect("movies.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()

cursor.execute("SELECT COUNT(*) FROM Movies")
result = cursor.fetchone()
print "Movie count as tuple =", result

cursor.execute("SELECT COUNT(*) FROM Customers")
result = cursor.fetchone()
print "Customer count =", result[0]

cursor.execute("SELECT COUNT(*) FROM Rentals")
result = cursor.fetchone()
print "Rentals"