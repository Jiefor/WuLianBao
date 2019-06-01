import  unittest
from Common.GetDriver import GetDriver
from Index.Login_index import Login_Index
from Index.Home_Index import Home_Index
from Index.BaoXiu_Index import BaoXiu_Index
from Index.BaoXiuList_Index import BaoXiuList_Index
from Tools.DL import singleton
from Tools.Move import Move
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr=GetDriver().dr
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test001(self):
        Login_Index().username.send_keys('18503119985')
        Login_Index().password.send_keys('88998600')
        Login_Index().regist.click()