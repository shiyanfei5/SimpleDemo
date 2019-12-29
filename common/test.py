# -*- coding: utf-8 -*-

from ETL_log import etl_log
import psycopg2



logger = etl_log.get_logger(__name__)
logger.info("aaaa")
logger.warn("wpc你好啊")
logger.warn("学校学校")