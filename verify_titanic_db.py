import sqlite3
import pandas as pd

def verify_data(db_name='titanic.db', csv_file='train.csv'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM titanic;")
    db_count = cursor.fetchone()[0]
    conn.close()

    df = pd.read_csv(csv_file)
    csv_count = len(df)

    print(f"Number of rows in database: {db_count}")
    print(f"Number of rows in CSV file: {csv_count}")

    if db_count == csv_count:
        print("All data has been successfully imported into the database.")
    else:
        print("Data mismatch: some rows may be missing in the database.")

if __name__ == "__main__":
    verify_data()
