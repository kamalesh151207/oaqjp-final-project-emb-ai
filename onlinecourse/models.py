from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    full_time = models.BooleanField(default=True)

    def __str__(self):
        return "Instructor"


class Learner(models.Model):
    occupation = models.CharField(max_length=200)

    def __str__(self):
        return self.occupation


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
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

    def __str__(self):
        return self.text


class Enrollment(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.learner} - {self.course}"


class Submission(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE
    )

    choices = models.ManyToManyField(Choice)

    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.enrollment)