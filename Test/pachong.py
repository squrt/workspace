import urllib
import urllib3
import re
from django.http.response import HttpResponse


def pachong(req):
    sock = urllib.request.urlopen(r'http://www.baidu.com/')
    h = sock.read()
    h = (h).decode('utf8')
    print(h)
    # match = pattern.match(h) 
    # if match:
    #     list=match.group()
    pattern = re.compile(r'src="(http://.+?\.jpg)" ')
    list = re.findall(pattern, h)
    i = 1
    for l in list:
        try:
            # urllib.request.urlretrieve(l,'%s.jpg'%i)
            i += 1
        except:
            continue

    print(1)
    return HttpResponse(h)


def pachong3(req):
    method = urllib3.request.RequestMethods(None)
    response = method.urlopen(method='post', url='www.baidu.com')
    data = response.read()
    print(data)
    return HttpResponse('OK')
