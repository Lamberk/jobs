from django.core.management.base import BaseCommand

from jobs.utils import get_companies_for_keyword, get_company_info
from jobs.models import Company


class Command(BaseCommand):
    help = 'Load new vacancies from SuperJob'

    def handle(self, *args, **options):

        companies = get_companies_for_keyword('Продавец консультант')
        for company in companies:
            info = get_company_info(company)
            company_object = dict()
            if info.get('industry'):
                company_object['industry'] = info.get('industry')[0]['title']
            else:
                company_object['industry'] = None
            company_object['site_url'] = info.get('url')
            company_object['company_size'] = info.get('staff_count')
            company_object['vacancies_count'] = info.get('vacancy_count')
            company_object['address'] = info.get('address')
            company_object['title'] = info.get('title')
            for k,v in company_object.items():
                if not company_object[k]:
                    company_object[k] = ''
            c, created = Company.objects.get_or_create(
                id=company,
                defaults=company_object,
            )
