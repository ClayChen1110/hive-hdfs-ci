"""Main entry point for the application."""

from pyhive import hive


def check_database_exists(db_name="product", host="localhost", port=10000):
    """
    Check if a Hive database exists.
    
    Args:
        db_name: Name of the database to check
        host: Hive server host
        port: Hive server port
        
    Returns:
        bool: True if database exists, False otherwise
    """
    try:
        # Connect to Hive
        conn = hive.Connection(host=host, port=port, username='hive')
        cursor = conn.cursor()
        
        # Show all databases
        cursor.execute("SHOW DATABASES")
        databases = [row[0] for row in cursor.fetchall()]
        
        # Check if database exists
        exists = db_name in databases
        
        if exists:
            print(f"✓ Database '{db_name}' exists")
        else:
            print(f"✗ Database '{db_name}' does not exist")
        
        cursor.close()
        conn.close()
        
        return exists
        
    except Exception as e:
        print(f"Error checking database: {e}")
        return False


def main():
    """Main function."""
    check_database_exists("product")


if __name__ == "__main__":
    main()
