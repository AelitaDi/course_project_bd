import psycopg2


class DBManger:
    """
    Класс для работы с базой данных (Postgres).
    """

    def __init__(self, name: str, params: dict[str, str]) -> None:
        """
        Инициализация экземпляра класса.
        """
        self._name = "postgres"
        self._params = params

    def create_database(self) -> None:
        """Метод для создания базы данных."""

        conn = psycopg2.connect(dbname=self._name, **self._params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE IF EXISTS {self._name}")
        cur.execute(f"CREATE DATABASE {self._name}")

        cur.close()
        conn.close()
