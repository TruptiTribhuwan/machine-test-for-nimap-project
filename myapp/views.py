from django.shortcuts import redirect, render
from .models import User, client
# Create your views here.
def home(request):
    std=client.objects.all()
    return render(request, "myapp/home.html",{"std":std})

def registration(request):
    if request.method=="POST":
      roll=request.POST.get("roll")
      name=request.POST.get("name")
      cb=request.POST.get("cb")
      pn=request.POST.get("pn")
      data=client(roll=roll,name=name,createdby=cb,Project=pn)
      data.save()
    return render(request,"myapp/registration.html")

def delete(request,roll):
    s=client.objects.get(pk=roll)
    s.delete()

    return redirect("/home/")

def edit(request,roll):
    std=client.objects.get(pk=roll)
    # data1=User.objects.all()
   
    # context={
    #     "data1":data1
    # }
    if request.method=="POST":
      roll=request.POST.get("roll")
      name=request.POST.get("name")
      createdby=request.POST.get("cb")
      Project=request.POST.get("pn")

      
      std.roll=roll
      std.name=name
      std.createdby=createdby
      std.Project=Project

      std.save()
      return redirect("/home/")

    return render(request,"myapp/edit.html",{'std':std},)

# def doedit(request,roll):
#     roll=request.POST.get("roll")
#     name=request.POST.get("name")
#     createdby=request.POST.get("createby")
#     Project=request.POST.get("Project")

#     std=client.objects.get(pk=roll)
    

#     std.roll=roll
#     std.name=name
#     std.createdby=createdby
#     std.Project=Project

    # std.save()

    # return redirect("/home/")