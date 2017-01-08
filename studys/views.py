from django.shortcuts import render,get_object_or_404
from .models import Articles,Methods
# Create your views here.
def index(request):
    #find latest_article in Article list
    latest_article = Articles.objects.order_by('-time')[:1]
    context = {'latest_article':latest_article,}
    return render(request,'studys/index.html',context)

def article_list(request):
    all_articles = Articles.objects.all()
    content = {'all_articles':all_articles}
    return render(request,'studys/article_list.html',content)

def article_detail(request, article_id):
    article = get_object_or_404(Articles,pk=article_id)
    return render(request,'studys/article_detail.html',{'article':article})

def method_list(request):
    all_methods = Methods.objects.all()
    content = {'all_methods':all_methods}
    return render(request,'studys/method_list.html',content)

def method_detail(request):
    method = get_object_or_404(Methods,pk=method_id)
    return render(request,'studys/method_detail.html',{'method':method})

def about(request):
    return render(request,'studys/about.html')
