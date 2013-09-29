'''
Created on Oct 20, 2012

@author: jsreese
'''
import time
import sqlite3
import argparse

parser = argparse.ArgumentParser(description='read database name.')
parser.add_argument('theDatabase')
args = parser.parse_args()
#print args.theDatabase

db = sqlite3.connect(args.theDatabase)
db.row_factory = sqlite3.Row
cursor = db.cursor()

#cursor.execute("CREATE INDEX actorId_movieId on Casts(aid,mid)")
#cursor.execute("CREATE INDEX Act_id on Actors(aid)")
#cursor.execute("CREATE INDEX Mov_Id on Movies(mid)")

print "From origActors.db:"

i = 0
while(i < 5):
    Q1 = """SELECT FName, LName, COUNT(*) as count
            FROM Actors, Casts 
            WHERE Actors.aid=Casts.aid
            GROUP BY Casts.aid"""

    #start = time.clock()
    #cursor.execute(Q1)
    #t = cursor.fetchall(); 
    #end = time.clock() - start
    #print "Processing time =", end
    #count = 0
    #for row in t:
    #    count = count + 1
    #print "Q1 count =", count
    
    A = """
        SELECT M.Title, Count(C.aid) as actorCount
        FROM Movies M, Casts C
        WHERE C.mid = M.mid
        GROUP BY C.aid
        HAVING actorCount > 10
        """
        
    start = time.clock()
    cursor.execute(A)
    t = cursor.fetchall(); 
    end = time.clock() - start
    print "A Processing time =", end
    count = 0
    for row in t:
        #print row['Title'], row['actorCount']
        count = count + 1
    print "A count =", count
    
    B = """
        SELECT A.FNAME, A.LNAME
        FROM Movies M, Casts C, Actors A
        WHERE M.mid = C.mid
            AND C.aid = A.aid
            AND M.Title = 'Donnie Darko'
        """
    start = time.clock()
    cursor.execute(B)
    t = cursor.fetchall(); 
    end = time.clock() - start
    print "B Processing time =", end
    count = 0
    for row in t:
        #print row['FNAME'], row['LNAME']
        count = count + 1
    print "B count =", count  
    
    C = """
        SELECT A.FNAME, A.LNAME, M.Title, M.year
        FROM Movies M, Casts C, Actors A
        WHERE M.mid = C.mid
            AND C.aid = A.aid
        GROUP BY A.aid
        HAVING M.year = MAX(M.year)
        """
            
    start = time.clock()
    cursor.execute(C)
    t = cursor.fetchall(); 
    end = time.clock() - start
    print "C Processing time =", end
    count = 0
    for row in t:
        #print row['FNAME'], row['LNAME'], row['Title'], row['year']
        count = count + 1
    print "C count =", count  
    
    #===========================================================================
    # E = """
    #    SELECT M.Title, Count(C.aid) as actorCount
    #    FROM Movies M, Casts C
    #    WHERE C.mid = M.mid
    #    GROUP BY C.aid
    #    HAVING actorCount > 10
    #    """
    #    
    # #cursor.execute("CREATE INDEX myIndex1 on Casts(aid)")
    # #print "index created"
    # start = time.clock()
    # cursor.execute(E)
    # t = cursor.fetchall(); 
    # end = time.clock() - start
    # print "Processing time =", end
    # count = 0
    # for row in t:
    #    #print row['Title'], row['actorCount']
    #    count = count + 1
    # print "E count =", count
    # 
    #===========================================================================
    
    i = i + 1