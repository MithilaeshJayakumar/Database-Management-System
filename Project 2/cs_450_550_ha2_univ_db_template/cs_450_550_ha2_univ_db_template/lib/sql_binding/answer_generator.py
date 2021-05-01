import os
import cx_Oracle
from credentials import username, password
from .connect import connect
from .delete import delete_all_tables
from .insert import insert_json_db
from .execute import execute_file
from .json_utils import query_to_json


def generate_answers(json_file, student_path, tables, views):
    conn = connect(username, password)
    delete_all_tables(conn, commit=True)

    # Create tables
    print("\nCreating tables...")
    file_path = os.path.join('create_empty_tables.sql')
    execute_file(file_path=file_path, conn=conn, commit=True)

    # Fill tables
    print("Inserting values...")
    insert_json_db(json_file=json_file, conn=conn, table_names=tables, commit=True)

    # Execute student sql file
    print("Executing student sql file...")
    execute_file(file_path=student_path, conn=conn, commit=True)

    answer_dict = {}

    for view in views:
        cursor = conn.cursor()
        try:
            cursor.execute(f'SELECT * FROM {view}')
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print('-'*70)
            print(error.code, error.message)
            print(f'{view} generated error!!')
            print('-'*70)
            answer_dict[view] = None
            continue
        answer_dict[view] = query_to_json(cursor)
    conn.commit()

    return answer_dict


