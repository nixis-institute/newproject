from django.db import models
import mysql.connector
# Create your models here.
from datetime import datetime
from django.contrib.auth.models import User


db = mysql.connector.connect(user='root',password="1986",host='localhost',database="")
cur = db.cursor()
# dbt = cur.execute(qu)
# qu = ("show databases")
# d = cur.execute(qu)
# for i in d:
#     print(i)

op = (
    ('PB','Public'),
    ('PV',"Private"),
)

class Author_Details(models.Model):
    Aut_name = models.CharField(max_length=20)
    Aut_country = models.CharField(max_length=20)
    Aut_Email = models.EmailField()

    def __str__(self):
        return self.Aut_name

# class option(models.Model):
    # option = models.CharField(max_length=20,)

class BLOG_Table1(models.Model):
    title = models.CharField(max_length=100,null=True)
    contain = models.TextField()
    # auther_name = models.CharField(max_length=20)
    # author_name = models.CharField(max_length=20,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    Date = models.DateTimeField(default=datetime.now(),null=True)
    # Tm = models.TimeField()
    # publish = models.CharField(max_length=20,choices=op,default="Private")
    def __str__(self):
        return self.title
        # return self.auther_name
# ins = ("insert into titles values({})".format(contain))


class LoginPage(models.Model):
    Uname = models.CharField(max_length=20,blank=True)
    passw = models.TextField(blank=True)
    
    def __str__(self):
        return self.Uname
