
from celery import Celery, current_app
import celery
from tasks import add, div
import celeryconfig
from threading import Thread

import pymysql

def mysql_db():
    # 连接数据库肯定需要一些参数
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        database="celery",
        charset="utf8",
        user="root",
        passwd="password"
    )
    return conn




app = Celery(__name__, include=["task"])
# 引入配置文件
app.config_from_object(celeryconfig)


def handle():
    conn = mysql_db()
    with conn.cursor() as cursor:
        sql = f"select request_id, task_name, task_id, status from task where status = 'PROCESS';"
        cursor.execute(sql)
        datas = cursor.fetchall()
        for data in datas:

            task_id = data.task_id

            res = celery.queryTask(task_id)
            if res.status == 'SUCCESS':
                dispatch(data)

list = ["add", "div" , "test"]

def dispatch(data):
    if data.request_id == 1 && data.status == "success":
        pass

    index = list.index(data.task_name)
    list[index +1 ]


if __name__ == '__main__':
    request_id = 1
    result = add.delay(30, 42)

    mthread = Thread(target=handle)
    mthread .start()


    conn = mysql_db()
    with conn.cursor() as cursor:
        sql = f"insert into task(request_id, task_name, task_id, status, next_task) values (request_id, result.task_id, result.status);"
        cursor.execute(sql)
        conn.commit()





