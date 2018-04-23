from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20) # 相当于mysql中的varchar(20)
    sex = models.BooleanField()  # 相当于mysql中的bit
    class Meta: # 元，模型对应于数据库中的stu表
        db_table = 'stu'