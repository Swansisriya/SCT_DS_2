import sqlite3

def show_database(db_name='titanic.db'):
    import pandas as pd
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])
    print("\nSample data from 'titanic' table:")
    df = pd.read_sql_query("SELECT * FROM titanic LIMIT 10;", conn)
    print(df.to_string(index=False))
    conn.close()

if __name__ == "__main__":
    show_database()
