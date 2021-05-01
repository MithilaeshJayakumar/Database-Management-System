import cx_Oracle
from .json_utils import load_json
from .parameters import ordered_table_names


# TABLE NAMES MUST BE IN ORDER TO SATISFY FOREIGN KEY CONSTRAINTS
def insert_json_db(json_file, conn, table_names, commit=True):
    tables_dict = json_file["tables"]

    cursor = conn.cursor()

    for table_name in table_names:
        table_dict_list = tables_dict[table_name]

        # Add only if any value exists in the json file
        if len(table_dict_list) > 0:
            
            # List of row tuples ordered by the column name
            row_tuple_list = []

            for row_dict in table_dict_list:
                row_tuple = []

                for col_name in sorted(row_dict.keys()):
                    row_tuple.append(row_dict[col_name])
                row_tuple_list.append(tuple(row_tuple))

            # Column names are based on last tuple which should be same for all
            col_names = ','.join(sorted(row_dict.keys()))

            # Make the command to execute ready
            command = f"INSERT INTO {table_name} ({col_names}) VALUES ("
            for i in range(len(row_tuple)):
                command += ":" + str(i+1) + ","
            command = command[:-1] + ")"
            cursor.bindarraysize = len(row_tuple_list)
            try:
                cursor.executemany(command, row_tuple_list)
            except cx_Oracle.IntegrityError as exc:
                error, = exc.args
                print('-'*70)
                print(error.code, error.message)
                print(command, row_tuple_list)


    if commit:
        conn.commit()
        print(f'Insertion commited.')

