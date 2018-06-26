-- Create user table if it doesn't already exist
CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY,
                        name TEXT, height REAL);

-- Create goal table if it doesn't already exist
CREATE TABLE IF NOT EXISTS goal(goal_id INTEGER PRIMARY KEY,
                        user INTEGER,
                        goal INTEGER,
                        date TEXT,
                        FOREIGN KEY(user) REFERENCES users(user_id));

-- Create track table if it doesn't already exist
CREATE TABLE IF NOT EXISTS track(track_id INTEGER PRIMARY KEY,
                        user INTEGER,
                        weight REAL,
                        pcent REAL
                        bmi REAL,
                        date TEXT,
                        FOREIGN KEY(user) REFERENCES users(user_id));
