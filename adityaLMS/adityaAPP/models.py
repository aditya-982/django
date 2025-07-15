from django.db import models

# Create your models here.
userTypeData = (
    ("Teacher", "Teacher"),
    ("Student", "Student")
)


class adityaAPPUser(models.Model):
    userId=models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=50, null=True , blank=True)
    number = models.IntegerField(unique=True)
    password = models.CharField(max_length=100)
    userType = models.CharField(max_length=20,choices=userTypeData)

class adityaAPPUpload(models.Model):
    courseUpload =models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=100)
    courseDescription = models.CharField(max_length=500)
    createdAt = models.DateField()
    coursePlaylist = models.IntegerField()
    couseDuretion = models.IntegerField()
    userName = models.ForeignKey(adityaAPPUser, on_delete=models.CASCADE)