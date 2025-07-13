
#insecure_credentials.py
def connect_to_database():
  username="admin"
  password="admin"
  db_url="mysql://localhost:3306/mydatabase"
  connection = f"mysql+pymysql://{username}:{password}@{db_url}"
  return connection

if __name__ == "__main__":
  db_connection = connect_to_database()
  print("connected to database")
