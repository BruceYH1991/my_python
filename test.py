
import pandas as pd
import pymysql
from collections import deque

deque.append()
mysql_config = {
    'host': 'cashlending-readonly.c3dsrzz0nv8o.ap-southeast-1.rds.amazonaws.com',
    'port': 3306,
    'user': 'cashlending',
    'password': 'cash123456',
    'charset': 'utf8'
}

conn = pymysql.connect(**mysql_config)

sqlerr = 'select application_id,member_id from indicator.etl_basisInfo where bs_last_app_status=2'

cursor = conn.cursor()
num = cursor.execute(sqlerr)

result1 = cursor.fetchall()


def get_last_status(application_id, member_id):
    sql = 'select status,loan_amount from cashlending.loan_application_info where member_id={} and id < {}'
    cursor.execute(sql.format(member_id, application_id))
    try:
        rr = cursor.fetchone()
        status = rr[0]
        amount = rr[1]

    except TypeError:
        status = None
        amount=None
    return {application_id: [status, amount]}


fr = []
for data in result1:
    application_id = data[0]
    member_id = data[1]
    r = get_last_status(application_id, member_id)
    fr.append(r)

print(fr)









