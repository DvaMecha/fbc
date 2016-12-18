import Model.MainModel
import requests
import time
from bs4 import BeautifulSoup
from Crawler.CrawlRule import *

model = Model.MainModel.MainModel.GetInstance()
defurl = 'http://odds.500.com/'


def creatWebHeard():
    # 构造请求报头
    webheaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}
    return webheaders


def getDatas(url):
    header = creatWebHeard()
    req = requests.get(url, headers=header)
    encoding = req.apparent_encoding
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
    encode_content = req.content.decode(encoding, 'replace')
    return encode_content


class Crawler():

    def __init__(self):
        self.ruleFun = {'odds500': ruleBy500, 'list': self.getMatchList}
        pass

    def runCrawler(self, t):
        model.view['main'].outPutText(
            model.datamodel['info']['start'], True)
        model.startTime = time.time()
        if model.crawlLock:
            model.view['main'].outPutText(model.datamodel['info']['start'], True)
            return
        model.crawlLock = True
        d = getDatas(defurl)
        soup = BeautifulSoup(d, 'html5lib')
        obj = self.ruleFun[t](soup)
        model.getData[t]=obj
        return obj

    def getAllodds(self):
        pass

    def getMatchList(self, soup):
        obj = {}
        # obj['odd'] = soup.find_all("tbody", attrs={"id": "main-tbody"})
        flag = False
        for item in model.datamodel['league'].items():
            lg = soup.find_all("tr", attrs={"data-mid": item[1]['mid_500']})
            lgid = item[0]
            obj[lgid] = {}
            obj[lgid]["lgname"] = item[1]['name']
            obj[lgid]['matchs'] = []
            if len(lg) == 0:
                model.view['main'].outPutText(
                    obj[lgid]["lgname"] + model.datamodel['info']['lgnomatch'])
                continue
            else:
                flag = True
                for i in lg:
                    matchId = i.get("data-fid")
                    obj[lgid]['matchs'].append(matchId)
                    matchInfo = {
                        "t1": i.select(".text_right > a")[0].get_text(),
                        "t2": i.select(".text_left > a")[0].get_text(),
                        "lc": i.select("td")[2].get_text()}
                    obj[lgid][matchId] = {'info': matchInfo}
                    t = "[" + obj[lgid]["lgname"] + "][" + matchInfo["lc"] + \
                        "]" + matchInfo["t1"] + " vs " + matchInfo["t2"] + ":"
                    model.view['main'].outPutText(t + '\n')

        if not flag:
            model.view['main'].outPutText(model.datamodel['info']['nomatch'], True)
        return obj
