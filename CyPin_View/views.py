from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.

def index_view(request):
    return render(request, "base.html")

def login_view(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")
        user_type = login_data.get("user_type")
        username = username + ":" + user_type
        user = authenticate(username=username, password=password)
        if user is not None:
            if(user_type == "head"):
                return redirect("home/home_head")
            elif user_type=="admin":
                return redirect("home/home_admin")
            elif user_type=="user":
                return redirect("home/home_user")
            else:
                return redirect("home")
        else:
            print("Not Authenticated")
        return HttpResponse("Hello There")
    else:
        return render(request, "base.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/home")
def home_admin(request):
    return HttpResponse("Hello Admin")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/home")
def home_head(request):
    return HttpResponse("Hello Head")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/home")
def home_user(request):
    return HttpResponse("Hello User")


