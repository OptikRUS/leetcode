import psycopg2


connect = psycopg2.connect(
    database="pdb",
    user="optikrus",
    password="password123456",
    host="127.0.0.1",
    port="5432"
)


def insert_user(username):
    return f"""
        INSERT INTO users ("name")
        VALUES('{username}');
        """


def fill_table_users(name: str):
    with connect:
        cursor = connect.cursor()
        cursor.execute(insert_user(name))
        return "Database successfully add " + name


for i in range(100):
    fill_table_users(f'name{i}')
