from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
def index_view(request):
    print(str(request.user.is_authenticated()))
    return render(request, "base.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
    print(str(request.user.is_authenticated()))
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")
        user_type = login_data.get("user_type")
        # username = username + ":" + user_type
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if(user_type == "head"):
                return HttpResponse("Home Head")
                # return redirect("home_head")
            elif user_type=="admin":
                # return HttpResponse("Home Admin")
                return render(request, "admin_home.html")
                # return redirect(request, "home_admin")
            elif user_type=="user":
                return HttpResponse("Home User")
                # return redirect("home_user")
            else:
                return render(request, "base.html")
                # return redirect("home")
        else:
            print("Not Authenticated")
        return HttpResponse("Hello There")
    else:
        return render(request, "base.html")

def home_admin(request):
    print("Kill")
    return HttpResponse("Hello Admin")

def home_head(request):
    return HttpResponse("Hello Head")

def home_user(request):
    return HttpResponse("Hello User")



