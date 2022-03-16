import logging, sys 

LEVELS = {
    'debug':logging.DEBUG,
    'info':logging.INFO,
    'warning':logging.ERROR,
    'error':logging.ERROR,
    'critical':logging.CRITICAL,
}

if len(sys.argv)>1:
    level_name = sys.argv[1]
    level=LEVELS.get(level_name,logging.NOTSET)
    logging.basicConfig(level=level)

logging.debug("This is a debug message")
logging.info("This is an infor message")
logging.warning("This is a warning message")
logging.error("This ia an error message")
logging.critical("This is a critical message")