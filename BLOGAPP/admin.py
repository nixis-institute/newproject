from django.contrib import admin
from .models import *
# Register your models here.

# class show_list1(admin.ModelAdmin):
#     show_list = ('title','contain','author_name')

admin.site.register(BLOG_Table1)
# admin.site.register(option)
admin.site.register(Author_Details)