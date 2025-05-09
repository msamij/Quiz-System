from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Student(models.Model):
    name = models.CharField(max_length=100)
    batch_name = models.CharField(max_length=20)
    batch_time = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""Student name: {self.name}, batch name: {self.batch_name}, 
    		batch time: {self.batch_time}"""


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=15)
