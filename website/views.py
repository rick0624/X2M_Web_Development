import re
from django.shortcuts import render
from django.utils import timezone
from .models import New
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
def main_page(request):
    return render(request, 'website/main_page.html', {})

def socialMedia(request):
    new_list = New.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(new_list, 3) # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'website/socialMedia_page.html', {'news': new_list, 'page_obj': page_obj,})

def new_detail(request,pk):
    new = get_object_or_404(New, pk=pk)
    return render(request, 'website/new_detail.html', {'new': new})