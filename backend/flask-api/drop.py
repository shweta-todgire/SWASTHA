import sqlite3

# Connect to your database
conn = sqlite3.connect("swastha.db")
cursor = conn.cursor()

# Get all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Tables you want to keep
keep_tables = []

# Drop all tables except the ones in keep_tables
for table in tables:
    table_name = table[0]
    if table_name not in keep_tables:
        print(f"Dropping table: {table_name}")
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

# Commit and close
conn.commit()
conn.close()

print("✅ Unnecessary tables deleted successfully!")
