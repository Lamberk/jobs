from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    industry = models.CharField(max_length=128, null=True, blank=True)
    telephone = models.CharField(max_length=32, null=True, blank=True)
    company_size = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    vacancies_count = models.IntegerField(null=True, blank=True)
    site_url = models.CharField(max_length=64, null=True, blank=True)
