# -*- coding: utf-8 -*-
import sys, os, platform
from core import HouseStark

print(platform.system())
if platform.system() == 'Linux':  # 判断系统版本
    Base_Dir = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
    print(Base_Dir)
else:
    Base_Dir = '//'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])

sys.path.append(Base_Dir)  # 添加环境变量

if __name__ == '__main__':
    HouseStark.ArgvHandler(sys.argv)  # 传参数调用核心模块
