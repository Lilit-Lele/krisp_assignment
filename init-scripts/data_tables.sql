CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

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
