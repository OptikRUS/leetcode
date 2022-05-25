import os
from time import time

import psycopg2

username = os.getenv('USERNAME', None)
password = os.getenv('PASSWORD', None)


connect = psycopg2.connect(
    database="pdb",
    user=username,
    password=password,
    host="127.0.0.1",
    port="5432"
)

QUERY = """
        INSERT INTO users ("username", "lastname", "age")
        VALUES('username', 'lastname', 18);
        """


def fill_table_users():
    with connect:
        cursor = connect.cursor()
        cursor.execute(QUERY)


def main():
    for i in range(10000):
        fill_table_users()


if __name__ == "__main__":
    start = time()
    main()
    print(time() - start)

# 16.386794090270996
# 16.187684059143066
# 16.108766078948975
