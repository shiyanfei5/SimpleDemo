# -*- coding: utf-8 -*-
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
本文件为公共方法相关配置，由于比较简单因此不引入配置解析模块，直接通过变量形式配置
"""
# 日志配置
is_log_file = False      # 是否要开启日志输出
log_file_path = './1.log'     # 日志文件夹路径
log_file_mode = 'a'           # 文件日志形式，追加还是覆写
log_level = logging.DEBUG   # 日志级别
log_formatter = '%(asctime)s-%(process)d-%(module)s[%(filename)s.line:%(lineno)d]-%(levelname)s: %(message)s'

# 数据库配置
db_config = {
    'dbuser': 'postgres',
    'password': '123456',
    'port': '5432',
    'host': '132.232.54.199',
    'database': 'postgres'
}