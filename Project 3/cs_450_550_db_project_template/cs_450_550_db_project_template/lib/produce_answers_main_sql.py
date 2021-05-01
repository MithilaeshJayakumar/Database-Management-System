import os
import sys
import pprint
from lib.json_utils import load_json, save_json
from lib.answer_generator import generate_answers
from lib.parameters import ordered_table_names, ordered_view_names


db_list = []

if len(sys.argv) == 1:
    path_to_student_sql = 'queries.sql'
else:
    path_to_student_sql = sys.argv[1]

answer_save_path = os.path.join('answers.json')

print(f'Running queries for file:\n{path_to_student_sql}\n')

# Load dbs
for file in sorted(os.listdir('testDBs')):
    if file.startswith('db') and file.endswith('.json'):
        file_path = os.path.join('testDBs', file)
        print(f'Found db file: {file_path}')
        db_list.append(load_json(file_path))

dbs = {f'db{i+1}': db for i, db in enumerate(db_list)}

answers = {}

# Generate query for each db
for db_name, db in dbs.items():
    print('\n')
    print('#'*70)
    print(f'Creaing answer for db: {db_name}')
    print('#'*70)
    answers[db_name] = generate_answers(json_file=db, student_path=path_to_student_sql,
    	tables=ordered_table_names, views=ordered_view_names)

# Save output
print('\n\n')
print('-*'*35)
save_json(answers, answer_save_path)
print(f'Output saved in {answer_save_path}')
print('-*'*35)
