from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "postgres"),
        database=os.environ.get("POSTGRES_DB", "mydb"),
        user=os.environ.get("POSTGRES_USER", "user"),
        password=os.environ.get("POSTGRES_PASSWORD", "password")
    )
    return conn

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected to PostgreSQL: {version}"
    except Exception as e:
        return f"Connection error: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
