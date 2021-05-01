import os
import sys
import json
import pprint
from lib.json_utils import load_json, save_json
from lib.answer_generator import generate_answers
from lib.parameters import ordered_table_names,ordered_view_names

sample_db_path = sys.argv[1]
answer_save_path = sys.argv[2]

path_to_student_sql = 'queries.sql'

print(f'Running queries for file:\n{path_to_student_sql}\n')

print('#'*70)
print(f'Creaing answer for db: {sample_db_path}')
print('#'*70)
sample_DB_json = load_json(sample_db_path)


answers = {
    'sampleDB': generate_answers(json_file=sample_DB_json,
        student_path=path_to_student_sql,
        tables=ordered_table_names,
        views=ordered_view_names)}

save_json(answers, answer_save_path)

print('\n\n')
print('-*'*35)
# pprint.pprint(json.dumps(answers))
print('-*'*35)
