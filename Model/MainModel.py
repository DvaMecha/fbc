import threading


class MainModel():
    '''
        datamodel 一个单例模式的数据mod
    '''

    # 定义静态变量实例
    instance = None
    mutex = threading.Lock()
    datamodel = {}
    getData={}
    view={}
    event={}
    def __init__(self):
        pass

    @staticmethod
    def GetInstance():
        if (MainModel.instance is None):
            MainModel.mutex.acquire()
            if (MainModel.instance is None):
                MainModel.instance = MainModel()
            else:
                MainModel.mutex.release()

        return MainModel.instance