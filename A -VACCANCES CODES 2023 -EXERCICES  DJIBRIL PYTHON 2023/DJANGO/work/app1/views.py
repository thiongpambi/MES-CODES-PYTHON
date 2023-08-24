from django.shortcuts import render

# Create your views here.
def index(request):
    ctx ={}
    return render(request,"app1/index.html",{})

def table():
    tab = []
    for i in range(10):
        tab.append(i*2)
    return tb