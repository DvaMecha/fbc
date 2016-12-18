# coding=utf-8
from view.QtView import *
from PyQt5.QtWidgets import QApplication
import Crawler.CrawlSave as fileManager
from Crawler import Crawl
import Model.MainModel as Model
import json
import requests
import sys

# 定义变量
eventModel = {}
websites = ()
model = Model.MainModel.GetInstance()



def initApp():
    jsfile = 'datamodel.json'
    fp = open(jsfile, 'r')
    model.datamodel = json.load(fp)
    fp.close()
    model.crawler = Crawl.Crawler()
    showHelp()


def initEvent():
    model.events = {
        'init': initApp,
        'runCrawl': runCrawl,
        'save': fileManager.saveData,
        'showHelp': showHelp,
        'getMatchs': getMatchList
    }
    return model.events


def runCrawl():
    main.outPutText('开始抓取', True)
    model.crawler.runCrawler('odds500')
    # model.getData['all'] = d
    # model.getData[t] = rule.analysisHtml(d, t)

def getMatchList():
    main.outPutText('开始获取比赛列表', True)
    model.crawler.runCrawler('list')

def showHelp():
    main.outPutText(
        '''
            Welcome!
            这是一个简单的操作界面，而且程序没有经过打包
            Start按钮会抓取所有网站的所有场次数据，这个过程非常慢，大概会持续几分钟
            抓取速度和当天的比赛多少有直接关系，比赛越多读取越慢，和网速也有一定的关系，
            之后用多线程优化一下应该能快点，也会加入一个读取的进度条
            List按钮会抓取今天的比赛列表，之后会做个抓取单场比赛数据的功能
            Save按钮会生成一个txt文件保存数据到output文件夹中
            现在显示的数据格式是
            [联赛名][轮次]主队 vs 客队:<[博彩公司]:胜|平|负>
            存储的数据格式是
            {
                联赛Id:{
                    lgname:联赛名，
                    matchs:[比赛1id，比赛2id...]
                    比赛1Id:{
                        info:{t1:主队名，t2:客队名，lc:轮次}
                        adds:{
                            博彩网站AId:{
                                w:主队胜赔率
                                d:主队平赔率
                                l:主队负赔率
                            },
                            博彩网站BId:{...}
                            ...
                        }
                    }
                    比赛2:{...}
                    ...
                }
                联赛Id:{...}
                ...
            }
            这个存储的数据格式就是最后要导入到模型中的数据
            ''', True)


# 获得窗口对象


app = QApplication(sys.argv)
main = QtView(initEvent())
model.view['main'] = main
initApp()
app.exec_()
