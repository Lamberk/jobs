from django.http import Http404
from django.shortcuts import render
from jobs.models import Company


def index(request):
    companies = Company.objects.all()
    return render(request, 'jobs/index.html', {'companies': companies})
