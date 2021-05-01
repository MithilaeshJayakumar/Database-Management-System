import cx_Oracle


def execute_file(file_path, conn, commit=True, verbose=False):
    with open(file_path) as f:
        file = f.read()
        
    cursor = conn.cursor()

    for line in file.split(';'):
        line = line.strip()

        try:
            cursor.execute(line)

        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            
            # Assert 942 only occurs when drop command is executed
            if error.code == 942:
                if verbose:
                    print('-'*70)
                assert 'drop' in line.lower(), \
                    f"Exception {error.code}:{error.message} occurred in a " \
                    f"non-DROP command:\n\n {line}"
                if verbose:
                    print(f'DROP command. Raised exception {error.code}:{error.message}.')

            elif line == '':
                # print(f"Empty command. Raised Exception {error.code}:{error.message}.")
                continue
            else:
                print('-'*70)
                print(error.code, error.message)
                print(line)
            if verbose:
                print('-'*70)


    if commit:
        conn.commit()


if __name__ == '__main__':
    import sys

    from connect import connect
    from credentials import username, password
    conn = connect(username, password)

    filepath = sys.argv[1]
    execute_file(file_path=file_path, conn=conn, commit=True)
