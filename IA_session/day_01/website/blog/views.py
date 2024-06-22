from django.shortcuts import render

# Create your views here.
def bloglist(request):
    blogs = [
    {"id":1,"title":"learn JS","author":"james","desc":"welcome to learn JS"},
    {"id":2,"title":"learn Django","author":"john","desc":"wlecome to learn Django"}
]
    return render(request,"blog/blogList.html",{"blogs":blogs})

def blogdetail(request,id):
    blogs = {
        1:{"title":"learn JS","author":"james","desc":"welcome to learn JS"},
        2:{"id":2,"title":"learn Django","author":"john","desc":"wlecome to learn Django"}
    }
    blogdetail = blogs.get(id)
    # print(blogdetail)
    return render(request,"blog/blogDetail.html",{"blog":blogdetail})