import threading


class MainModel():
    '''
        datamodel 一个单例模式的数据mod
    '''
    mutex = threading.Lock()
    instance = None
    def __init__(self):
        self.datamodel = {}
        self.getData={}
        self.threads=[]
        self.view={}
        self.events={}
        self.match_queue=[]
        self.max_threads=20
        self.crawlLock=False


    @staticmethod
    def GetInstance():
        if (MainModel.instance is None):
            MainModel.mutex.acquire()
            if (MainModel.instance is None):
                MainModel.instance = MainModel()
            else:
                MainModel.mutex.release()

        return MainModel.instance