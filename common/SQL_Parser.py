# -*- coding: utf-8 -*-

from ETL_log import etl_log
import io



logger = etl_log.get_logger("SQL_Parser")


class SqlResource(object):
    sql_map_cache = {}    # cache，缓存加载过的SQL

    def __init__(self, sql_file, encoding = 'gb2312'):
        self.file = sql_file
        self.is_parsed = False  # 表明没有被解析替换参数过
        logger.info(self.load_sql_file(encoding))

    def load_sql_file(self, encoding):
        sql = None  # 作用域提前,执行失败为None
        if self.file is not None:
            try:
                with io.open(self.file, 'r', encoding=encoding) as f:
                    sql = f.read()
            except Exception as e :
                logger.error("%s SQL资源文件打开失败" % self.file)
                raise e     # 及时抛错，避免多次加载
        return sql


if __name__ == '__main__':
    print("xx")










