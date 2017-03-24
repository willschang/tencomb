# -*- coding: utf-8 -*-

# We can overwite setting.py here
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 使用mysql做为数据库（本地测试）
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'tencomb',
    #     'USER': 'root',
    #     'PASSWORD': '123456',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    #     'STORAGE_ENGINE': 'INNODB',
    #     'OPTIONS': {},
    # }
    # qcloud上数据库
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'tencomb',
    #     'USER': 'ten',
    #     'PASSWORD': '123456',
    #     'HOST': 'ip',
    #     'PORT': '3306',
    #     'STORAGE_ENGINE': 'INNODB',
    #     'OPTIONS': {},
    # }
}