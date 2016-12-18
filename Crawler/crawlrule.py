from bs4 import BeautifulSoup
import Model.MainModel
from Crawler import Crawl as crawl
from Crawler import CrawlThread as thread
import sys
model = Model.MainModel.MainModel.GetInstance()




def oddTo10(u, d):
    return (u + d) / d

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
            matchInfo = {"t1": i.select(".text_right > a")[0].get_text(),
                             "t2": i.select(".text_left > a")[0].get_text(), "lc": i.select("td")[2].get_text()}

            t1 = "[" + obj[lgid]["lgname"] + "][" + matchInfo["lc"] + "]" + matchInfo["t1"] + " vs " + matchInfo[
                    "t2"] + ":"

            model.match_queue.append({'matchid': matchId, 'txt': t1, 'lgid': lgid})
            # odds = rulBy500getAll(matchId)
            obj[lgid][matchId] = {'info': matchInfo}

    result = thread.startThread(obj)

    return result


def rulBy500getAll(tid) -> object:
    u = 'http://odds.500.com/fenxi/ouzhi-' + tid + '.shtml'
    corrent = crawl.getDatas(u)
    soup = BeautifulSoup(corrent, 'html5lib')
    obj = {}
    try:
        for cpItem in model.datamodel['web']:
            cid = cpItem['cid_500']
            if 0 == cid:
                continue
            k = cpItem["id"]
            obj[k] = {}
            try:
                datatb = soup.find(id="datatb")
                trs = datatb.find("tr", attrs={"id": cid})
                if not trs:
                    continue
                tds = trs.find(class_="pl_table_data").find_all("tr")[1].find_all("td")
            except:
                print("Unexpected error:", tid, sys.exc_info()[0])
                print(cpItem)
            obj[k]["w"] = tds[0].get_text()
            obj[k]["d"] = tds[1].get_text()
            obj[k]["l"] = tds[2].get_text()
    except:
        print("Unexpected error:", sys.exc_info()[0])
    return obj
