from django.urls import path
from . import views


urlpatterns = [
    path('', views.default_top_headlines, name="topHeadLines"),
    path('cycat/<value>', views.top_headlines_with_country, name='home'),
    path('search/query', views.search, name='search'),
    path('contact', views.contact, name='contact')
]