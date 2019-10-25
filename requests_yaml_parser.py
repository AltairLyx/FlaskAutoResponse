# encoding: utf-8
"""
@author: Yixuan Liu
@contact: yixuan_liu@shannonai.com

@file: requests_yaml_parser.py.py
@time: 2019/10/19 下午2:30
@version: 1.0
@intro:
    description
"""


import yaml


class Sim:
    def __init__(self):
        with open(file='requests.yaml') as f:
            self.requests_yaml = yaml.load(f, Loader=yaml.FullLoader)

    @property
    def requests(self):
        return self.requests_yaml.get('requests')


sim = Sim()


if __name__ == '__main__':
    pass
