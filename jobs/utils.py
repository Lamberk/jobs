import requests

from jobs.settings import SUPERJOB_TOKEN, SUPERJOB_API_URL


def get_companies_for_keyword(keyword):
    per_page = 100
    headers = {'X-Api-App-Id': SUPERJOB_TOKEN}
    params = {'keyword': keyword, 'count': per_page}
    companies = set()
    for i in range(5): # SuperJob отдает только 500 записей, 5 по 100
        params['page'] = i
        request = requests.get(SUPERJOB_API_URL.format('vacancies'), headers=headers, params=params)
        data = request.json()
        for elem in data['objects']:
            companies.add(elem['id_client'])
    companies.remove(0)
    return companies


def get_company_info(company):
    headers = {'X-Api-App-Id': SUPERJOB_TOKEN}
    request = requests.get(SUPERJOB_API_URL.format('clients')+str(company)+'/', headers=headers)
    return request.json()
