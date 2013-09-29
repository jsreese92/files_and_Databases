'''
Created on Sep 20, 2012

@author: jsreese
'''
import sqlite3

db = sqlite3.connect("movies.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()

print "Question 2.A"
cursor.execute("SELECT title FROM Movies WHERE title LIKE '%Star Wars%'")
for row in cursor:
    print row[0]
print
