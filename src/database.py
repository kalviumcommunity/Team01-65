"""Database helpers for the HR analytics project."""


def get_connection_string():
    """Return the database connection string from environment configuration."""
    return "sqlite:///team1_hr_analytics.db"
