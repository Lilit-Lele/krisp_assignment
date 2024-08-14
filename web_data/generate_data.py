from flask import Flask, render_template
import pandas as pd
from datetime import datetime, timedelta
import random
import psycopg2
import time

app = Flask(__name__)

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                dbname="mydatabase",
                user="myuser",
                password="mypassword",
                host="postgres",
                port="5432"
            )
            return conn
        except psycopg2.OperationalError:
            print("Unable to connect to the database. Retrying in 5 seconds...")
            retries -= 1
            time.sleep(5)
    raise Exception("Could not connect to the database after multiple attempts")

# Function to generate random timestamps
def random_timestamp(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def insert_data(start):
    conn = get_db_connection()
    cur = conn.cursor()

    users_data = {
        'user_id': list(range(start, start+10)),
        'username': [f'user_{i}' for i in range(start, start+10)],
        'email': [f'user{i}@example.com' for i in range(start, start+10)],
        'created_at': [random_timestamp(datetime(2024, 8, 10, 12, 0, 0), datetime(2024, 8, 10, 14, 0, 0)) for _ in range(10)]
    }
    users_df = pd.DataFrame(users_data)

    for i in range(len(users_df)):
        # Check if email already exists
        cur.execute("SELECT COUNT(*) FROM users WHERE email = %s", (users_df.iloc[i]['email'],))
        if cur.fetchone()[0] == 0:
            cur.execute(
                "INSERT INTO users (username, email, created_at) VALUES (%s, %s, %s)",
                (users_df.iloc[i]['username'], users_df.iloc[i]['email'], users_df.iloc[i]['created_at'])
            )

    # Insert data into 'sessions' table
    cur.execute("SELECT user_id FROM users")
    user_ids = [row[0] for row in cur.fetchall()]
    print(f"Fetched User IDs: {user_ids}")

    sessions_data = {
        'user_id': [int(random.choice(user_ids)) for _ in range(20)],
        'session_start': [random_timestamp(datetime(2024, 8, 10, 12, 0, 0), datetime(2024, 8, 10, 14, 0, 0)) for _ in range(20)],
        'session_end': [random_timestamp(datetime(2024, 8, 10, 14, 0, 1), datetime(2024, 8, 10, 16, 0, 0)) for _ in range(20)],
        'device_info': [f'device_{i}' for i in range(1, 21)],
        'location': [f'location_{i}' for i in range(1, 21)],
        'network_type': [random.choice(['WiFi', '4G', '5G']) for _ in range(20)],
        'app_version': [f'v{random.randint(1, 5)}.0' for _ in range(20)]
    }
    sessions_df = pd.DataFrame(sessions_data)

    for i in range(len(sessions_df)):
        cur.execute(
            "INSERT INTO sessions (user_id, session_start, session_end, device_info, location, network_type, app_version) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (int(sessions_df.iloc[i]['user_id']), sessions_df.iloc[i]['session_start'], sessions_df.iloc[i]['session_end'],
             sessions_df.iloc[i]['device_info'], sessions_df.iloc[i]['location'], sessions_df.iloc[i]['network_type'],
             sessions_df.iloc[i]['app_version'])
        )

    # Insert data into 'metrics' table
    cur.execute("SELECT session_id FROM sessions")
    session_ids = [row[0] for row in cur.fetchall()]
    print(f"Fetched Session IDs: {session_ids}")

    metrics_data = {
        'session_id': [int(random.choice(session_ids)) for _ in range(50)],
        'timestamp': [random_timestamp(datetime(2024, 8, 10, 12, 0, 0), datetime(2024, 8, 10, 16, 0, 0)) for _ in range(50)],
        'talked_time': [int(random.randint(0, 3600)) for _ in range(50)],
        'microphone_used': [random.choice([True, False]) for _ in range(50)],
        'speaker_used': [random.choice([True, False]) for _ in range(50)],
        'voice_sentiment': [random.choice(['Positive', 'Negative', 'Neutral']) for _ in range(50)]
    }
    metrics_df = pd.DataFrame(metrics_data)

    for i in range(len(metrics_df)):
        cur.execute(
            "INSERT INTO metrics (session_id, timestamp, talked_time, microphone_used, speaker_used, voice_sentiment) VALUES (%s, %s, %s, %s, %s, %s)",
            (int(metrics_df.iloc[i]['session_id']), metrics_df.iloc[i]['timestamp'].to_pydatetime(), 
            int(metrics_df.iloc[i]['talked_time']), 
            bool(metrics_df.iloc[i]['microphone_used']), 
            bool(metrics_df.iloc[i]['speaker_used']), 
            metrics_df.iloc[i]['voice_sentiment'])
        )

    conn.commit()
    cur.close()
    conn.close()

@app.route('/populate')
def populate():

    with app.app_context():
        insert_data(0)

    conn = get_db_connection()
    cur = conn.cursor()
    # Fetch users
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()

    # Fetch sessions
    cur.execute('SELECT * FROM sessions;')
    sessions = cur.fetchall()

    # Fetch metrics
    cur.execute('SELECT * FROM metrics;')
    metrics = cur.fetchall()

    cur.close()
    conn.close()
    # insert_data(14)
    return render_template('index.html', users=users, sessions=sessions, metrics=metrics)


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    # Fetch users
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()

    # Fetch sessions
    cur.execute('SELECT * FROM sessions;')
    sessions = cur.fetchall()

    # Fetch metrics
    cur.execute('SELECT * FROM metrics;')
    metrics = cur.fetchall()

    cur.close()
    conn.close()
    # insert_data(14)
    return render_template('index.html', users=users, sessions=sessions, metrics=metrics)

@app.route('/delete')
def delete_data():
    conn = get_db_connection()
    cur = conn.cursor()

    # Delete content from the tables
    cur.execute('DELETE FROM metrics;')
    cur.execute('DELETE FROM sessions;')
    cur.execute('DELETE FROM users;')
    
    # Commit the transaction
    conn.commit()

    # Fetch the empty tables to pass to the template
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()

    cur.execute('SELECT * FROM sessions;')
    sessions = cur.fetchall()

    cur.execute('SELECT * FROM metrics;')
    metrics = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('index.html', users=users, sessions=sessions, metrics=metrics)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')