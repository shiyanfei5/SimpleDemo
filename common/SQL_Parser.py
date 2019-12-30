# -*- coding: utf-8 -*-

from ETL_Log import etl_log
import io
import re


logger = etl_log.get_logger("SQL_Parser")


class SqlResource(object):
    sql_map_cache = {}    # cache，缓存加载过的SQL
    reg = re.compile("'\$.*?'")

    def __init__(self, sql_file, encoding='gb2312'):
        self.file = sql_file
        self.is_parsed = False  # 表明没有被解析替换参数过
        SqlResource.sql_map_cache[self.file] = self.load_sql_file(encoding)

    def load_sql_file(self, encoding):
        sql = None  # 作用域提前,执行失败为None
        if self.file is not None:
            try:
                with io.open(self.file, 'r', encoding=encoding) as f:
                    sql = f.read()
            except Exception as e :
                logger.error("%s SQL资源文件打开失败" % self.file)
                raise e     # 及时抛错，执行必要条件缺少
        logger.info("%s SQL资源文件获取成功" % self.file)
        return sql

    # 获取未替换的sql
    def get_raw_sql(self):
        return SqlResource.sql_map_cache[self.file]

    def sql_param_parsed(self,**kw):
        raw_sql = self.get_raw_sql()
        for key in kw.keys():
            raw_sql = raw_sql.replace('$'+key, str(kw[key]) )
            logger.info("%s SQL资源文件获取参数替换$%s" % (self.file,key))
        # 替换完成检查是否含有参数
        remain = SqlResource.reg.findall(raw_sql)
        if len(remain) > 0 :
            logger.error("%s SQL资源存在未解析参数%s" % (self.file,remain))
            raise Exception("%s SQL资源存在未解析参数%s" % (self.file,remain))
        else:
            logger.info("%s SQL资源参数解析完成" % self.file)
            return raw_sql




if __name__ == '__main__':
    res = SqlResource("E:\python_project\etl\common\jcb_personas_acct_info_latest010200.sql")
    logger.info(res.sql_param_parsed(DayOfData=1,ETL_TXDATE=2 ))









