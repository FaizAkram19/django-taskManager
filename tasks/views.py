from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Priority, Task
from datetime import date
from .forms import TaskForm


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
    context={"tasks":tasks} 
    return render(request,'tasks/index.html', context)

def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST, request.FILES or None) #FILES looks for any files or images that were uploaded, they won't be uploaded without it

        if form.is_valid():
            form.save()
            return redirect('index')# HTTP_REFERER points back to the page from where we came from.
                                                                     # we gave index as a fallback so that if we arent able to fallback 
                                                                     # to the last page, we can go back to the homepage.
    else:
        form=TaskForm() #if the request was GET, create an empty instance of the ModelForm
    
    return render(request, "tasks/taskform.html",{"form":form})

def edit_task(request, pk):
    task=get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        form=TaskForm(request.POST,  request.FILES or None, instance=task) #added instance=task to fill the form with prexisting data(if any)

        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form=TaskForm(instance=task)
    context={"form":form}
    return render(request,'tasks/taskform.html', context)

