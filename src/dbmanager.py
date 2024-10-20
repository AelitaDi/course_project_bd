import psycopg2


class DBManger:
    """
    Класс для работы с базой данных (Postgres).
    """

    # def __init__(self, name: str, params: dict[str, str]) -> None:
    #     """
    #     Инициализация экземпляра класса.
    #     """
    #     self._name = "postgres"
    #     self._params = params

    def get_companies_and_vacancies_count(self) -> tuple:
        """
        Метод получения количества компаний и вакансий в БД.
        """
        pass

    def get_all_vacancies(self) -> list[dict]:
        """
        Метод получения списка всех вакансий.
        """
        pass

    def get_avg_salary(self) -> float:
        """
        Метод получения средней зп по вакансиям.
        """
        pass

    def get_vacancies_with_higher_salary(self) -> list[dict]:
        """
        Метод получения всех вакансий, у которых зп выше средней.
        """
        pass

    def get_vacancies_with_keyword(self) -> list[dict]:
        """
        Метод получения выборки вакансий по ключевому слову.
        """
        pass
