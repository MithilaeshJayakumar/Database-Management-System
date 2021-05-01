import json
import class_example_algebra as ha

f = open("../testDBs/sampleUnivDB.json", "r")
db = json.loads(f.read())

output = ha.ha2(db)

print(json.dumps(output))
