from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Priority, Task


# Create your views here.

def task_list(request):
    tasks=Task.objects.all()

    # 1. get search, sort, filter values from request.GET
    search=request.GET.get('search', '') #'' denotes that default is empty
    sort=request.GET.get('sort', 'pub_date') #'pub_date' denotes that by default tasks are sorted based on pub_date
    priority=request.GET.get('priority','') #'' denotes that default is empty
    is_completed=request.GET.get('is_completed','') #'' denotes that default is empty

    # 2. apply search if present
    if(search!=''):
        tasks=tasks.filter(title__icontains=search)
    
    # 3. apply priority/completion filter if present
    if(priority!=''):
        tasks=tasks.filter(priorityLevel__priority_idx=priority)
    if(is_completed!=''):
        tasks=tasks.filter(is_completed=(is_completed=='True'))
    # 4. apply ordering
    if(sort!='pub_date'):
        tasks=tasks.order_by(sort)
    
    # 5. pass to template via context
    return render(request,'tasks/index.html',{'tasks':tasks})