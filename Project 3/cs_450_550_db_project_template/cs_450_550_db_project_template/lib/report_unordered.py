import sys
import json
import copy
from collections import OrderedDict, Iterable


def save_json(data, path):
	with open(path, 'w') as f:
		json.dump(data, f)

def load_json(path):
	with open(path, 'r') as f:
		data = json.load(f)
	return data

def get_query_fields(dbs, queries):
	fields = {}

	for query in queries:
		for db in dbs:
			c_out = correct_answers[db][query]
			if len(c_out) == 0:
				continue
			query_fields = [i for i in c_out[0]]
			fields[query] = query_fields
			break
	return fields

# def template_perDBreport(query, dbs):
# 	return [{"query": query, "db":i, "correct": False} for i in dbs]


correct_answers_path = sys.argv[1]
answers_path = sys.argv[2]

correct_answers = load_json(correct_answers_path)
answers = load_json(answers_path)

dbs = [i for i in correct_answers]
queries = [i for i in correct_answers[dbs[0]]]
fields = get_query_fields(dbs, queries)


report = OrderedDict({
						"correctQueries": 0,
						"outOf": len(queries),
						"perQueryReport":[
											{
												"query":q,
												"correct": False,
												"perDBreport": []
											} for q in queries
										]
										})

CHECK_ORDER = False

# For each query
for query_idx, query in enumerate(queries):
	query_correct_all = True

	# For each database
	for db in dbs:
		c_out = copy.deepcopy(correct_answers[db][query])

		# Default per db report
		query_db_report = {
							"query": query,
							"db": db,
							"correct": True
							}

		try:
			a_out = copy.deepcopy(answers[db][query])
		# If db not in answer or query not in the db
		except KeyError as e:
			query_db_report["correct"] = False
			query_correct_all = False
		# If key in anwer, check each tuple in c_out
		else:
			# If checking order, no need to worry about a_out being iterator
			if CHECK_ORDER:
				if c_out != a_out:
					query_db_report["correct"] = False
					query_correct_all = False
			# If answer is NULL or not both of them are iterables
			elif isinstance(c_out, list) and not isinstance(a_out, list):
				query_db_report["correct"] = False
				query_correct_all = False
			else:
				# Check tuple in c_out in a_out
				for c_tuple in c_out:
					if c_tuple in a_out:
						a_out.remove(c_tuple)
					else:
						# Break at once if not found
						query_db_report["correct"] = False
						query_correct_all = False
						break
					
				# If all tuples checked and a_out still has some tuples left
				if len(a_out) != 0:
					query_db_report["correct"] = False
					query_correct_all = False

		report['perQueryReport'][query_idx]['perDBreport'].append(query_db_report)
	
	if query_correct_all:
		report['perQueryReport'][query_idx]["correct"] = query_correct_all
		report["correctQueries"] += 1

print(json.dumps(report))