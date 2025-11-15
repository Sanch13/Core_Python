"""
Абстрактная фабрика — это порождающий паттерн проектирования, который позволяет создавать семейства
связанных объектов, не привязываясь к конкретным классам создаваемых объектов.

---------------------------------------------------------------------------------

В контексте паттернов проектирования:
Для Абстрактной фабрики лучше использовать ABC, потому что:
✅ Явно показываешь намерение создать иерархию
✅ Ошибки ловятся в рантайме, а не только в IDE
✅ Это классический ООП-паттерн, и ABC тут естественнее
"""

from abc import ABC, abstractmethod
from typing import List, Any, Tuple


class Connection(ABC):
    @abstractmethod
    def connect(self) -> None:
        ...

    @abstractmethod
    def disconnect(self) -> None:
        ...

    @abstractmethod
    def create_cursor(self) -> "Cursor":
        ...


class Cursor(ABC):
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    @abstractmethod
    def execute(self, sql: str, params: List[Any] = None) -> None:
        ...

    @abstractmethod
    def fetchall(self):
        ...


class QueryBuilder(ABC):
    def __init__(self):
        self._table = None
        self._columns = []
        self._conditions = []
        self._params = []

    @abstractmethod
    def select(self, table: str, columns: List[str] = None) -> 'QueryBuilder':
        pass

    @abstractmethod
    def where(self, column: str, value: Any) -> 'QueryBuilder':
        pass

    @abstractmethod
    def build(self) -> Tuple[str, List[Any]]:
        """Возвращает (SQL-запрос, параметры)"""
        pass


class MySQLConnection(Connection):
    def connect(self):
        print("Connecting to MySQL...")

    def disconnect(self):
        print("Disconnecting from MySQL...")

    def create_cursor(self) -> 'Cursor':
        return MySQLCursor(self)


class MySQLCursor(Cursor):
    def execute(self, sql: str, params: List[Any] = None) -> None:
        print(f"Executing SQL... {sql}")

    def fetchall(self):
        # Имитация данных
        return [(1, "Alice"), (2, "Bob")]


class MySQLQueryBuilder(QueryBuilder):
    def select(self, table: str, columns: List[str] = None) -> 'QueryBuilder':
        self._table = table
        self._columns = columns or ["*"]
        return self

    def where(self, column: str, value: Any) -> 'QueryBuilder':
        self._conditions.append(f"{column} = %s")  # MySQL использует %s
        self._params.append(value)
        return self

    def build(self) -> Tuple[str, List[Any]]:
        columns_str = ", ".join(self._columns)
        sql = f"SELECT {columns_str} FROM {self._table}"

        if self._conditions:
            sql += " WHERE " + " AND ".join(self._conditions)

        return sql, self._params


class PostgreSQLConnection(Connection):
    def connect(self):
        print("Connecting to PostgreSQL...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL...")

    def create_cursor(self) -> 'Cursor':
        return PostgreSQLCursor(self)


class PostgreSQLCursor(Cursor):
    def execute(self, sql: str, params: List[Any] = None) -> None:
        print(f"Executing SQL... {sql}")

    def fetchall(self):
        # Имитация данных
        return [(1, "Charlie"), (2, "Diana")]


class PostgreSQLQueryBuilder(QueryBuilder):
    def select(self, table: str, columns: List[str] = None) -> 'QueryBuilder':
        self._table = table
        self._columns = columns or ["*"]
        return self

    def where(self, column: str, value: Any) -> 'QueryBuilder':
        # PostgreSQL использует $1, $2, $3
        param_num = len(self._params) + 1
        self._conditions.append(f"{column} = ${param_num}")
        self._params.append(value)
        return self

    def build(self) -> Tuple[str, List[Any]]:
        columns_str = ", ".join(self._columns)
        sql = f"SELECT {columns_str} FROM {self._table}"

        if self._conditions:
            sql += " WHERE " + " AND ".join(self._conditions)

        return sql, self._params


class DBFactory(ABC):
    @abstractmethod
    def create_connection(self) -> Connection:
        ...

    @abstractmethod
    def create_query_builder(self) -> QueryBuilder:
        pass


class MySQLFactory(DBFactory):
    def create_connection(self) -> Connection:
        return MySQLConnection()

    def create_query_builder(self) -> QueryBuilder:
        return MySQLQueryBuilder()


class PostgreSQLFactory(DBFactory):
    def create_connection(self) -> Connection:
        return PostgreSQLConnection()

    def create_query_builder(self) -> QueryBuilder:
        return PostgreSQLQueryBuilder()


class DatabaseClient:
    def __init__(self, factory: DBFactory):
        self.factory = factory

    def run_query(self, table: str, column: str, value: Any):
        conn = self.factory.create_connection()
        conn.connect()

        try:
            cursor = conn.create_cursor()

            builder = self.factory.create_query_builder()
            sql, params = builder.select(table).where(column, value).build()

            cursor.execute(sql, params)
            results = cursor.fetchall()
            return results
        finally:
            conn.disconnect()

    def __repr__(self):
        return f"{self.factory.__class__.__name__}"


if __name__ == '__main__':
    mysql_client = DatabaseClient(MySQLFactory())
    res = mysql_client.run_query("users", "age", 25)
    print(f"Result from {mysql_client}: {res}")

    postgres_client = DatabaseClient(PostgreSQLFactory())
    res = postgres_client.run_query("users", "age", 25)
    print(f"Result from {postgres_client}: {res}")
