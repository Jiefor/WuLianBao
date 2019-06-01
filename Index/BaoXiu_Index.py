from Common.GetDriver import GetDriver
from appium.webdriver.common.touch_action import TouchAction
from Tools.Move import Move
class BaoXiu_Index(object):
    def __init__(self):
        self.dr=GetDriver().dr
    def Voice_input(self):
        self.aaa=self.dr.find_element_by_id('com.meilin.wulianbao:id/iv_voice')
        try:
            self.voice_input=TouchAction(self.dr).long_press(self.aaa,5000).perform()
        except:
            Move().Move_up()
            self.dr.find_element_by_id('com.meilin.wulianbao:id/rr_voice').click()
        return self.voice_input
    def Write_input(self):
        try:
            self.write_input=self.dr.find_element_by_id('com.meilin.wulianbao:id/word')
        except:
            self.dr.find_element_by_id('com.meilin.wulianbao:id/rr_write').click()
        return self.write_input
    def Video_input(self):
        pass
    def BaoXiu_Button(self):
        try:
            self.baoxiu_button=self.dr.find_element_by_id('com.meilin.wulianbao:id/next_button')
        except Exception as error:
            assert False,'未找到按钮'
        return self.baoxiu_button
