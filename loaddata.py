def loadData():
    import collections
    import mysql.connector
    import json
    conn = mysql.connector.connect(user='root', password='hacker', database='chatbot')
    cursor = conn.cursor()
    cursor.execute("""SELECT intents_tag, intents_patterns, intents_responses FROM trainingData""")
    data = cursor.fetchall()
    jsondata_list = []
    for rowdata in data:
        t = (rowdata[0], rowdata[1], rowdata[2])
        jsondata_list.append(t)
        print(jsondata_list)
    intents = json.dumps(jsondata_list, indent=4)
    print(intents)
    objects_list = []

    for rowdata in data:
        d = {}
        d['tag'] = rowdata[0]
        d['patterns'] =  rowdata[1]
        d['responses'] = rowdata[2]
        objects_list.append(d)
    # objects_list.append(d)
    #print (objects_list)
    j = json.dumps(objects_list,indent=3)

    print (j)
    objects_file = 'intent.json'
    f = open(objects_file, 'w')
    f.write('{"intents":' + j + '}')
    f.close
    conn.close()


if __name__ == "__main__":
    loadData()
