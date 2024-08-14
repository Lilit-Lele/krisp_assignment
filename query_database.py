print("aaaaaaaaaaaaaaaaaaaaaaaa!")
import psycopg2

import time
print("Waiting for the database to initialize...")
time.sleep(60)  # Wait for 10 seconds

# Connection details
conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password="mypassword",
    host="postgres",  # or the service name if running within Docker Compose
    port="5432"
)

# Create a cursor
cur = conn.cursor()

# Execute a query to retrieve column names
cur.execute("""
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'metrics';
""")

# Fetch and print the results
columns = cur.fetchall()
for column in columns:
    print(column[0])


print("Executing query to fetch rows from 'metrics' table...")
cur.execute("SELECT * FROM metrics;")

# Fetch all rows
rows = cur.fetchall()

# Check if any rows were returned
if not rows:
    print("No rows found in 'metrics' table.")
else:
    print("\nContents of 'metrics' table:")
    for row in rows:
        print(row)



# Close the cursor and connection
cur.close()
conn.close()
