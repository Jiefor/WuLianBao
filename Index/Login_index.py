from Common.GetDriver import GetDriver

class Login_Index(object):
    def __init__(self):
        self.dr=GetDriver().dr
    def UserName(self):
        try:
            self.username=self.dr.find_element_by_id('com.meilin.wulianbao:id/userId_EditText')
        except Exception as error:
            assert False,'未找到用户名输入框'
        return self.username
    def PassWord(self):
        try:
            self.password=self.dr.find_element_by_id('com.meilin.wulianbao:id/password_EditText')
        except Exception as error:
            assert False,'未找到密码输入框'
        return self.password
    def RememberPassword(self):
        try:
            self.rememberpassword=self.dr.find_element_by_id('com.meilin.wulianbao:id/regist_checkBox')
        except Exception as error:
            assert False,'未找记住密码复选框'
        return self.rememberpassword
    def ForgetPassword(self):
        try:
            self.forgetpassword=self.dr.find_element_by_id('com.meilin.wulianbao:id/forgetPassword_textView')
        except Exception as error:
            assert False,'未找到忘记密码'
        return self.forgetpassword
    def LoginButton(self):
        try:
            self.loginbutton=self.dr.find_element_by_id('com.meilin.wulianbao:id/next_button')
        except Exception as error:
            assert False,'未找到登录按钮'
        return self.loginbutton
    def Regist(self):
        try:
            self.regist=self.dr.find_element_by_id('com.meilin.wulianbao:id/now_login')
        except Exception as error:
            assert False,'未找到注册'
        return self.regist