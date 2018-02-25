from django.shortcuts import render

def portfolio_show(request):
    return render(request, 'portfolios/portfolio_show.html', {})

