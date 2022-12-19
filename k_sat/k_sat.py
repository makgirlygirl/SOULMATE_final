#%%
from k_sat_question import *
import json

'''
#미리 문제 만들 때!
# passageID=3

# filepath='/home/a1930008/k_sat/testset/'+str(passageID)+'.txt'
filepath='/home/a1930008/k_sat_pre/testset/221138.txt'

passageID=11


f = open(filepath)
passage = f.read()

'''
# 실시간 문제 생성용
class QuestionGenerate:
  def __init__(self, passageID, passage):
    self.passageID = passageID
    self.passage = passage
  
  def result(self):
    result = '{\n\t\"question_details\": ['
    q1 = Q1()
    q1json=q1.make_json(self.passageID, self.passage, is_Korean=False)
    if(q1json): result = result + '\t\t' + q1json + ','
    q2 = Q2()
    q2json= q2.make_json(self.passageID, self.passage, is_Korean=False)
    if(q2json):result = result + '\t\t' + q2json + ','
    q3 = Q3()
    q3json=q3.make_json(self.passageID, self.passage)
    if(q3json):result = result + '\t\t' + q3json + ','
    q4 = Q4()
    q4json=q4.make_json(self.passageID, self.passage)
    if(q4json):result = result + '\t\t' + q4json + ','
    q5 = Q5()
    q5json=q5.make_json(self.passageID, self.passage)
    if(q5json):result = result + '\t\t' + q5json + ','
    q6 = Q6()
    q6json=q6.make_json(self.passageID, self.passage)
    if(q6json):result = result + '\t\t' + q6json + ','
    q7 = Q7()
    q7json=q7.make_json(self.passageID, self.passage)
    if(q7json):result = result + '\t\t' + q7json + ','
    q8 = Q8()
    q8json=q8.make_json(self.passageID, self.passage)
    if(q8json):result = result + '\t\t' + q8json
    result = result + '\t]\n}'
    return json.loads(result)