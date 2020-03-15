"""
date:
author: east
function:
"""
import datetime
import random
import requests
import traceback
from apscheduler.schedulers.blocking import BlockingScheduler

sch = BlockingScheduler()


def job_add():
    """
    调用自己的推送服务进行推送通知
    """
    print("add job")
    sch.add_job(push, 'cron', day_of_week='0-5', hour='10-18')


def push():
    """
    给手机发推送
    """
    words = [
        '站起来休息一下',
        '走一走了',
        '摸会儿鱼呀',
        '站起来喝口水吧'
    ]
    try:
        print(f"当前时间：{datetime.datetime.now()}，执行提醒")
        requests.get(f"http://eastfly.top:8080/YS277KEBhxZ4jh7gT9YJnL/TakeARest/{random.choice(words)}")
    except Exception:
        print("push error")
        traceback.print_exc()


if __name__ == '__main__':
    job_add()
    print('job start')
    sch.start()
