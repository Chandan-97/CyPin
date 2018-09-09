from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.cache import cache
from .models import *

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
        return HttpResponse("Error Login")
    else:
        return render(request, "base.html")

def home_admin(request):
    print("Kill")
    return HttpResponse("Hello Admin")

def home_head(request):
    return HttpResponse("Hello Head")

def home_user(request):
    return HttpResponse("Hello User")

def add_item(request):
    if request.POST:
        form_data = request.POST.dict()
        item_name = form_data.get("item_name")
        item_model = form_data.get("item_model")
        item_quantity = form_data.get("item_quantity")
        # writing hash function to get the item id
        item_id = -1
        item_cost = form_data.get("item_cost")

        print(item_id, item_name, item_model, item_quantity, item_cost)
        try:
            Items(item_id=item_id, item_name=item_name, item_model=item_model, item_cost=item_cost, item_count=item_quantity).save()
            print("Item Saved")
        except Exception as e:
            print("Item Saving Error")
        return HttpResponse("Item Added")

    else:
        return render(request, "add_items.html")

def Logout(request):
    try:
        del request.session['session_id']
    except Exception as e:
        print("Error Deleting Session")

    try:
        logout(request)
        cache.clear()
        print("Logout Successfully")
    except Exception as e:
        print("Error Logging out user")
    return HttpResponseRedirect("/")



