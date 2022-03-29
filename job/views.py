from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import Job
from .forms import ApplyForm, AddJobForm
from .filters import JobFilter

# Create your views here.

def job_list(request):
    filter = JobFilter(request.GET, queryset=Job.objects.all())
    paginator = Paginator(filter.qs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'jobs': page_obj,
        'filter': filter.form
    }
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            current_apply = form.save(commit=False)
            current_apply.job = job_detail
            current_apply.save()

    form = ApplyForm()

    context = {
    'job': job_detail, 
    'form': form
    }
    return render(request, 'job/job_detail.html', context)  

@login_required
def add_job(request):
    
    if request.method == "POST":
        form = AddJobForm(request.POST, request.FILES)
        if form.is_valid():
            current_job = form.save(commit=False)
            current_job.owner = request.user
            current_job.save()
            return redirect(reverse('jobs:job_list'))
    form = AddJobForm()
    context = {
        'form': form
    }
    return render(request, 'job/add_job.html', context)