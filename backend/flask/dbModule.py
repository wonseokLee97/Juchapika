import pymysql


class Database():
    def __init__(self):
        self.db = pymysql.connect(host='',
                                  user='',
                                  password='',
                                  db='',
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        self.db.commit()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        self.db.commit()
        return row

    def commit():
        self.db.commit()
