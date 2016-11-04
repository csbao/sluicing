#!/usr/bin/python

import sqlite3, sys, json

# requires json format, a la allSluices.jsons
f = sys.argv[1]
content = []
with open(f, 'r') as fd:
    content = fd.readlines()

conn = sqlite3.connect('nyt.db')
c = conn.cursor()



#create nyt table, index will be metadata.file+"_"+metadata.line
c.execute(''' DROP TABLE IF EXISTS sluices''')

c.execute('''CREATE TABLE sluices
              (line text, file text, sluice text, sentence text,
              govVP text, before text, after text) ''')


for l in content:
    obj = json.loads(l)
    # "metadata": {
    #                 "line": 3855,
    #                 "file": "Treebanks/NYT-Parsed/nyt_eng_199407.tgrep2",
    #                 "treeNode": 12
    #             },

    index = obj["metadata"]["file"] + "_" + str(obj["metadata"]["line"])
    file = obj["metadata"]["file"]
    sluice = obj["match"]["sluice"]["string"] #should we add the tree too?
    sent = obj["match"]["sentence"]["string"]
    govVP = obj["match"]["govVP"]["string"]
    before = ""
    after = ""
    for i in obj["before"]:
        before+=i["string"]
    for i in obj["after"]:
        after += i["string"]
    record = (index, file, sluice, sent, govVP, before, after)

    c.execute("INSERT INTO sluices VALUES (?, ?, ?, ?, ?, ?, ?)", record)

conn.commit()
conn.close()

#
#
# f = sys.argv[1]
# fd = open(f)
# content = fd.readlines()
#
# for l in content[1:20]:
#     # l = fd.readline()
#     obj = json.loads(l)
#     print(obj)
#     print('\n\n\n')
#     out = json.dumps(obj, indent=2)
#     # pdb.set_trace()
#     # print (out)
#
# fd.close()