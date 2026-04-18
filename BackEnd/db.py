from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.getenv("ACCESS_DB_PATH")

# Fetches "DB_PATH" file from the ".env" file using a variable; conceals the local machine's path to the accdb file.
print("DB PATH FROM ENV:", DB_PATH)
print("EXISTS:", os.path.exists(DB_PATH))

# Driver connection to the MS Access database file
conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    rf'DBQ={DB_PATH};'
)

print("CONNECTED SUCCESSFULLY")

# Calls the connection to the db file
def get_connection():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        rf'DBQ={DB_PATH};'
    )
    return pyodbc.connect(conn_str)

# Fetches client input from app.
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

# Calls for retrieved input to be placed in database.
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
