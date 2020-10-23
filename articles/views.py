from django.shortcuts import render
from .models import article
# Create your views here.

def article_gen(request):
    news = article.objects.all()
    context = {
        'news_list': list(reversed(news))
    }
    return render(request,'articles/index.html', context=context)
