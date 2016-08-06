from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
# Use psycopg to interact with Postgres
import psycopg2
from redis import StrictRedis

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.redis = StrictRedis()

    def process(self, tup):
        word = tup.values[0]
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
        
        #if(self.counts[word] == 0 ):
        #    conn = psycopg2.connect(database="tcount", user="postgres", password="password", host="localhost", port="5432")
        #    cur = conn.cursor()
        #    cur.execute("INSERT INTO Tweetwordcount (word, count) VALUES (%s, %s)", (word, str(1)));
        #    conn.commit()
        #    conn.close
        #else:
        #    conn = psycopg2.connect(database="tcount", user="postgres", password="password", host="localhost", port="5432")
        #    cur = conn.cursor()
        #    uCount = self.counts[word] + 1
        #    cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s",(uCount, word))
        #    conn.commit()
        #    conn.close()
