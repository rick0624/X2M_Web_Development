from django.contrib import admin
from .models import New
from .models import Contact

# Register your models here.
class NewAdmin(admin.ModelAdmin):
    list_display = ('title','created_date', )
    list_display_links = ('title', ) 
    list_filter = ('created_date', )
    search_fields = ('title','created_date', )
    list_per_page = 10
    list_max_show_all = 200 
    
class ContactAdmin(admin.ModelAdmin):
    '''list display對象'''
    list_display = ('first_name', 'last_name','email','phone','message',)
    list_display_links = ('first_name', ) 
    '''filter對象'''
    list_filter = ('first_name','email','phone', )
    '''search對象'''
    search_fields = ('first_name', 'last_name','email','phone','message',)
    '''一頁顯示的文章數'''
    list_per_page = 10
    '''一頁顯示的文章數 when clicking show all'''
    list_max_show_all = 200 
# Register your models here.
admin.site.register(New,NewAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.site_header = 'X2M administration'
admin.site.site_title = 'X2M'
admin.site.index_title = 'Site administration'
