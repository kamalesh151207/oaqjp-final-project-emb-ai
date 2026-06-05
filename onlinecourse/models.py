from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
class Submission(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.user
    def __str__(self):
        return self.text

class Submission(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.user
