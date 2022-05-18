import psycopg2

connect = psycopg2.connect(
    database="pdb",
    user="optikrus",
    password="password123456",
    host="127.0.0.1",
    port="5432"
)


def fill_table_users(name: str):
    cursor = connect.cursor()
    insert = cursor.execute
    insert(f"""
    INSERT INTO users ("name")
    VALUES('{name}');
    """)
    connect.commit()
    print("Database successfully add " + name)


fill_table_users('user')
