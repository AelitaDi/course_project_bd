from src.hh_api import HeadHunterAPI


def main() -> None:
    """
    Главная функция проекта для взаимодействия с пользователем.
    :return: None
    """
    default_companies = ["HeadHunter", "ПАКС", "Level Group", "Роскосмос", "институт теплотехники",
                         "сколково", "Дело жизни", "SkyPro", "ГИБДД", "DatsTeam"]
    query = input("""Введите названия компаний через пробел, информацию о вакансиях которых вы хотели бы получить:
(По умолчанию будут использованы активные вакансии компаний:
HeadHunter, ПАКС, Level Group, Роскосмос, институт теплотехники, Сколково, Дело жизни, SkyPro, ГИБДД, DatsTeam) \n""").split()
    if query:
        companies_keywords = query
    else:
        companies_keywords = default_companies
    companies = HeadHunterAPI().get_companies(companies_keywords)
    for company in companies:
        vacancies = HeadHunterAPI().get_vacancies(company["company_id"])
        print(type(vacancies[0]["id"]))
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")
    #
    # list_vacancies_hh = HeadHunterAPI().get_vacancies(search_query)
    #
    # vacancies_list = get_vacancy_list(list_vacancies_hh)
    #
    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # if len(top_vacancies) == 0:
    #     print("По вашим параметрам не найдено ни одной вакансии.")
    # else:
    #     print_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
