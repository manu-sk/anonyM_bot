import mysql.connector
import pyodbc
import json
import collections
conn = mysql.connector.connect(user='root',password='hacker',database='chatbot')
cursor = conn.cursor()
cursor.execute("""SELECT intents_tag, intents_patterns, intents_responses FROM trainingData""")	
data = cursor.fetchall()
jsondata_list = []
for rowdata in data:
	t = (rowdata[0],rowdata[1],rowdata[2])
	jsondata_list.append(t)
	
intents = json.dumps(jsondata_list, indent=4, sort_keys=True)


objects_list = []
objects_list.append('{ intents :')
for rowdata in data:
	d = collections.OrderedDict()
	d['tag']= rowdata[0]
	d['patterns']= rowdata[1]
	d['responses']= rowdata[2]
	objects_list.append(d)	
objects_list.append('}')
j = json.dumps(objects_list)

print(j)	
