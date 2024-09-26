from django.db import models

class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f'Question {self.id}'

class Deleted(models.Model):
    question = models.TextField()
    answer = models.TextField()

