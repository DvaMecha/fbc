from bs4 import BeautifulSoup
import Model.MainModel
import Crawler.Crawl as crawl

model = Model.MainModel.MainModel.GetInstance()


def analysisHtml(h: object, w: str) -> object:
    ruleFun = {'odds': ruleBy500,
               'list': getMatchList}
    soup = BeautifulSoup(h, 'html5lib')
    obj = ruleFun[w](soup)
    return obj


def oddTo10(u, d):
    return (u + d) / d


def getMatchList(soup):
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
                obj[lgid]["lgname"] + "联赛目前似乎没有比赛，请过段时间再试")
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
        model.view['main'].outPutText("目前似乎没有所需联赛的比赛，过段时间再试吧", True)
    return obj


def ruleBy500(soup):
    obj = {}
    # obj['odd'] = soup.find_all("tbody", attrs={"id": "main-tbody"})
    for item in model.datamodel['league'].items():
        lg = soup.find_all("tr", attrs={"data-mid": item[1]['mid_500']})
        lgid = item[0]
        obj[lgid] = {}
        obj[lgid]["lgname"] = item[1]['name']
        obj[lgid]['matchs'] = []
        for i in lg:
            matchId = i.get("data-fid")
            obj[lgid]['matchs'].append(matchId)
            matchInfo = {
                "t1": i.select(".text_right > a")[0].get_text(),
                "t2": i.select(".text_left > a")[0].get_text(),
                "lc": i.select("td")[2].get_text()}
            odds = rulBy500getAll(matchId)
            obj[lgid][matchId] = {'info': matchInfo,
                                  'odds': odds}
            t1 = "[" + obj[lgid]["lgname"] + "][" + matchInfo["lc"] + \
                 "]" + matchInfo["t1"] + " vs " + matchInfo["t2"] + ":"
            t2 = ''
            for cpItem in model.datamodel['web']:
                cid = cpItem['cid_500']
                if cid == 0:
                    continue
                k = cpItem["id"]
                t2 += '<[' + cpItem["name"] + ']:' + odds[k]['w'] + \
                      '|' + odds[k]['d'] + '|' + odds[k]['l'] + '>'

            t = t1 + t2
            model.view['main'].outPutText(t + '\n')
    return obj


def rulBy500getAll(tid):
    url = 'http://odds.500.com/fenxi/ouzhi-' + tid + '.shtml'
    corrent = crawl.getDatas(url)
    soup = BeautifulSoup(corrent, 'html5lib')
    obj = {}
    for cpItem in model.datamodel['web']:
        cid = cpItem['cid_500']
        if cid == 0:
            continue
        k = cpItem["id"]
        obj[k] = {}
        tds = soup.find(
            id="datatb").find(
            "tr", attrs={
                "id": cid}).find(
            class_="pl_table_data").find_all("tr")[1].find_all("td")
        obj[k]["w"] = tds[0].get_text()
        obj[k]["d"] = tds[1].get_text()
        obj[k]["l"] = tds[2].get_text()
    return obj
