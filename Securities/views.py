from django.http import HttpResponse
from . import Investing_securities
from django.shortcuts import render

def show_securities(request):
    all = Investing_securities.portfolio_securities()
    all_sec = {'all':all}
    Investing_securities.security_graph()
    return render(request, 'Securities/Investing_favorite_securities.html', all_sec)

def show_menu(request):
    return render(request, 'Securities/menu.html')
    # return render(request, 'test.html')

