import threading
import Model.MainModel
import time
from Crawler import CrawlRule
model = Model.MainModel.MainModel.GetInstance()

class CrawlThread(threading.Thread):
    def __init__(self, match: object, threadId):
        threading.Thread.__init__(self)
        self.match = match
        self.threadId = threadId

    def run(self):
        print("开始线程：", self.threadId)
        self.result=treadfun(self.match, self.threadId)

    def getResult(self):
        return self.result

def treadfun(match: object, threadId):
    print(threadId, "号队列的目标", match['matchid'])
    #main.outPutText("开始抓取"+match['txt'])
    odds = CrawlRule.rulBy500getAll(match['matchid'])
    t2 = ''
    for cpItem in model.datamodel['web']:
        cid = cpItem['cid_500']
        if cid == 0:
            continue
        k = cpItem["id"]
        if not odds[k]:
            continue
        t2 += '<[' + cpItem["name"] + ']:' + odds[k]['w'] + '|' + odds[k]['d'] + '|' + odds[k]['l'] + '>'
    t = match['txt'] + t2
    model.view['main'].outPutText(t + '\n')
    return odds


def startThread(obj):
    threadId = 1
    while model.threads or model.match_queue:
        for thread in model.threads:
            if not thread.is_alive():
                re=thread.getResult()
                m=thread.match
                obj[m['lgid']][m['matchid']]['odds']=re
                model.threads.remove(thread)
                print("已抓取" + thread.match['txt']+"剩余"+str(len(model.match_queue))+"场")
                print("退出线程：", thread.threadId)
        while len(model.threads) < model.max_threads and model.match_queue:
            # can start some more threads
            newthread = CrawlThread(model.match_queue.pop(), threadId)
            threadId+=1
            newthread.start()
            model.threads.append(newthread)
            # all threads have been processed
            # sleep temporarily so CPU can focus execution on other threads
        time.sleep(1)
    else:
        model.endTime = time.time()
        s = model.endTime - model.startTime
        model.view['main'].outPutText("Time consuming : " + str(int(s)) + 's')
        model.view['main'].outPutText("抓取结束，点击save保存为txt文件")
        model.crawlLock = False
    return obj
