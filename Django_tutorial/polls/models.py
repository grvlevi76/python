from django.db import models

# Create your models here. -> edited by me

class Question(models.Model):    #question is module
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):     #choice is module
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class ggg(models.Model):
    not_nigga = models.IntegerField(default=0)
    nigga_text = models.CharField(max_length=300)

#these classes r nothing but just the table name with variables inside of classs as attribute(columns) of database with their datatype

