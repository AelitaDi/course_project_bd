from typing import Any

import psycopg2


def create_database(database_name: str, parameters: dict) -> None:
    """
    Создание базы данных и таблиц кампаний и вакансий.
    """

    conn = psycopg2.connect(dbname="postgres", **parameters)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **parameters)

    with conn.cursor() as cur:
        cur.execute(
            """
                CREATE TABLE companies (
                    company_id VARCHAR,
                    company_name VARCHAR(255) NOT NULL,
                    company_url VARCHAR,
                    
                    CONSTRAINT pk_companies_company_id PRIMARY KEY (company_id));
            """
        )

    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE vacancies (
                vacancy_id VARCHAR(20),
                company_id VARCHAR(20),
                vacancy_name VARCHAR NOT NULL,
                salary real,
                vacancy_url TEXT,
                description TEXT,

                CONSTRAINT pk_vacancies_vacancy_id PRIMARY KEY (vacancy_id),
                CONSTRAINT fk_vacancies_companies FOREIGN KEY(company_id) REFERENCES companies(company_id)
            );
        """
        )

    conn.commit()
    conn.close()


def save_data_to_database(
    companies_data: list[dict[str, Any]], vacancies_data: list[dict], params: dict, database_name: str = "headhunter"
) -> None:
    """
    Сохранение данных о компаниях и вакансиях в базу данных.
    """

    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        for company in companies_data:
            cur.execute(
                """
                INSERT INTO companies (company_id, company_name, company_url)
                VALUES (%s, %s, %s)
                """,
                (company["company_id"], company["company_name"], company["company_url"]),
            )

        for vacancy in vacancies_data:
            cur.execute(
                """
                INSERT INTO vacancies (vacancy_id, company_id, vacancy_name, salary, vacancy_url, description)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    vacancy["vacancy_id"],
                    vacancy["company_id"],
                    vacancy["name"],
                    vacancy["salary"],
                    vacancy["url"],
                    vacancy["description"],
                ),
            )

    conn.commit()
    conn.close()
