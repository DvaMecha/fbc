import requests



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


def getWebInfo(url):
    req = creatWebHeard()
    r = requests.get(url, headers=req)
    print(type(r))
    print(r.status_code)
    print(r.encoding)
    # print r.text
    print(r.cookies)
    info = {
        'encoding': r.encoding,
        'info': r.cookies,
        'code': r.status_code}
    return info
