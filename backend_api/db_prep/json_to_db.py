import pymysql
import json


def insert_passage(val):
    conn = pymysql.connect(
        host='localhost',
        user = 'root',
        password = '<your password>',
        db = '<your db name>',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "insert into passage(passage) values (%s)"
    vals = (val["passage"])
    cur.execute(sql, vals)
    conn.commit()
    conn.close()

def insert_question(val):
    conn = pymysql.connect(
        host='localhost',
        user = 'root',
        password = '<your password>',
        db = '<your db name>',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "insert into question(passageID, question_type, question, new_passage, answer, e1, e2, e3, e4, e5) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    vals = (val["passageID"], val["question_type"], val["question"], val["new_passage"], val["answer"], val["e1"], val["e2"], val["e3"], val["e4"], val["e5"])
    cur.execute(sql, vals)
    conn.commit() 
    conn.close()

with open('prep.json') as f:
    json_data = json.load(f)

    for passage in json_data["passages"]:
        insert_passage(passage)

    for question in json_data["question_details"]:
        insert_question(question)