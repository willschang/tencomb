# -*- encoding: utf-8 -*-


def singleton(cls, *args, **kw):
    '''
    单例模式 使用装饰器(decorator)
    '''
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton