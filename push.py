# -*- coding: utf-8 -*-
import pymysql
import time
import requests
import json
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


def database_connector(): #连接数据库
    db = pymysql.connect("kikocore.cn", "timetable", "kiko2333", "timetable_push", charset='utf8')
    return db

def get_weekday():
    return time.localtime().tm_wday + 1

def get_dat():
    tim = time.localtime()
    stri = str(tim.tm_year) + "年" + str(tim.tm_mon) + "月" + str(tim.tm_mday) + "日"
    return stri

def tmst(str):
    db = pymysql.connect("kikocore.cn", "timetable", "kiko2333", "timetable", charset='utf8')
    cursor = db.cursor()
    sql = "SELECT * FROM school_term"

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            if row[0] == str:
                return row[1]
    except:
        print("在程序执行中发生了错误，错误信息为：未能找到相应学校信息，请检查是否输入错误")
    db.close()

def this_week(scl):
    term_start = tmst(scl)
    imatime = time.localtime()
    weekday_past = imatime.tm_yday - term_start
    week = weekday_past / 7 + 1
    return int(week)

def select_today_all():
    db = database_connector()
    cursor = db.cursor()
    sql = "SELECT * FROM PushTable WHERE Weekday LIKE " + str(get_weekday()) + " AND ClassStartWeek <= " + str(this_week('hiit')) + " AND ClassStopWeek >= " + str(this_week('hiit'))

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

    except:
        print("在程序执行中发生了错误，错误信息为：未能找到相应学校信息，请检查是否输入错误")
    db.close()
    return results

def select_all():
    db = database_connector()
    cursor = db.cursor()
    sql = "SELECT * FROM PushTable WHERE Weekday LIKE " + str(get_weekday()) + " AND ClassStartWeek <= " + str(this_week('hiit')) + " AND ClassStopWeek >= " + str(this_week('hiit'))

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

    except:
        print("在程序执行中发生了错误，错误信息为：未能找到相应学校信息，请检查是否输入错误")
    db.close()
    return results

def push(inp):
    url = "https://oapi.dingtalk.com/robot/send?access_token=bb9cd7cc600a1ebae4cc11a03f5430a488b87c9d54c4eda537f92ee34d05da94"
    key = "【上课通知】"
    headers = {"Content-Type" : "application/json;charset=utf-8"}
    post_data = {
    "actionCard": {
        "title": "【上课通知】" + inp[6] + " 将于 " + inp[9] + " 开始上课",
        "text": "### 【上课通知】" + inp[6] + " 将于 " + inp[9] + " 开始上课\n\n" + "今天是" + get_dat() + "，星期" + str(get_weekday()) + "\n\n课程名称：" + inp[6] + "\n\n"
        + "教室：" + inp[7] + "\n\n上课时间：" + str(inp[9]) + " -- " + str(inp[10]) + "\n\n开课周：" + str(inp[11]) + " -- " +
        str(inp[12]) + "\n\n网课链接：" + str(inp[14]),
        "hideAvatar": "0",
        "btnOrientation": "0",
        "btns": [
            {
                "title": "点击跳转上课",
                "actionURL": inp[14]
            }
        ]
    },
    "msgtype": "actionCard"
}
    print(post_data)
    post_data = json.dumps(post_data)
    P_post = requests.post(url, headers=headers, data=post_data)
    print(P_post.json())


def time_judge():
    tim = time.localtime()
    ima = str(tim.tm_hour) + ":" + str(tim.tm_min)
    return ima

def push_by_time():
    ta = select_today_all()
    for ta in ta:
        if time_judge() == ta[2]:
            push(ta)
    print(ta)

push_by_time()
