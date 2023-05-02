import mysql.connector


class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.config = config    # to send dict with params DB

    def __enter__(self) -> "cursor":
        self.conn = mysql.connector.connect(**self.config)  # Create a connect with DataBase
        # and save link in the self.conn
        self.cursor = self.conn.cursor()  # create cursor-object.
        return self.cursor   # return self.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()  # write to the DB immediately
        self.cursor.close()  # close the cursor-object.
        self.conn.close()  # close the connection with DB
