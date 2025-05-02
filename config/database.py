import os

def get_database_uri():
    db_driver = os.getenv("DB_CONNECTION", "sqlite")

    if db_driver == "mysql":
        user = os.getenv("DB_USERNAME", "root")
        password = os.getenv("DB_PASSWORD", "")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", 3306)
        database = os.getenv("DB_DATABASE", "app")
        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    
    elif db_driver == "postgresql":
        user = os.getenv("DB_USERNAME", "postgres")
        password = os.getenv("DB_PASSWORD", "")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", 5432)
        database = os.getenv("DB_DATABASE", "app")
        return f"postgresql://{user}:{password}@{host}:{port}/{database}"

    # Default: SQLite
    db_path = os.getenv("DB_DATABASE", "app.sqlite")
    return f"sqlite:///{db_path}"
