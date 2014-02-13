from django.test import TestCase
from login.models import Users

SUCCESS               =   1
ERR_BAD_CREDENTIALS   =  -1
ERR_USER_EXISTS       =  -2
ERR_BAD_USERNAME      =  -3
ERR_BAD_PASSWORD      =  -4

class UnitTests(TestCase):
    def testReset(self):
        self.assertEquals(Users().TESTAPI_resetFixture(), SUCCESS)
    
    
    def testAddUser1(self):
        self.assertEquals(Users().add("user1", "pw"), SUCCESS)

    def testAddUser2(self):
        self.assertEquals(Users().add("user1", "pw"), SUCCESS)
        self.assertEquals(Users().add("user2", "pw"), SUCCESS)

    def testAddEmptyUser(self):
        self.assertEquals(Users().add("", "pw"),ERR_BAD_USERNAME)

    def testAddEmptyPassword(self):
        self.assertEquals(Users().add("user1", ""),SUCCESS)
    
    def testAddDuplicate(self):
        self.assertEquals(Users().add("user1", "pw"), SUCCESS)
        self.assertEquals(Users().add("user1", "pw"), ERR_USER_EXISTS)
    

    def testLoginNotExistUser(self):
        self.assertEquals(Users().login("user0", "pw"), ERR_BAD_CREDENTIALS)

    def testLoginEmptyUser(self):
        self.assertEquals(Users().login("", "pw"),ERR_BAD_CREDENTIALS)
    
    def testLoginCorrect(self):
        self.assertEquals(Users().add("user1", ""),SUCCESS)
        self.assertEquals(Users().login("user1", ""), 2)

    def testLoginCount(self):
        self.assertEquals(Users().add("user1", "pw"),1)
        self.assertEquals(Users().login("user1", "pw"),2)
        self.assertEquals(Users().login("user1", "pw"), 3)

    def testTwoUserSamePassword(self):
        self.assertEquals(Users().add("user1", ""),SUCCESS)
        self.assertEquals(Users().add("user2", ""),SUCCESS)

    def testLoginWithWrongPassword(self):
        self.assertEquals(Users().add("user1", "pw"), SUCCESS)
        self.assertEquals(Users().login("user", ""), ERR_BAD_CREDENTIALS)

    def testBadUsername(self):    self.assertEquals(Users().add("alkjdlkaAskljfswlqwroiqnalkdjfalksjflaksjdlfkajsdlkjaflakjfslaksjfdlaksjdflakdjflaksjdflakjsflaksjdflakjflakjflakjfdlakjflaksjflaksjflakjfslkajflakjflkajakjflkjw", ""), ERR_BAD_USERNAME)

    def testBadPassword(self):    self.assertEquals(Users().add("user1","alkjdlkaAskljfswlqwroiqnalkdjfalksjflaksjdlfkajsdlkjaflakjfslaksjfdlaksjdflakdjflaksjdflakjsflaksjdflakjflakjflakjfdlakjflaksjflaksjflakjfslkajflakjflkajakjflkjw"), ERR_BAD_PASSWORD)
    
    def testDBclear(self):
        Users().add("user1", "pw")
        Users().TESTAPI_resetFixture()
        self.assertEquals(Users().login("user1", "pw"), ERR_BAD_CREDENTIALS )