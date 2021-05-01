import cx_Oracle


def connect(username, password):
    login = f'{username}/{password}@artemis.vsnet.gmu.edu:1521/vse18c.vsnet.gmu.edu'

    print('Connecting...')
    conn = cx_Oracle.connect(login)
    print('Connection complete\n')

    return conn

