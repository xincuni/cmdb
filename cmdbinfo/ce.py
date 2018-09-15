
a = set([1,2,3,4])
b = set([1,2,3])
c = a - b
c = b - a
print c

# import hashlib
# def gen_token():
#     token_format = "asdasdasd111"
#     #print('--->token format:[%s]'% token_format)
#     obj = hashlib.md5()
#     obj.update(token_format.encode())
#     return obj.hexdigest()
# aa=gen_token()
# print aa
# obj = hashlib.md5()
# obj.update('asdasdasd')

# import logging
#
# def use_logging(func):
#     logging.warn("%s is running" % func.__name__)
#     return func()
#
# def foo():
#     print 'i am foo'
#
# def bar():
#     print 'i am bar'

# use_logging(foo)
# use_logging(bar)

# def use_logging(func):
#     def wrapper(*args,**kwargs):
#         logging.warn("%s is running" % func.__name__)
#         return func(*args)
#     return wrapper
#
# @use_logging
# def foo():
#     print 'i an foo'
#
# @use_logging
# def bar():
#     print 'i am bar'
#
# foo()
# bar()