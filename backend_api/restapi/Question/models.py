from django.db import models

# Create your models here.
class Question(models.Model):
    questionID = models.AutoField(primary_key=True)
    passageID = models.IntegerField()
    question_type = models.IntegerField()
    question = models.TextField(max_length=1000)
    new_passage = models.TextField(max_length=2000, null=True)
    answer = models.IntegerField()
    e1 = models.TextField(max_length=1000)
    e2 = models.TextField(max_length=1000)
    e3 = models.TextField(max_length=1000)
    e4 = models.TextField(max_length=1000)
    e5 = models.TextField(max_length=1000)

    class Meta:
      db_table = 'question'

class Evaluation(models.Model):
    evalID = models.AutoField(primary_key=True)
    questionID = models.IntegerField(null=True)

    class Meta:
      db_table = 'evaluation'

class delQuestion(models.Model):
    questionID = models.IntegerField(primary_key=True)
    passageID = models.IntegerField()
    question_type = models.IntegerField()
    question = models.TextField(max_length=1000)
    new_passage = models.TextField(max_length=2000, null=True)
    answer = models.IntegerField()
    e1 = models.TextField(max_length=1000)
    e2 = models.TextField(max_length=1000)
    e3 = models.TextField(max_length=1000)
    e4 = models.TextField(max_length=1000)
    e5 = models.TextField(max_length=1000)

    class Meta:
      db_table = 'del_question'