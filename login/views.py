from login.models import Users
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import Context, loader
import json
from django.http import HttpResponse
from django.test import TestCase
from django.test.client import Client


import tests
import StringIO
import unittest



SUCCESS               =   1
ERR_BAD_CREDENTIALS   =  -1
ERR_USER_EXISTS       =  -2
ERR_BAD_USERNAME      =  -3
ERR_BAD_PASSWORD      =  -4

@csrf_exempt
def index(request):
    return render_to_response('client.html')



@csrf_exempt
def login(request):
    requestData = json.loads(request.body)
    username = requestData['user']
    password = requestData['password']
    count = Users().login(username, password)
    
    if count == -1:
        return HttpResponse(json.dumps({'errCode' : -1}), content_type = "application/json")
    return HttpResponse(json.dumps({'errCode' : 1, 'count' : count}), content_type = "application/json")

@csrf_exempt
def add(request):
    requestData = json.loads(request.body)
    username = requestData['user']
    password = requestData['password']
    count = Users().add(username, password)
    
    if count == -2 :
        return HttpResponse(json.dumps({'errCode' : -2}), content_type = "application/json")
    if count == -3 :
        return HttpResponse(json.dumps({'errCode' : -3}), content_type = "application/json")
    if count == -4 :
        return HttpResponse(json.dumps({'errCode' : -4}), content_type = "application/json")
    return HttpResponse(json.dumps({'errCode' : 1, 'count' : count}), content_type = "application/json")

@csrf_exempt
def resetFixture(request):
    count = Users().TESTAPI_resetFixture()
    if (count == 1):
        return HttpResponse(json.dumps({'errCode' : 1}), content_type = "application/json")

@csrf_exempt
def unitTests(request):
    buffer = StringIO.StringIO()
    suite = unittest.TestLoader().loadTestsFromTestCase(tests.UnitTests)
    result = unittest.TextTestRunner(stream = buffer, verbosity = 2).run(suite)
    rv = {"totalTests": result.testsRun, "nrFailed": len(result.failures), "output": buffer.getvalue()}
    return HttpResponse(json.dumps(rv), content_type = "application/json")