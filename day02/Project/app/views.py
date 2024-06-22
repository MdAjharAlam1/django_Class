from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def reverse_pgm(request):
    if request.method=="POST":
        get_input = request.POST.get('inp')
        output = get_input[::-1]
        mydict ={"get_input":get_input,"output":output}
    
    return render(request,'about.html',mydict)