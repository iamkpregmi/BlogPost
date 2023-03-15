from django.shortcuts import render
from myblog.models import myblog

def home(request):
    myresult = myblog.objects.all().order_by("-id")
    data = {
        "myresult": myresult
    }
    return render(request,"index.html",data)
