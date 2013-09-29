'''
Created on Sep 20, 2012

@author: jsreese
'''
import sqlite3

db = sqlite3.connect("movies.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()

print "********Question 2.A********"
cursor.execute("SELECT title FROM Movies WHERE title LIKE '%Star Wars%'")
for row in cursor:
    print row[0]
print

print "********Question 2.B********"
#distinct because somebody could rent it multiple times
query = """SELECT DISTINCT C.cardNo, C.first, C.last
            FROM Customers C, Rentals R, Movies M
            WHERE C.cardNo = R.cardNo
                AND M.movieId = R.movieId
                AND M.title = "The Sting"
                AND (C.first = 'PAUL' OR C.first = 'ROBERT')
            ORDER BY C.first"""
cursor.execute(query)
for row in cursor:
    print row['first'], row['last']
print

print "********Question 2.C********"
query = """SELECT C.cardNo, C.first, C.last
            FROM Customers C, Rentals R, Movies M
            WHERE C.cardNo = R.cardNo
                AND M.movieId = R.movieId
                AND M.title = "2001: A Space Odyssey"
                AND R.date >= '2001-01-01'
                AND R.date < '2001-01-8'"""
cursor.execute(query)
for row in cursor:
    print row['first'], row['last']
print
        
print "********Question 2.D********"

query = """ 
        SELECT C.first, C.last, Count(R.cardNo) as count
        From Customers C, Rentals R
        WHERE C.cardNo = R.cardNo
        GROUP BY R.cardNo
        HAVING count(R.cardNo) = (
            SELECT max(count) as maxCount from (
                SELECT Count(R.cardNo) AS count
                FROM Customers C, Rentals R
                WHERE C.cardNo = R.cardNo
                GROUP BY R.cardNo
            )
        )
        """
cursor.execute(query)

for row in cursor:
    print row['first'], row['last'], row['count']
print


print "********Question 2.E********"

query = """
        SELECT M.title, Count(M.movieId) as count
        FROM Rentals R, Movies M
        WHERE R.movieId = M.movieId
        GROUP BY M.movieId
        HAVING count(M.movieId) = (
            SELECT max(count) as maxCount from (
                SELECT Count(M.movieId) as count
                FROM Movies M, Rentals R
                WHERE M.movieId = R.movieId
                GROUP BY M.movieId
            )
        )
        """
cursor.execute(query)

for row in cursor:
    print row['title'], row['count']
print        

print "********Question 2.F********"

query = """
        SELECT  C.cardNo, C.first, C.last
        FROM Customers C, Movies M, Rentals R, Movies M2, Rentals R2
        WHERE C.cardNo = R.cardNo
            AND R.movieId = M.movieId
            AND M.title = "King Kong"
            AND C.cardNo = R2.cardNo
            AND R2.movieId = M2.movieId
            AND M2.title = "Godzilla"
            AND R.rating > R2.rating
            AND C.cardNo IN (
                SELECT C.cardNo
                FROM Customers C
                WHERE C.cardNo IN ( 
                    SELECT C.cardNo 
                    FROM Customers C, Rentals R, Movies M
                    WHERE C.cardNo = R.cardNo
                        AND M.movieId = R.movieId
                        AND M.title = "King Kong"
               
                    INTERSECT
        
                    SELECT C.cardNo 
                    FROM Customers C, Rentals R, Movies M
                    WHERE C.cardNo = R.cardNo
                        AND M.movieId = R.movieId
                        AND M.title = "Godzilla"
                )
            )      
        """

cursor.execute(query)

for row in cursor:
    print row['cardNo'], row['first'], row['last']
print

print "********Question 2.G*********"

query = """
        SELECT C.first, C.last, Count(R.rating) as count
        FROM Customers C, Rentals R
        WHERE C.cardNo = R.cardNo
            AND R.rating = 5
        GROUP BY C.cardNo
        ORDER BY count DESC
        LIMIT 1
        """
cursor.execute(query)

for row in cursor:
    print row['first'], row['last'], row['count']
print

print "********Question 2.H********"

query = """
        SELECT M.title, Count(R.rating) as count
        FROM Rentals R, Movies M
        WHERE R.movieId = M.movieId
            AND R.rating = 1
        GROUP BY M.title
        ORDER BY count DESC
        LIMIT 1
        """

cursor.execute(query)

for row in cursor:
    print row['title'], row['count']
print
        
print "********Question 2.I********"

query = """
        SELECT C.first, C.last, M.title
        FROM Customers C, Rentals R, Movies M
        WHERE C.cardNo = R.cardNo
            AND R.movieId = M.movieId
            AND C.first = "ALICE"
            AND M.title LIKE '%Alice%'
        """

cursor.execute(query)

for row in cursor:
    print row['first'], row['last'], row['title']
print

print "********Question 2.J********"

query = """
        SELECT COUNT(R.rating) frequency, R.rating
        FROM Rentals R
        GROUP BY R.rating
        ORDER BY COUNT(R.rating) DESC
        LIMIT 1
        """
cursor.execute(query)

for row in cursor:
    print row['rating'], row['frequency']
print


