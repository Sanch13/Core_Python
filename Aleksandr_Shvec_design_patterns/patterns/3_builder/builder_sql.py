"""
Напиши Builder для создания SQL-запросов.
Требования:
Продукт: класс SQLQuery, который хранит части запроса и может вывести финальный SQL.
Строитель: SQLQueryBuilder с методами:

select(*fields) — выбрать поля (например, "name", "age")
from_table(table) — указать таблицу
where(condition) — добавить условие (можно вызывать несколько раз)
order_by(field, direction="ASC") — сортировка
limit(n) — лимит
build() — вернуть объект SQLQuery
"""


class SQLQuery:
    def __init__(
            self,
            fields: list[str],
            table: str,
            conditions: list[str] | None = None,
            order_field: str | None = None,
            order_direction: str | None = None,
            limit_value: int | None = None,
    ):
        self.fields = fields
        self.table = table
        self.conditions = conditions or []
        self.order_field = order_field
        self.order_direction = order_direction
        self.limit_value = limit_value

    def __str__(self) -> str:
        query = "SELECT "
        fields = ", ".join(self.fields)
        query += fields
        query += f"\nFROM {self.table}"
        if self.conditions:
            query += "\nWHERE "
            query += " AND ".join(self.conditions)

        if self.order_field:
            query += f"\nORDER BY {self.order_field} {self.order_direction or "ASC"}"

        if self.limit_value:
            query += f"\nLIMIT {str(self.limit_value)}"

        return query


class SQLQueryBuilder:
    def __init__(self):
        self._fields = []
        self._table = ""
        self._conditions = []
        self._order_field = ""
        self._order_direction = ""
        self._limit_value = None

    def select(self, *fields: str):
        self._fields = list(fields)
        return self

    def from_table(self, table: str):
        self._table = table
        return self

    def where(self, condition: str):
        self._conditions.append(condition)
        return self

    def order_by(self, field, direction="ASC"):
        self._order_field = field
        self._order_direction = direction
        return self

    def limit(self, value):
        self._limit_value = value
        return self

    def build(self):
        if not self._fields:
            raise ValueError("No fields specified")
        if not self._table:
            raise ValueError("No table specified")

        return SQLQuery(
            fields=self._fields,
            table=self._table,
            conditions=self._conditions,
            order_field=self._order_field,
            order_direction=self._order_direction,
            limit_value=self._limit_value,
        )


if __name__ == '__main__':
    # sql = SQLQuery(
    #     fields=["name", "age"],
    #     table="users",
    #     conditions=["age >= 18", "name = Bob"],
    #     # order_field="name",
    #     # order_direction="ASC",
    #     # limit_value=5,
    # )
    # print(sql)
    builder = SQLQueryBuilder()
    query = (builder
             .select("name", "age")
             .from_table("users")
             .where("age > 18")
             .where("age < 20")
             .order_by("name")
             .limit(10)
             .build()
             )
    print(query)
