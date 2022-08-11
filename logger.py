import logging


def config(app):
    api_logger = logging.getLogger("api_logger")
    api_logger.setLevel(logging.INFO)

    api_logger_handler = logging.FileHandler(filename='./log/api.log')
    api_logger_handler.setLevel(logging.INFO)
    api_logger.addHandler(api_logger_handler)

    api_logger_format = logging.Formatter("%(asctime)s : %(message)s")
    api_logger_handler.setFormatter(api_logger_format)
