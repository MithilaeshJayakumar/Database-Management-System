from .connect import connect
from .defaults import del_all_plsql


def delete_all_tables(conn, commit=True):

    cursor = conn.cursor()

    print('Deleting all tables...')
    cursor.execute(del_all_plsql)
    print('Deletion complete')
    
    if commit:
        conn.commit()
        print('Deletion committed.')


if __name__ == '__main__':
    from credentials import username, password
    from connect import connect
    conn = connect(username, password)
    delete_all_tables(conn)
    conn.close()


