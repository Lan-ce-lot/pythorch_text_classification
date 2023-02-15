#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: open_ckpt_tool.py
@time: 2021/4/13 9:41
"""
from importlib import import_module

import torch

if __name__ == '__main__':
    # 加载
    dataset = 'data'
    # torch.cuda.empty_cache()
    model_name = 'bert'  # bert
    x = import_module('models.' + model_name)
    config = x.Config(dataset)
    model_dict = torch.load('..\\data\\saved_dict\\bert_2021_4_13_cpu.ckpt')
    pass
