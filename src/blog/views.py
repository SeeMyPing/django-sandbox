from datetime import datetime
from django.shortcuts import render

def index(request):
    date = datetime.today()
    
    return render(request, 'blog/index.html', context={
        "date": date,
        "request": request
    })