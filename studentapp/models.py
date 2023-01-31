import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from studentapp.validator import validate_file_size


class Login_view(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Student_Registration(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE,related_name='student',null=True)
    name=models.CharField(max_length=200)
    dob= models.DateField()
    phone=models.IntegerField()
    age= models.IntegerField(default=0)
    student_image = models.FileField(upload_to='profilepic/',validators=[validate_file_size])
    def age(self):
        age = datetime.date.today() - self.dob
        return int((age).days / 365.25)

    def __str__(self):
        return self.name

class Admin1(models.Model):
     user = models.OneToOneField(Login_view, on_delete=models.CASCADE, related_name='admin', null=True)
     name=models.CharField(max_length=100)
     phone_number= models.IntegerField()

     def __str__(self):
        return self.name




class Mark(models.Model)  :
    roll_number = models.IntegerField(default=0,unique=True)
    name = models.ForeignKey(Student_Registration,on_delete=models.CASCADE)
    maths= models.IntegerField(validators=[MaxValueValidator(50)])
    english = models.IntegerField(validators=[MaxValueValidator(50)])
    physics = models.IntegerField(validators=[MaxValueValidator(50)])
    chemistry = models.IntegerField(validators=[MaxValueValidator(50)])
    biology = models.IntegerField(validators=[MaxValueValidator(50)])
    Total = models.IntegerField(validators=[MaxValueValidator(50)])
    Total_mark = models.IntegerField(default=0)

    def __str__(self):
        return self.name + self.Total_mark

    def Total_mark(self):
        self.Total_mark=self.maths + self.english +self.physics +self.chemistry +self.biology
        return self.Total_mark

