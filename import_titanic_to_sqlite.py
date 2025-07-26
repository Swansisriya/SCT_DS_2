import sqlite3
import pandas as pd

def create_database(db_name='titanic.db'):
    conn = sqlite3.connect(db_name)
    return conn

def import_csv_to_db(csv_file, conn):
    df = pd.read_csv(csv_file)
    df.to_sql('titanic', conn, if_exists='replace', index=False)
    print("Data imported successfully into the 'titanic' table.")

def main():
    db_name = 'titanic.db'
    csv_file = 'train.csv'
    conn = create_database(db_name)
    import_csv_to_db(csv_file, conn)
    conn.close()

if __name__ == "__main__":
    main()
