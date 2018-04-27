#!/usr/bin/env python3
# coding: utf-8
# File: test.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-27
from sim_cilin import *
from sim_hownet import *
from sim_simhash import *
from sim_tokenvector import *
from sim_vsm import *

def test():
    cilin = SimCilin()
    hownet = SimHownet()
    simhash = SimHaming()
    simtoken = SimTokenVec()
    simvsm = SimVsm()

    while 1:
        text1 = input('enter sent1:').strip()
        text2 = input('enter sent2:').strip()
        print('cilin', cilin.distance(text1, text2))
        print('hownet', hownet.distance(text1, text2))
        print('simhash', simhash.distance(text1, text2))
        print('simtoken', simtoken.distance(text1, text2))
        print('simvsm', simvsm.distance(text1, text2))
test()