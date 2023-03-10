# Generated by Django 4.1.1 on 2022-12-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='delQuestion',
            fields=[
                ('questionID', models.IntegerField(primary_key=True, serialize=False)),
                ('passageID', models.IntegerField()),
                ('question_type', models.IntegerField()),
                ('question', models.TextField(max_length=1000)),
                ('new_passage', models.TextField(max_length=2000, null=True)),
                ('answer', models.IntegerField()),
                ('e1', models.TextField(max_length=1000)),
                ('e2', models.TextField(max_length=1000)),
                ('e3', models.TextField(max_length=1000)),
                ('e4', models.TextField(max_length=1000)),
                ('e5', models.TextField(max_length=1000)),
            ],
            options={
                'db_table': 'del_question',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('evalID', models.AutoField(primary_key=True, serialize=False)),
                ('questionID', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'evaluation',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionID', models.AutoField(primary_key=True, serialize=False)),
                ('passageID', models.IntegerField()),
                ('question_type', models.IntegerField()),
                ('question', models.TextField(max_length=1000)),
                ('new_passage', models.TextField(max_length=2000, null=True)),
                ('answer', models.IntegerField()),
                ('e1', models.TextField(max_length=1000)),
                ('e2', models.TextField(max_length=1000)),
                ('e3', models.TextField(max_length=1000)),
                ('e4', models.TextField(max_length=1000)),
                ('e5', models.TextField(max_length=1000)),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]
