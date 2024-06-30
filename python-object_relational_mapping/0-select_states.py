#!/usr/bin/python3
"""States"""


if __name__ == '__main__':
    from sys import argv                                                                                                    import MySQLdb
    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()

    executed = f"SELECT * FROM states"
    records = cursor.execute(executed).fetchall()

    for state in records:
        print(state)

    if cursor:
        cursor.close()
    if db:
        db.close()
