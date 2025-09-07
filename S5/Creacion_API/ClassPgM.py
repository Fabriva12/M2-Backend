import psycopg2

class PgManager():
    def __init__(self, host, user, password, dbname,  port ):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.port = port

        self.connection = self.create_connection()
        if self.connection :
            print ("Connected to database")
            self.cursor = self.connection.cursor()
    
    def create_connection(self):
        try:
            connection = psycopg2.connect(
                host = self.host,
                user = self.user,
                password = self.password, 
                dbname = self.dbname, 
                port = self.port 
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None
        
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")

    def execute_query(self, query, *args):
        self.cursor.execute(query, args)
        self.connection.commit()
        if self.cursor.description:
            results = self.cursor.fetchall()
            return results