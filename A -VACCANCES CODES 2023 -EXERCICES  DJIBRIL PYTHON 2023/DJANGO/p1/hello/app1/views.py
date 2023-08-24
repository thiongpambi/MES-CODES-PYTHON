from django.shortcuts import render

# Create your views here.
def tablemulti():
    tb = []
    for i in range(10):
        tb.append()
    return tb 
      
def index(request):
    ctx={'moi':'mamadou thiongane'}
    ctx['tab']=tablemulti()
    return render(request,'app1/index.html',ctx)

def about(request):
    ctx = {}
    return render(request,'app1/about.html',ctx)