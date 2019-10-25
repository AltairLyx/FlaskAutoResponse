# encoding: utf-8
"""
@author: Yixuan Liu
@contact: yixuan_liu@shannonai.com

@file: config_gunicorn.py
@time: 2019/10/22 下午6:00
@version: 1.0
@intro:
    description
"""


worker_class = 'gevent'
workers = 1
bind = '0.0.0.0:5000'
loglevel = 'info'

if __name__ == '__main__':
    pass
