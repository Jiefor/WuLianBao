from Common.GetDriver import GetDriver
class Move(object):
    def __init__(self):
        self.dr=GetDriver().dr
        self.x=self.dr.get_window_size()['width']
        self.y=self.dr.get_window_size()['height']

    def Move_left(self):
        self.move_left=self.dr.swipe(self.x*0.9,self.y*0,self.x*0.1,self.y*0,1000)
        return self.move_left
    def Move_right(self):
        self.move_right=self.dr.swipe(self.x*0.1,self.y*0,self.x*0.9,self.y*0,1000)
        return self.move_right
    def Move_up(self):
        self.move_up=self.dr.swipe(self.x*0,self.y*0.9,self.x*0,self.y*0.1,1000)
        return self.move_up
    def Move_down(self):
        self.move_down=self.dr.swipe(self.x*0,self.y*0.1,self.x*0.1,self.y*0.9,1000)
        return self.move_down