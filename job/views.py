from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job
from .forms import ApplyForm, AddJobForm

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj
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

def add_job(request):
    
    if request.method == "POST":
        form = AddJobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
    form = AddJobForm()
    context = {
        'form': form
    }
    return render(request, 'job/add_job.html', context)