# WARNING: This is bad code on purpose.
# Hardcoded passwords are a major security risk.

def connect_to_database():
    username = "admin"
    password = "superSecretPassword123"  # Bandit should catch this!
    print(f"Connecting as {username}")

connect_to_database()
