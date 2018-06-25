from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers

import json
class Task:
    def __init__(self, task_text="", task_id=0, completed=False):
        self.task_text = task_text
        self.task_id = task_id
        self.completed = completed
Tasks = []
def tasks(request):
    """tasks_list = json.loads(serializers.serialize('json', Tasks))
    return JsonResponse(tasks_list, safe=False)"""
    json_list = json.dumps([tsk.__dict__ for tsk in Tasks])
    return JsonResponse(json_list, safe=False)
def update(request):
    print(update)
    body_unicode = request.body.decode('utf-8')
    res = json.loads(body_unicode)
    num = int(res)
    Tasks[num].completed = True
    return HttpResponse("Task completed")

def new(request):
    body_unicode = request.body.decode('utf-8')
    res = json.loads(body_unicode)
    i = 1
    for e in Tasks:
        i += 1
    new_task = Tasks.append(Task(res,i, False))
    return HttpResponse("Created")

    
# Create your views here.
