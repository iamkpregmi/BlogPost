from django.contrib import admin
from myblog.models import myblog

class myblogAdmin(admin.ModelAdmin):
    list_display = ("blog_title","blog_desc")

admin.site.register(myblog,myblogAdmin)
