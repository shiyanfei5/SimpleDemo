# -*- coding: utf-8 -*-

from config import common_config
import logging


class Logger(object):

    def __init__(self):
        format_str = logging.Formatter(common_config.log_formatter)  # 设置日志格式
        self.logger_name = 'MAIN'
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(common_config.log_level)     # 设置日志级别

        sh = logging.StreamHandler()    # 往屏幕上输出
        sh.setFormatter(format_str)     # 设置屏幕上显示的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        if common_config.is_log_file:
            th = logging.FileHandler(filename=common_config.log_file_path, mode='a', encoding='utf-8')
            th.setFormatter(format_str)  # 设置文件里写入的格式
            self.logger.addHandler(th)

    def get_logger(self, name):
        return logging.getLogger(self.logger_name+"."+name)


etl_log = Logger()




