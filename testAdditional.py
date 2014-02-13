import unittest
import os
import testLib

class TestBadUsername(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testBadUsername(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : "alkjdlkaAskljfswlqwroiqnalkdjfalksjflaksjdlfkajsdlkjaflakjfslaksjfdlaksjdflakdjflaksjdflakjsflaksjdflakjflakjflakjfdlakjflaksjflaksjflakjfslkajflakjflkajakjflkjw", 'password' : ''} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)

class TestBadPassword(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testBadPassword(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : "alkjdlkaAskljfswlqwroiqnalkdjfalksjflaksjdlfkajsdlkjaflakjfslaksjfdlaksjdflakdjflaksjdflakjsflaksjdflakjflakjflakjfdlakjflaksjflaksjflakjfslkajflakjflkajakjflkjw"} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD)

class TestAddMultipleUsers(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):

        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
        
    def testAddTwoUsers(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user2', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)

class TestAddEmptyUsername(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testAddEmptyUsername(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)

class TestAddDuplicateUsername(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):

        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testAddDuplicate(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_USER_EXISTS)

class TestLoginEmptyUsername(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testLoginEmptyUsername(self):
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)

class TestLoginIncorrectPassword(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):

        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testLoginIncorrectgPassword(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'pw'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)

class TestLoginIncorrectUser(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):
  
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testLoginIncorrectUser(self):
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)

class TestDBCleared(testLib.RestTestCase):
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):
        
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testDBCleared(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = {} )
        respData2 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData2, errCode = ERR_BAD_CREDENTIALS)

