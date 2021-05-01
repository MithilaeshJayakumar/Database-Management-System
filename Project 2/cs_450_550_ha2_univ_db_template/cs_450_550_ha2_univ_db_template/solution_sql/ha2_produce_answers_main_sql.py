import sys
sys.path.append('..')

import json

from lib.sql_binding.json_utils import load_json, save_json
from lib.sql_binding.parameters import ordered_table_names, ordered_view_names
from lib.sql_binding.answer_generator import generate_answers


db1 = load_json("../testDBs/db1.json")
db2 = load_json("../testDBs/db2.json")
db3 = load_json("../testDBs/db3.json")
db4 = load_json("../testDBs/db4.json")
db5 = load_json("../testDBs/db5.json")
db6 = load_json("../testDBs/db6.json")
db7 = load_json("../testDBs/db7.json")
db8 = load_json("../testDBs/db8.json")
db9 = load_json("../testDBs/db9.json")
db10 = load_json("../testDBs/db10.json")
db11 = load_json("../testDBs/db11.json")
db12 = load_json("../testDBs/db12.json")

student_path = 'sql_views.sql'
tables = ordered_table_names
views = ordered_view_names

answers = {}
print(f'-'*40, 'Generating answers for db1')
answers["db1"] = generate_answers(db1, student_path, tables, views)
print(f'-'*40, 'Generating answers for db2')
answers["db2"] = generate_answers(db2, student_path, tables, views)
print(f'-'*40, 'Generating answers for db3')
answers["db3"] = generate_answers(db3, student_path, tables, views)
print(f'-'*40, 'Generating answers for db4')
answers["db4"] = generate_answers(db4, student_path, tables, views)
print(f'-'*40, 'Generating answers for db5')
answers["db5"] = generate_answers(db5, student_path, tables, views)
print(f'-'*40, 'Generating answers for db6')
answers["db6"] = generate_answers(db6, student_path, tables, views)
print(f'-'*40, 'Generating answers for db7')
answers["db7"] = generate_answers(db7, student_path, tables, views)
print(f'-'*40, 'Generating answers for db8')
answers["db8"] = generate_answers(db8, student_path, tables, views)
print(f'-'*40, 'Generating answers for db9')
answers["db9"] = generate_answers(db9, student_path, tables, views)
print(f'-'*40, 'Generating answers for db10')
answers["db10"] = generate_answers(db10, student_path, tables, views)
print(f'-'*40, 'Generating answers for db11')
answers["db11"] = generate_answers(db11, student_path, tables, views)
print(f'-'*40, 'Generating answers for db12')
answers["db12"] = generate_answers(db12, student_path, tables, views)

# print('+'*70, f'\nFINAL OUTPUT FOR ALL DATABASE:\n\n')
# print(json.dumps(answers))

save_path = 'answers.json'
if len(sys.argv) > 1:
	save_path = sys.argv[1]
save_json(answers, save_path)
