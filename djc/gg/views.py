from django.shortcuts import render
from datetime import datetime
from .tasks import add, mul

# Create your views here.
from django.http import HttpResponse


def index(request):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tr = add.delay(10,20)
    print(tr)
    context = {
        'dt':now,
        'tr':tr.task_id,
    }
    return render(request, 'gg/index.html', context=context)