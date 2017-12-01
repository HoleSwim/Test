# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging


def get_logger():
    formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(formatter)
    file_handle = logging.FileHandler('log.log', mode='wb', encoding='utf8')
    file_handle.setLevel(logging.WARNING)
    file_handle.setFormatter(formatter)
    logger = logging.getLogger('logger')
    logger.setLevel(logging.WARNING)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handle)
    return logger


def get_stream_logger():
    formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.StreamHandler()
    # handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger


def get_file_logger():
    formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('log.log', mode='wb', encoding='utf8')
    # handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger


if __name__ == '__main__':
    # logger = get_logger()
    # logger.info('info')
    # logger.warning('warning')

    console_logger = get_stream_logger()
    file_logger = get_file_logger()
    console_logger.info('console info')
    file_logger.info('file info')
