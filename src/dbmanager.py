import psycopg2


class DBManager:
    """
    Класс для работы с базой данных (Postgres).
    """

    def __init__(self, name: str, params: dict[str, str]) -> None:
        """
        Инициализация экземпляра класса.
        """
        self._name = name
        self._params = params

    def get_companies_and_vacancies_count(self) -> list[tuple]:
        """
        Метод получения количества компаний и вакансий в БД.
        """
        conn = psycopg2.connect(dbname=self._name, **self._params)
        cur = conn.cursor()

        cur.execute(
            """SELECT company_name, COUNT(*)
            FROM vacancies JOIN companies USING (company_id)
            GROUP BY company_name
            ORDER BY COUNT(*) DESC;"""
        )
        rows = cur.fetchall()
        for row in rows:
            print(f"Название компании:\n{row[0]}\nКоличество открытых вакансий: {row[1]}\n")

        cur.close()
        conn.close()
        return rows

    def get_all_vacancies(self) -> list[tuple]:
        """
        Метод получения списка всех вакансий.
        """
        conn = psycopg2.connect(dbname=self._name, **self._params)
        cur = conn.cursor()
        cur.execute(
            """SELECT company_name, vacancy_name, salary, vacancy_url
                    FROM vacancies JOIN companies USING (company_id);"""
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_avg_salary(self) -> float:
        """
        Метод получения средней заработной платы по вакансиям.
        """
        conn = psycopg2.connect(dbname=self._name, **self._params)
        cur = conn.cursor()
        cur.execute("""SELECT AVG(salary) FROM vacancies;""")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return round(rows[0][0], 2)

    def get_vacancies_with_higher_salary(self) -> list[tuple]:
        """
        Метод получения всех вакансий, у которых зп выше средней.
        """
        conn = psycopg2.connect(dbname=self._name, **self._params)
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM vacancies
                    WHERE salary > (SELECT AVG(salary) FROM vacancies);"""
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_vacancies_with_keyword(self, keyword) -> list[tuple]:
        """
        Метод получения выборки вакансий по ключевому слову.
        """
        conn = psycopg2.connect(dbname=self._name, **self._params)
        cur = conn.cursor()
        cur.execute(
            f"""SELECT * FROM vacancies
                    WHERE vacancy_name
                    LIKE '%{keyword.lower()}%';"""
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
