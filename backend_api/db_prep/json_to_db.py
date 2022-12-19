import pymysql
import json

'''conn = pymysql.connect(
    host='localhost',
    user = 'root',
    password = 'akrrjfflrjf',
    db = 'restapidb',
    charset = 'utf8')'''

def insert_passage(val):
    conn = pymysql.connect(
        host='localhost',
        user = 'root',
        password = 'akrrjfflrjf',
        db = 'restapidb',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "insert into passage(passage) values (%s)"                         # 데이터 입력 틀
    vals = (val["passage"])             # 입력값 분리? 
    cur.execute(sql, vals)                                                  # 데이터 입력 실행
    conn.commit()  # 입력한 데이터 저장
    conn.close()   # MySQL 연결 종료

def insert_question(val):
    conn = pymysql.connect(
        host='localhost',
        user = 'root',
        password = 'akrrjfflrjf',
        db = 'restapidb',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "insert into question(passageID, question_type, question, new_passage, answer, e1, e2, e3, e4, e5) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"                         # 데이터 입력 틀
    vals = (val["passageID"], val["question_type"], val["question"], val["new_passage"], val["answer"], val["e1"], val["e2"], val["e3"], val["e4"], val["e5"])             # 입력값 분리? 
    cur.execute(sql, vals)                                                  # 데이터 입력 실행
    conn.commit()  # 입력한 데이터 저장
    conn.close()   # MySQL 연결 종료

with open('prep.json') as f:
    json_data = json.load(f)

    for passage in json_data["passages"]:
        insert_passage(passage)

    for question in json_data["question_details"]:
        insert_question(question)