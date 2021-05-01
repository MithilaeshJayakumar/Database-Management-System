import json
import ha2lib_calculus as ha

f = open("../testDBs/db1.json", "r")
db1 = json.loads(f.read())
f = open("../testDBs/db2.json", "r")
db2 = json.loads(f.read())
f = open("../testDBs/db3.json", "r")
db3 = json.loads(f.read())
f = open("../testDBs/db4.json", "r")
db4 = json.loads(f.read())
f = open("../testDBs/db5.json", "r")
db5 = json.loads(f.read())
f = open("../testDBs/db6.json", "r")
db6 = json.loads(f.read())
f = open("../testDBs/db7.json", "r")
db7 = json.loads(f.read())
f = open("../testDBs/db8.json", "r")
db8 = json.loads(f.read())
f = open("../testDBs/db9.json", "r")
db9 = json.loads(f.read())
f = open("../testDBs/db10.json", "r")
db10 = json.loads(f.read())
f = open("../testDBs/db11.json", "r")
db11 = json.loads(f.read())
f = open("../testDBs/db12.json", "r")
db12 = json.loads(f.read())

answers = {
  "db1": ha.ha2(db1),
  "db2": ha.ha2(db2),
  "db3": ha.ha2(db3),
  "db4": ha.ha2(db4),
  "db5": ha.ha2(db5),
  "db6": ha.ha2(db6),
  "db7": ha.ha2(db7),
  "db8": ha.ha2(db8),
  "db9": ha.ha2(db9),
  "db10": ha.ha2(db10),
  "db11": ha.ha2(db11),
  "db12": ha.ha2(db12)
}
# print(json.dumps(answers))

with open('answers.json', 'w') as f:
    json.dump(answers, f)
