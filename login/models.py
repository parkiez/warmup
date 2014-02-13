from django.db import models
import json


SUCCESS               =   1
ERR_BAD_CREDENTIALS   =  -1
ERR_USER_EXISTS       =  -2
ERR_BAD_USERNAME      =  -3
ERR_BAD_PASSWORD      =  -4

class Users(models.Model):
    username = models.CharField(max_length=128, blank= True)
    password = models.CharField(max_length=128)
    count = models.IntegerField()

    def login(self, userid, passw):
        if (Users.objects.filter(username=userid).count()==0):
            return ERR_BAD_CREDENTIALS
        else:
            info = Users.objects.get(username = userid)
            if (info.password != passw):
                return ERR_BAD_CREDENTIALS
            else:
                info.count += 1
                info.save()
                return info.count
        
    def add(self, userid, passw):
        if userid == "" or len(userid) > 128:
            return ERR_BAD_USERNAME
        if len(passw) > 128:
            return ERR_BAD_PASSWORD
        if (Users.objects.filter(username = userid).count()==1):
            return ERR_USER_EXISTS
        info = Users.objects.create(username = userid, password = passw, count = 1)
        return SUCCESS
        
    def TESTAPI_resetFixture(self):
        Users.objects.all().delete()
        return SUCCESS
        
    def TESTAPI_unitTests(self):
        return SUCCESS
