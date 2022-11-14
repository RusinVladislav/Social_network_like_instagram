import logging


def config(app):
    api_logger = logging.getLogger()
    api_logger.setLevel('INFO')
    api_logger_format = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    console_handler = logging.StreamHandler()

    api_logger_handler = logging.FileHandler("./log/api.log", 'a')
    api_logger_handler.setFormatter(api_logger_format)

    api_logger.addHandler(console_handler)
    api_logger.addHandler(api_logger_handler)
