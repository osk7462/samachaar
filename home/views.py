from django.shortcuts import render
from pythonCodes.news_api import NewsApi

news = NewsApi()


def default_top_headlines(request):
    print("top headlines")
    context = {'news': news.get_news()['articles']}
    return render(request, 'home/index.html', context=context)


def top_headlines_with_country(request, value):
    news.set_country_or_category(value)
    context = {'news': news.get_news()['articles']}
    return render(request, 'home/index.html', context=context)


def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        language = request.POST['language']
        sort_by = request.POST['sortBy']
        context = {'news': NewsApi.get_static_news(query, language, sort_by)['articles']}
        return render(request, 'home/index.html', context=context)


def contact(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        description = request.POST['description']
        context={'contact':{'name': name, 'email':email, 'subject': subject, 'description': description}}
    return render(request, 'home/contact.html', context=context)