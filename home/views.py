from django.shortcuts import render
from job.models import Job, category
from job.filters import jobFilter
from django.db.models import Count
# Create your views here.
"""def home(request):
    return render(request,'home/index.html',{})"""







def home(request):
    job_filter = jobFilter(request.GET, queryset=Job.objects.all())
    total_jobs = Job.objects.count()
    filtered_jobs = job_filter.qs[:6] 
    categories = category.objects.annotate(num_jobs=Count('job'))
    context = {
        'jobs': filtered_jobs,  
        'categories': categories,
        'job_filter': job_filter,
        'total_jobs': total_jobs,  
    }
    return render(request, 'home/index.html', context)