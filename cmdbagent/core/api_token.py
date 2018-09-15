# -*- coding: utf-8 -*-
'''
生成hash 并且取10-17位数据 加盐算法
返回算法结果 时间戳
'''
import hashlib, time
from functools import wraps


def get_token(username, token_id):
    timemap = int(time.time())
    md5_format_str = '{}{}{}'.format(username, token_id, timemap)
    # print(md5_format_str)
    obj = hashlib.md5()
    obj.update(md5_format_str.encode('utf-8'))
    # print(obj.hexdigest())
    return obj.hexdigest()[10:17], timemap


# cc = get_token(username='aaa', token_id='33')
# print(cc)
# obj = hashlib.md5()
# obj.update('aaaa'.encode('utf-8'))
# print(obj.hexdigest())
if __name__ == '__main__':
    print(get_token('xxx','text'))
