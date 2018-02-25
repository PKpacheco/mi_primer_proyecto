from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.portfolio_show, name='show_portfolios'),


]

