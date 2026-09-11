#题1类的继承与再次编写
class car:
    def __init__(self,typ,pai):
        self.typ=typ
        self.pai=pai

    def start(self):
        print("成功启动")

    def stop(self):
        print("启动失败")

class taxi(car):
    def __init__(self,typ,pai,compy):
        super().__init__(typ,pai)
        self.compy=compy

    def start(self):
        print("乘客你好!")
        print(f"我是{self.compy}的,我的车牌是{self.pai},你要去哪?")

    def stop(self):
        print("目的地到了")

che = taxi("出租车","京A8888","长城汽车公司")
che.start()
che.stop()
