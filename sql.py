import difflib
import dimsim
import pymysql
import unicodedata
from pypinyin import lazy_pinyin, Style

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='mycy',
    charset='utf8'
)

cursor = conn.cursor()
"""

sql = 'select * from cy where name = "马达成功"'
rows = cursor.execute(sql) 


cursor.close()


conn.close()


if rows >= 0:
    print('连接数据库成功')
else:
    print('连接数据库失败')
"""


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


def sql(newstring, prelist):
    list = []
    list2 = []
    cursor = pymysql.cursors.SSCursor(conn)
    sql = "select * from cy"
    cursor.execute(sql)
    # row = cursor.fetchone()
    # print(row)
    while True:
        row = cursor.fetchone()
        if type(row) is tuple:
            # print(1)
            cy = "".join(row[2])
            res = unicodedata.normalize('NFKD', cy).encode('ascii', 'ignore')
            rescy = (res.decode()).replace(" ", "")
            # print(res.decode())
            if string_similar(rescy, newstring) > 0.7:
                # print(res.decode())
                # print(row)
                style = Style.TONE3
                listi = lazy_pinyin(row[1], style=style)
                if len(listi) == 4:
                    list.append(listi)
                    list2.append(row[1])
            # if row[1] == right:
            # print(row)
        if not row:
            break
        # print(row)
    #print(list)
    #print(list2)
    try:
        distlist = []
        for a in list:
            # print(a)
            if len(a) == 4:
                dist = dimsim.get_distance(a, prelist, pinyin=True)
                distlist.append(dist)
    except:
        pass

    #print(len(distlist))
    #print(len(list2))
    #print(distlist.index(min(distlist)))
    #print(distlist[distlist.index(min(distlist))])
    #print(list2[distlist.index(min(distlist))])

    return list2[distlist.index(min(distlist))]

#sql("yongwangzhiqian", ['yong3', 'wang3', 'zhi2', 'qian2'])

def sqlmean(cyname):
    cy = cyname
    #sql = "select * from orange where color = %s"
    #cursor.execute(sql, color)
    cursor = pymysql.cursors.SSCursor(conn)
    sql = 'select content from cy where name = %s'
    #print(sql)
    rows = cursor.execute(sql,cy)
    #print(cursor.fetchone())

    return cursor.fetchone()[0]

def onesql(string):
    list = []
    list2 = []
    distancelist = []
    cursor = pymysql.cursors.SSCursor(conn)
    sql = "select * from cy"
    cursor.execute(sql)
    while True:
        row = cursor.fetchone()
        if type(row) is tuple:
            # print(1)
            cy = "".join(row[2])
            res = unicodedata.normalize('NFKD', cy).encode('ascii', 'ignore')
            rescy = (res.decode()).replace(" ", "")
            #print(res.decode())
            distancelist.append(string_similar(res.decode(), string))
            list.append(res.decode())
            list2.append(row[1])
            # print(res.decode())
            # print(list)
        if not row:
            break
    index = distancelist.index(max(distancelist))
    #print(distancelist)
    #print(index)
    #print(distancelist[index])

    #print(list[index])
    #print(list2[index])

    return  list[index] ,list2[index]
#print(sqlmean('鸟语花香'))

#onesql("yongwangshiqian")



def aftersql(newstring, prelist):
    list = []
    list2 = []
    dict = {}
    cursor = pymysql.cursors.SSCursor(conn)

    sql = "select * from cy"

    cursor.execute(sql)
    # row = cursor.fetchone()
    # print(row)
    while True:
        row = cursor.fetchone()

        if type(row) is tuple:
            # print(1)
            cy = "".join(row[2])
            res = unicodedata.normalize('NFKD', cy).encode('ascii', 'ignore')
            rescy = (res.decode()).replace(" ", "")
            # print(res.decode())
            if string_similar(rescy, newstring) > 0.7:
                # print(res.decode())
                # print(row)
                style = Style.TONE3
                listi = lazy_pinyin(row[1], style=style)
                #print(listi)
                try:
                    if len(listi) == 4:
                        dict[row[1]] = dimsim.get_distance(listi, prelist, pinyin=True)
                except:
                    pass
            # if row[1] == right:
            # print(row)
        if not row:
            break

        # print(row)
    m = min(dict.keys(), key=(lambda x: dict[x]))
    #print(m)
    #print(dict[m])
    #print(dict)
    #print(dict)

    return m

c = aftersql("niyuhuaxiang", ['ni3', 'yu2', 'hua1', 'xiang1'])
#print(c)
