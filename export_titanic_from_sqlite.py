import sqlite3
import pandas as pd

def export_to_files(db_name='titanic.db', export_csv='titanic_full_table_cleaned.csv', export_excel='titanic_full_table.xlsx'):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT * FROM titanic;", conn)
    df.to_csv(export_csv, index=False)
    df.to_excel(export_excel, index=False)
    print(f"Exported {len(df)} rows to {export_csv} and {export_excel}")
    conn.close()

if __name__ == "__main__":
    export_to_files()
