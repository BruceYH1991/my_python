#
# import sys
#
#
#
# a = 3
#
#
# frame = sys._getframe()
#
# print(frame)
#
# def f():
#     frame_ = sys._getframe()
#     print(frame_)
#     print(frame_.f_back.f_locals)
#     print(frame_.f_back.f_globals)
#
#
# def g():
#     b = 2
#     f()
#
#
# class a:
#     pass
#
# print(type(a))


# def a():
#     try:
#         for i in range(10):
#             print(i)
#         return 'ok'
#
#     finally:
#         print('close')
#
#
# b = a()
# print(b)


class Acc:
    def __init__(self, data):
        self.data = data


data = {}
print(data)
a1 = Acc(data)
a1.data['a1'] = 1
print(data)
a2 = Acc(data)
print(a2.data)














