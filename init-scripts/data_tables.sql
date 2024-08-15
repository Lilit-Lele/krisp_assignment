-- create users table, each user name should have a unique identifier, and  username cannot be null,
-- the user_id is primary key, it makes sure that each row is uniquely identifiable
-- the email must be unique and cannot be null, the timestamp is created when the user is created, 
-- the default value is current time  
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- create session table, session_id is piriamy key, it is a uniq identifier for each table
-- foreign key referenced 'users' table to link each session to a specific user
-- the session start time cannot be null, the end time can be null, if the session is still ongoing
-- the session duration is automatically calculated by the difference of start and end times
CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    session_start TIMESTAMP NOT NULL,
    session_end TIMESTAMP,
    session_duration INT GENERATED ALWAYS AS (EXTRACT(EPOCH FROM (session_end - session_start))) STORED,
    device_info VARCHAR(255),
    location VARCHAR(255),
    network_type VARCHAR(50),
    app_version VARCHAR(50)
);


-- Create the 'metrics' table to store metrics related to user sessions
-- metric_id is primary key, it is unique identifier for each metric record
-- timstamp is the time when reccord is created and cannot be null
CREATE TABLE metrics (
    metric_id SERIAL PRIMARY KEY,
    session_id INT REFERENCES sessions(session_id),
    timestamp TIMESTAMP NOT NULL,
    talked_time INT,
    microphone_used BOOLEAN,
    speaker_used BOOLEAN,
    voice_sentiment VARCHAR(50)
);

-- SELECT * FROM metrics
