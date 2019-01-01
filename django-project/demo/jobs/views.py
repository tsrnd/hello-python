from django.shortcuts import render
from .models import Job
from django.http import Http404

# Create your views here.


def home(request):
    jobs = Job.objects
    return render(request, 'home.html', {'jobs': jobs})


def detail(request, job_id):
    try:
        job_detail = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'detail.html', {'job': job_detail})
