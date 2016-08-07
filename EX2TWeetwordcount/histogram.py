from sys import argv
import psycopg2


conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost",port="5432")

k1 = int(raw_input('lower bound: '))
k2 = int(raw_input('upper bound: '))

#get cursor
cur = conn.cursor()
cur.execute('''SELECT word, count FROM tweetwordcount WHERE count >= %d AND count <= %d;''' % (k1, k2))

#fetch all the words
wordhistogram  = cur.fetchall()
wordhistogram.sort()

print wordhistogram

conn.commit()

conn.close()
