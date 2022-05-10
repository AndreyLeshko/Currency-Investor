from django.shortcuts import render
from django.http import HttpResponse
from .Custom_func import Investing_securities


def show_securities(request):
    all = Investing_securities.portfolio_securities()
    all_sec = {'all':all}
    Investing_securities.security_graph()
    return render(request, 'Frame/Investing_favorite_securities.html', all_sec)

def show_menu(request):
    return render(request, 'Frame/menu.html')
    # return render(request, 'base.html')

def start_page(request):
    return HttpResponse('Hello')

def blog(request):
    return render(request, 'Blog/blog-main.html')