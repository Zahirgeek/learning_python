import logging
# 设置格式
LOG_FORMAT = "%(asctime)s=====%(levelname)s++++++%(message)s"

# 修改log配置 filename: log文件名, level: 输出最低级别, format: 格式
logging.basicConfig(filename="Zahirlog.log", level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is an error log.")
logging.critical("This is a critical log.")

logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")
