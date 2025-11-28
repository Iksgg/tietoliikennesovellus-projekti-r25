import mysql.connector
import csv
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")
db_port = int(os.getenv("DB_PORT", 3306))

def fetch_data_from_db(groupid=25):
    data = []
    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name,
            port=db_port,
            auth_plugin='mysql_native_password')
        try:
            cur = conn.cursor()
            query = "SELECT * FROM posdata WHERE groupid = %s"
            cur.execute(query, (groupid,))
            rows = cur.fetchall()
            for row in rows:
                data.append(row)
            cur.close()
        except Exception as e:
            print(f"Error during query execution: {e}")
    except Exception as e:
        print(f"Error connecting to database: {e}")
    finally:
        conn.close()
        return data

def makeCSV(data):
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            if row:  
                writer.writerow(row)
    print("Data written to output.csv")


def main():
    data = fetch_data_from_db()
    makeCSV(data)

if __name__ == "__main__":
    main()

        