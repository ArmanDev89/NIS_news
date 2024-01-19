from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
<<<<<<< Updated upstream
    return render(request, 'site_back/index.html')
=======
    articles = Article.objects.all()
    return render(request, 'site_back/index.html', {'articles': articles})

def tag_viev(request, tag):
    articles = Article.objects.filter(tags=tag)
    return render(request, 'site_back/index.html', {'articles': articles})

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'site_back/article.html', {'article': article})

def admission(request):
    return render(request, 'site_back/admission.html')
>>>>>>> Stashed changes
