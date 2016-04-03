from django.db import models

# Create your models here.
'''
every time after creating or updating model, need do "makemigrations"
command:
python manage.py makemigrations quiz
to notify Django about changes

then run generated SQL to create model tables in DB by this command:
python manage.py migrate

use python manage.py sqlmigrate quiz 0001 command to see details
'''

class Question(models.Model):
    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    class Meta:
        db_table = 'questions'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.TextField(max_length=200)
    def __str__(self):
        return self.choice_text
    class Meta:
        db_table = 'choices'
