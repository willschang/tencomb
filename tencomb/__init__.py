# -*- encoding: utf-8 -*-

# python3.5里的MySQL-python版本不支持，只能安装pymysql
# 通过该部分的设置申请，使django=1.8支持MySQLdb的引用
import pymysql

pymysql.install_as_MySQLdb()