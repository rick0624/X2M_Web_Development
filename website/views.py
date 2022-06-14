import re
from urllib import request
from django.shortcuts import render
from django.utils import timezone
from .models import New
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .form import NewForm,ContactForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.
def main_page(request):
    return render(request, 'website/main_page.html', {})

def about_company(request):
    return render(request, 'website/about_company.html', {})

def about_business(request):
    return render(request, 'website/about_business.html', {})

def socialMedia(request):
    new_list = New.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    num_per_page = 10
    if request.GET.get('p') != None:
            num_per_page = request.GET.get('p')
            request.session['p'] = num_per_page
    else:
        num_per_page = request.session['p']
    paginator = Paginator(new_list, num_per_page) # Show 3 contacts per page.
    page_number = 1
    if request.GET.get('page') != None:
         page_number = request.GET.get('page')
    total_page_num = paginator.num_pages

    if int(page_number)>int(total_page_num):  #確保新聞序號正確
        page_number = total_page_num

    page_obj = paginator.get_page(page_number)
    count = (int(page_number)-1)*int(num_per_page)
    if int(page_number)<=2:
        page_minus_2 = 0
    elif int(page_number)>total_page_num-2:
        page_minus_2 = total_page_num-5
    else:
        page_minus_2 = int(page_number)-3
    active_check_num = int(page_number)-1
    
    return render(request, 'website/socialMedia_page.html', {'page_obj': page_obj, 'total_page_num':range(total_page_num), 'count':count, 
    'page_number':int(page_number),'active_check_num':active_check_num, 'num_per_page':num_per_page, 'total_page':total_page_num, 'total_5':range(page_minus_2,page_minus_2+5)})

def new_detail(request,pk):
    new = get_object_or_404(New, pk=pk)
    new_list = New.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #published_date__lte : lte在這時間之後都會選到
    new_list = new_list.filter(~Q(pk = pk))
    return render(request, 'website/new_detail.html', {'new': new, 'new_list':new_list[:5]})

def news_create(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('new_detail', pk=post.pk)
    else:
        form = NewForm()
    return render(request, 'website/news_edit.html', {'form': form})  #news_edit == news_create

def news_edit(request, pk):
    news = get_object_or_404(New, pk=pk)
    if request.method == "POST":
        form = NewForm(request.POST, instance=news)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('new_detail', pk=post.pk)
    else:
        form = NewForm(instance=news)
    return render(request, 'website/news_edit.html', {'form': form})

def news_remove(request, pk):
    post = get_object_or_404(New, pk=pk)
    post.delete()
    return redirect('socialMedia')

# def test(request,pk):
#     new = get_object_or_404(New, pk=pk)
#     new_list = New.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #published_date__lte : lte在這時間之後都會選到
#     new_list = new_list.filter(~Q(pk = pk))
#     return render(request, 'website/test.html', {'new': new, 'new_list':new_list[:5]})
 
# def setcookie():  
#     response = HttpResponse("Cookie Set")  
#     response.set_cookie('Test', 'javatest')  
#     return response  

# def getcookie(request):  
#     tutorial  = request.COOKIES['java-tutorial']  
#     return HttpResponse("java tutorials @: "+  tutorial); 

def contact_view(request):
    if request.method == 'POST':
        details = ContactForm(request.POST)
        if details.is_valid():
                form = details.save(commit = False)
                form.save()
                #send_mail(first_name+last_name,message,email,['ted87940@gmail.com',email]) #第一個欄位是email標題，最後一欄位是管理者的email 在setting中也要設定  
                #return redirect("/contact/")
                #return render(request, 'contact/success.html')
                return render(request, "contact/contact.html", {'form':details,'success':True})  
        else:
                #return render(request, 'contact/contact.html')
                return redirect("/contact/")
    else:
        form = ContactForm(None)
        return render(request, 'contact/contact.html', {'form': form})