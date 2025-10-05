from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blogger/index.html')

def art(request, numart):
    if numart in [1, 2, 3]:
        return render(request, f"blogger/art{numart}.html")
    return render(request, "blogger/art_not_found.html")