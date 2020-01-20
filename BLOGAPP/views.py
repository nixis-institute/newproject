from django.shortcuts import render,HttpResponse
from django.shortcuts import HttpResponseRedirect
from .models import *
# import mysql.connector
# db = mysql.connector.connect(user='root',password="1986",host='localhost')
# print(dir(db))
# import mysql.connector

# Create your views here.
# db = mysql.connector.connect("localhost",'nixis','1986')
# db = connector.connect("localhost",'nixis','1986')
# qu = ('create database Data_of_websites')
# ins = ('insert into table title ({})')

# cur = db.cursor()
# print(cur.execute(qu))
# dbt = cur.execute(qu)
# print(dbt is not None)
# for i in dbt:
    # print(i)

# def Homepage(request):
#     return HttpResponse("This is home Page")


# def viewpage(request):
#     return HttpResponse("This is view page")


# def Detailpage(request):
#     return HttpResponse("This is Detail page")

# # def All(request):
#     # return HttpResponse("{}\n{}\n{}".format(Homepage,viewpage,Detailpage))

# def page(request,a):
#     return HttpResponse("This multiple pages {}".format(a))


# def Onefun(request):
    # return HttpResponse("This is home page {}".format(Homepage(request)))
    # return HttpResponse("This is view page {}".format(viewpage(request)))


def Homepage(request):
    ts = BLOG_Table1.objects.all().order_by('-id')
    # print(dir(ts))
    ts.reverse()
    # print(ts[0].title)
    return render(request,'Home.html',{'T':ts})
    

def CreateTable(request):
    cr = BLOG_Table1.objects.all()
    return render(request,"create.html",{'C1':cr})

def CTable(request):
    d = request.POST
    tl = d.get('Title')
    con = d.get("cont")
    at = d.get("Aname")
    # dt = d.get("date")
    # pb = d.get("publish")
    BLOG_Table1.objects.create(title=tl,contain=con,author_name=at)
    return HttpResponseRedirect('/')


def ContainPage(request,a):
    cp = BLOG_Table1.objects.get(id=a)
    return render(request,"Contain.html",{'CP1':cp})


def Login_page(request):
    lg = LoginPage.objects.all()
    return render(request,"Login.html",{'L1':lg})

def LGdata(request):
    pd = request.POST
    unm = pd.get("Username")
    pnm = pd.get('pass')
    LoginPage.objects.create(Uname=unm,passw=pnm)
    return HttpResponseRedirect('/')


def AboutPage(request):
    return render(request,"About.html")
