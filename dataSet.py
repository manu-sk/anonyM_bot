import collections
import mysql.connector
import json
import sys
conn = mysql.connector.connect(user='root', password='hacker', database='chatbot')
cursor = conn.cursor()
tag = sys.argv[1]
print(tag)
patterns = []
patterns = [sys.argv[2]]
stringpatterns = json.dumps(patterns)
#stringlistvalue=json.dumps(patterns)
responses = []
responses = [sys.argv[3]]
stringresponses = json.dumps(responses)
print(tag)
print(stringpatterns)
print(stringresponses)
cursor.execute("""INSERT INTO trainingData(intents_tag,intents_patterns,intents_responses) VALUES(%s,%s,%s)""",(tag, stringpatterns, stringresponses))
conn.commit()