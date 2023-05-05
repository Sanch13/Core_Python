import mysql.connector


class ConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass


class SQLError(Exception):
    pass


class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.config = config  # to send dict with params DB

    def __enter__(self) -> "cursor":
        try:  # try to connect to the DB
            self.conn = mysql.connector.connect(**self.config)  # Create a connect with DataBase
            # and save link in the self.conn
            self.cursor = self.conn.cursor()  # create cursor-object.
            return self.cursor  # return self.cursor()
        except mysql.connector.errors.InterfaceError as error:
            raise ConnectionError(error)  # display error
        except mysql.connector.errors.ProgrammingError as error:
            raise CredentialsError(error)  # display error

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()  # write to the DB immediately
        self.cursor.close()  # close the cursor-object.
        self.conn.close()  # close the connection with DB
