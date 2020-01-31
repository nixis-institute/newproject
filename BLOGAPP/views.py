from django.shortcuts import render,HttpResponse
from django.shortcuts import HttpResponseRedirect
from .models import *
from django.contrib.auth import login,logout,authenticate
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
    
    # ts = BLOG_Table1.objects.filter(author_id = request.user.id).order_by('-id')
    # print(dir(ts))
    ts.reverse()
    # print(ts[0].title)
    return render(request,'Home.html',{'T':ts,"user":request.user})
    

def CreateTable(request):
    cr = BLOG_Table1.objects.all()
    return render(request,"create.html",{'C1':cr})

def CTable(request):
    d = request.POST
    tl = d.get('Title')
    con = d.get("cont")
    author = request.user.id
    # at = d.get("Aname")
    # dt = d.get("date")
    # pb = d.get("publish")
    BLOG_Table1.objects.create(title=tl,contain=con,author_id=author)
    return HttpResponseRedirect('/')


def ContainPage(request,a):
    cp = BLOG_Table1.objects.get(id=a)
    return render(request,"Contain.html",{'CP1':cp})


def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def Login_page(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect("/")

    if(request.method == 'POST'):        
        user = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user,password=password)
        if(user is not None):
            login(request,user)
            return HttpResponseRedirect("/")
        else:
            return render(request,"Login.html") 
    else:
        return render(request,"Login.html")

def LGdata(request):
    pd = request.POST
    unm = pd.get("Username")
    pnm = pd.get('pass')
    LoginPage.objects.create(Uname=unm,passw=pnm)
    return HttpResponseRedirect('/')


def AboutPage(request):
    return render(request,"About.html")


def Policy(request):
    return render(request,"policy.html")


def Contact(request):
    return render(request,"contact.html")