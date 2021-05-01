import json
import cx_Oracle
from collections import OrderedDict

def query_to_json(cursor, name=None):
	# name, type, display_size, internal_size, precision, scale, null_ok
	columns = OrderedDict()

	rows_dict_list = []

	for col_idx, desc in enumerate(cursor.description):
		col_type = desc[1]
		precision = desc[4]
		scale = desc[5]

		if col_type == cx_Oracle.NUMBER:
			col_type = 'number'
		elif col_type == cx_Oracle.STRING:
			col_type = 'string'

		columns[col_idx] = {
			'name': desc[0],
			'type': col_type,
			'precision': precision,
			'scale': scale,
			'null_ok': desc[6]
			}
	
	result = cursor.fetchall()
	
	for row in result:
		row_dict = {}
			
		for col_idx, col in columns.items():
			col_name = col['name']
			row_dict[col_name] = row[col_idx]
		rows_dict_list.append(row_dict)

	return rows_dict_list


def convert_query_json_list(cursor, name=None):
	# name, type, display_size, internal_size, precision, scale, null_ok
	columns = {}

	for col_idx, desc in enumerate(cursor.description):
		col_type = desc[1]
		precision = desc[4]
		scale = desc[5]

		if col_type == cx_Oracle.NUMBER:
			col_type = 'number'
		elif col_type == cx_Oracle.STRING:
			col_type = 'string'

		columns[col_idx] = {
			'name': desc[0],
			'type': col_type,
			'precision': precision,
			'scale': scale,
			'null_ok': desc[6]
			}

	query_json = {
		'name': None,
		'column_inf': columns,
		'values': {
			col['name']:[] for col_idx, col in columns.items() 
		}
	}

	result = cursor.fetchall()

	for row in result:
		for col_idx, col in columns.items():
			col_name = col['name']
			query_json['values'][col_name].append(row[col_idx])

	return query_json



def convert_query_json_list(cursor, name=None):
	# name, type, display_size, internal_size, precision, scale, null_ok
	columns = {}

	for col_idx, desc in enumerate(cursor.description):
		col_type = desc[1]
		precision = desc[4]
		scale = desc[5]

		if col_type == cx_Oracle.NUMBER:
			col_type = 'number'
		elif col_type == cx_Oracle.STRING:
			col_type = 'string'

		columns[col_idx] = {
			'name': desc[0],
			'type': col_type,
			'precision': precision,
			'scale': scale,
			'null_ok': desc[6]
			}

	query_json = {
		'name': None,
		'column_inf': columns,
		'values': {
			col['name']:[] for col_idx, col in columns.items() 
		}
	}

	result = cursor.fetchall()

	for row in result:
		for col_idx, col in columns.items():
			col_name = col['name']
			query_json['values'][col_name].append(row[col_idx])

	return query_json


def save_json(data, path):
	with open(path, 'w') as f:
		json.dump(data, f)


def load_json(path):
	with open(path, 'r') as f:
		data = json.load(f)
	return data


def insert_json_db(file, conn):
	db = load_json(file)
	tables = db['tables']
	cursor = conn.cursor()

	for table_name, table_data in tables.items():
		command = f'INSERT INTO {table_name} values ('

		for col, col_data in table_data.items():
			command += f'{col} {col_type}, '
		command += f'primary key({table_info["primary_key"]}));'
		print(command)
		cursor.execute(command)
	cursor.commit()
	conn.close()
	
