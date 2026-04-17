from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.getenv("ACCESS_DB_PATH")

# Temporary print
print("DB PATH FROM ENV:", DB_PATH)
print("EXISTS:", os.path.exists(DB_PATH))

# Test connection:
conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    rf'DBQ={DB_PATH};'
)

print("CONNECTED SUCCESSFULLY")

def get_connection():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        rf'DBQ={DB_PATH};'
    )
    return pyodbc.connect(conn_str)


def insert_client(client):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Clients (clntName, clntEmail, clntCompany) VALUES (?, ?, ?)",
        client['name'],
        client['email'],
        client['company']
    )

    conn.commit()
    conn.close()


def get_clients():
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT [clntName], [clntEmail], [clntCompany] FROM [Clients]"
    ).fetchall()

    conn.close()

    return [
        {"name": r[0], "email": r[1], "company": r[2]}
        for r in rows
    ]