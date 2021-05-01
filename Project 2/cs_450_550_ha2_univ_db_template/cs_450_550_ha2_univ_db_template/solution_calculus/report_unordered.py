import sys
import json
import copy
from collections import OrderedDict

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


#correct_answers_path = sys.argv[1]
#answers_path = sys.argv[2]

#correct_answers = load_json(correct_answers_path)
#answers = load_json(answers_path)
correct_answers = load_json("../testDBs/correct_answers.json")
answers = load_json("answers.json")

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

for query_idx, query in enumerate(queries):
	query_correct_all = True

	for db in dbs:
		c_out = copy.deepcopy(correct_answers[db][query])
		a_out = copy.deepcopy(answers[db][query])

		query_db_report = {
							"query": query,
							"db": db,
							"correct": True
							}

		if CHECK_ORDER:
			if c_out != a_out:
				query_db_report["correct"] = False
				query_correct_all = False
		else:
			for c_tuple in c_out:

				# Check if this tuple is in a_out
				# Break at once if not found
				if c_tuple in a_out:
					a_out.remove(c_tuple)
					continue

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

#print(json.dumps(report))
f = open("report.json","w")
f.write(json.dumps(report))
