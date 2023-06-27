import logging


def get_logger(service_name):
    LOG_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

    # Path and log file name
    LOG_FILE = f'basic_logging.log'

    # service name
    LOG_NAME = service_name

    # instantiante the logger
    logger = logging.getLogger(LOG_NAME)
    # formater
    log_formatter = logging.Formatter(LOG_FORMAT)
    # define filehandler
    log_file_handler = logging.FileHandler(LOG_FILE)
    # apply formater
    log_file_handler.setFormatter(log_formatter)
    # define min verbosity level
    log_file_handler.setLevel(logging.INFO)

    # add handler
    logger.addHandler(log_file_handler)

    return logger


if __name__ == '__main__':
    # get logger obj
    logger = get_logger('testando')

    logger.info('this is an info log message')
    logger.warning('this is a warning log message')
    logger.error('this is an error log message')
    logger.critical('this is a critical log message')
    logger.exception('this is an exception log message')

    try:
        raise
    except:
        logger.exception('this is an EXCEPTION log message')
