from django.shortcuts import render
from .models import PersonalData

def portfolio_show(request):
    person = PersonalData.objects.all()
    context = {'person': person}

    return render(request, 'portfolios/portfolio_show.html', context)

