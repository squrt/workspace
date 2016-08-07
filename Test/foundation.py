import os
import gzip
# import cStringIO
import xml.dom.minidom


def dom_parser(path):
    vs_cnt = 0
    str_s = ''
    #     file_io = cStringIO.StringIO()
    #     xm = gzip.open(gz,'rb')
    file = open(path, 'r+')
    print("已读入：%s.\n解析中：" % (os.path.abspath(path)))
    doc = xml.dom.minidom.parseString(file.read())
    bulkPmMrDataFile = doc.documentElement
    # 读入子元素
    enbs = bulkPmMrDataFile.getElementsByTagName("eNB")
    measurements = enbs[0].getElementsByTagName("measurement")
    objects = measurements[0].getElementsByTagName("object")
    # 写入csv文件
    for object in objects:
        vs = object.getElementsByTagName("v")
        vs_cnt += len(vs)
        for v in vs:
            print(enbs[0].getAttribute("id") + ' ' + object.getAttribute("id") + ' ' + \
                  object.getAttribute("MmeUeS1apId") + ' ' + object.getAttribute(
                "MmeGroupId") + ' ' + object.getAttribute("MmeCode") + ' ' + \
                  object.getAttribute("TimeStamp") + ' ' + v.childNodes[0].data + '\n')  # 获取文本值
        #             file_io.write(enbs[0].getAttribute("id")+' '+object.getAttribute("id")+' '+\
        #             object.getAttribute("MmeUeS1apId")+' '+object.getAttribute("MmeGroupId")+' '+object.getAttribute("MmeCode")+' '+\
        #             object.getAttribute("TimeStamp")+' '+v.childNodes[0].data+'\n')  #获取文本值
        #     str_s = (((file_io.getvalue().replace(' \n','\r\n')).replace(' ',',')).replace('T',' ')).replace('NIL','')
    file.close()
    #     file_io.close()
    return (str_s, vs_cnt)


if __name__ == '__main__':
    dom_parser(r'/home/kqb/桌面/t.xml')
