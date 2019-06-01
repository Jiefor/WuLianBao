from appium import webdriver


class GetDriver(object):
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'MI_6'
        desired_caps['appPackage'] = 'com.meilin.wulianbao'
        desired_caps['appActivity'] = '.OnStartActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 使用webdriver与appium创建连接（session）
        self.dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
