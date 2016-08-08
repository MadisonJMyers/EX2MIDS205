from sys import argv
import getopt
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

def asker(word):
	conn = psycopg2.connect(database="tcount", user="postgres", password="password", host="localhost", port="5432")
	cur = conn.cursor()
	query = cur.mogrify("SELECT count FROM tweetwordcount WHERE word = %s", (word,))
	cur.execute(query)
	count = cur.fetchall()
	if count:
		result = count[0][0]
	else:
		result = 0
	return result

def results():
	conn = psycopg2.connect(database="tcount", user="postgres", password="password", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT * FROM tweetwordcount")
	output = cur.fetchall()
	output.sort()
	print str(output)[1:-1]
	return output


if __name__== "__main__":
	if len(argv) == 1:
		results()
	else:
		for a in argv[1:]:
			print "Total number of occurences of \"%s\": " %a + str(asker(a))
