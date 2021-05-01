import sys
sys.path.append('..')

import json

from lib.sql_binding.json_utils import load_json
from lib.sql_binding.answer_generator import generate_answers
from lib.sql_binding.parameters import ordered_table_names


sample_db_path = "../testDBs/sampleUnivDB.json"

num_params = len(sys.argv)
if num_params > 1:
	sample_db_path = sys.argv[1]

db = load_json(sample_db_path)

student_path = 'class_example_sql.sql'
tables = ordered_table_names
views = ['query_a', 'query_b']
output = generate_answers(db, student_path, tables, views)

print(json.dumps(output))
