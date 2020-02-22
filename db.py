import pymysql
import json
import time
import random
import string


def database_connector(): #连接数据库
    db = pymysql.connect("101.132.165.43", "timetable", "kiko2333", "timetable_push", charset='utf8')
    return db

def select_all():
    db = database_connector()
    cursor = db.cursor()
    sql = "SELECT * FROM PushTable order by Weekday, ClassNo asc"

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

    except:
        print("在程序执行中发生了错误，错误信息为：未能找到相应学校信息，请检查是否输入错误")
    db.close()
    return results