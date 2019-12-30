# -*- coding: utf-8 -*-

from ETL_Log import etl_log
import psycopg2
import traceback

from config.common_config import db_config

logger = etl_log.get_logger("ELK_Db")


class ElkDb:

    # 创建连接、游标
    def __init__(self, **kwargs):
        self.conn = None
        self.user = kwargs.get("dbuser")
        self.password = kwargs.get("password")
        self.host = kwargs.get("host")
        self.port = kwargs.get("port")
        self.database = kwargs.get("database")
        if not (self.host and self.port and self.user and
                self.password and self.database):
            logger.warn("conn_error, missing some params!")

    def _conn(self):
        # 清理上次资源
        if self.conn is not None:
            self.conn.close()
        try:
            self.conn = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.conn.autocommit = True     # 默认 单条语句是一个事务
        except Exception as e:
            logger.error(
                "%s,%s,%s,%s连接elk数据库失败"%
                (self.host, self.port, self.user, self.password)
            )
            raise e     # 此类错误立即抛出，就别跑了
        logger.info(
            "%s,%s,连接elk数据库成功" % (self.host, self.port)
        )

    def checkConnect(self):
        if self.conn is None :
            self._conn()

    # 目前仅支持查询select语句
    def select(self, sql):
        # 检查连接状态，若其重连
        self.checkConnect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            a = cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            logger.error("%s  SQL异常"% sql)
            logger.error(traceback.format_exc())
        finally:
            if cursor is not None:
                cursor.close()

    # 支持运行 insert update
    def update(self, sql):
        # 检查连接状态，若其重连
        self.checkConnect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            count = cursor.execute(sql)
            return count
        except Exception as e:
            self.rollback() # 回滚
            logger.error("%s  SQL异常"% sql)
            logger.error(traceback.format_exc())
        finally:
            if cursor is not None:
                cursor.close()

    # 开启事务
    def start_transaction(self):
        self.checkConnect()
        self.conn.autocommit = False
        logger.info("%s,%s,elk数据库事务开启" % (self.host, self.port))

    def end_transaction(self):
        self.commit()   # 提交事务
        self.conn.autocommit = True
        logger.info("%s,%s,elk数据库事务关闭" % (self.host, self.port))

    # 提交
    def commit(self):
        self.conn.commit()

    # 回滚
    def rollback(self):
        self.conn.rollback()

    # 关闭连接
    def close(self):
        self.conn.close()
        self.conn = None



if __name__ == '__main__':
    db = ElkDb(**db_config)
    db.start_transaction()
    res = db.select("select * from test.people")
    print(res)
    res = db.select("select * from test.people t where t.name = 'yfshi'")
    print(res)

    res = db.update("insert into test.people values('yfshi3','123','20','100.3','0')")
    print(res)

    # db.end_transaction()