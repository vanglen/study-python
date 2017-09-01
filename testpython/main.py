import pymysql.cursors
import urllib
import urllib2


class _Request():
    def __init__(self):
        pass

    def test(self):
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     db='test',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                cursor.execute(sql, ('webmaster@python.org',))
                result = cursor.fetchone()
                print(result)
        finally:
            connection.close()


class _Request():
    def __init__(self):
        pass

    def test(self):
        requrl = "http://proxy.finance.qq.com/ifzqgtimg/appstock/app/HsDealinfo/getDadan?code=sz002036&_appName=android&_dev=Redmi+Note+4X&_devId=c50cb922972722424434833f4167e6721c90d991&_mid=c50cb922972722424434833f4167e6721c90d991&_md5mid=22523BE796DEE7EA0C09F1346EF28481&_omgid=d60a9565b0d6064e612955b535047ef779d10010212615&_omgbizid=096de883a6ae2d4b6f395e484189e416b9ba0140212718&_appver=5.8.2&_ifChId=119&_screenW=1080&_screenH=1920&_osVer=6.0.1&_uin=10000&_wxuin=20000&_net=WIFI&__random_suffix=38315"
        req = urllib2.Request(url=requrl)
        print req
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        print res

req =_Request()
req.test()