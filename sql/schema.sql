-- HR analytics schema
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    role TEXT,
    salary REAL,
    hire_date TEXT
);
