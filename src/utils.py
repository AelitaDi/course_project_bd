import psycopg2

from config.config import config


def create_database(database_name: str, params: dict):
    """
    Создание базы данных и таблиц кампаний и вакансий.
    """

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE companies (
                company_id VARCHAR(20),
                company_name VARCHAR(255) NOT NULL,
                company_url TEXT
                
                CONSTRAINT pk_companies_company_id PRIMARY KEY (company_id)
            );
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                vacancy_id VARCHAR(20),
                company_id VARCHAR(20),
                vacancy_name VARCHAR NOT NULL,
                salary real,
                vacancy_url TEXT,
                description TEXT
            
                CONSTRAINT pk_vacancies_vacancy_id PRIMARY KEY (vacancy_id)
                CONSTRAINT fk_vacancies_companies FOREIGN KEY(company_id) REFERENCES companies(company_id)
            );
        """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    params = config()
    create_database("HH", params)
