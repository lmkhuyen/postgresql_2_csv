# Note: worked well with python3.9

import psycopg2.extras

postg_conn = psycopg2.connect(
       database="xxx",
       user="xxxx",
       password="xxx",
       #host="localhost",
       host="xxx.xxx.xxx.xxx",
       port= "xxxx"
)

tables = []

cursor = postg_conn.cursor() 
query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
cursor.execute(query)
results = cursor.fetchall()
for table in results:
    for item in table:
        tables.append(item)

cursor_2 = postg_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
for table in tables:
    print(table)
    with open(f"{table}.csv", 'w') as file_w:
        cursor_2.copy_expert(f"COPY {table} TO STDOUT WITH (FORMAT CSV,  HEADER TRUE, FORCE_QUOTE *)", file_w)
