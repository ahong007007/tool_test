#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Project_name :     git
    File Name    :     test
    Description  :
    Author       :     chenhong
    date         :     2018/10/16
   
-------------------------------------------------
"""

__author__ = 'chenhong'
import logging


def log_init():
    """
    Initialize python logging modules.
    - return:
    """
    log_file = './pyalgo.log'

    # Initialize log settings.
    log_format = '%(levelname)7s - %(asctime)s %(process)d %(filename)s:%(lineno)s] %(message)s'
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        datefmt='%Y-%m-%d %a %H:%M:%S',
                        filename=log_file,
                        filemode='w')
    console = logging.StreamHandler()
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


log_init()
test = 5
print(test)
logging.info("test is {}".format(test))
