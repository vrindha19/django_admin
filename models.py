from django.db import models

# class settingsapp(models.Model):
#     email = models.EmailField(max_length=30)
#     password = models.CharField(max_length=50)

# class Persons(models.Model):
#     first_name = models.CharField(max_length=70)
#     last_name = models.CharField(max_length=70)

# class School(models.Model):
#    name = models.CharField(max_length=256)
#    principal = models.CharField(max_length=256)
#    location= models.CharField(max_length=256)
#    def __str__(self) -> str:
#        return self.name

# class Student(models.Model):
#     name = models.CharField(max_length=256)
#     age = models.PositiveBigIntegerField()
#     school= models.ForeignKey(School,on_delete=models.CASCADE,related_name='student')
#     def __str__(self) -> str:
#        return self.name
    
class LoginModel (models.Model):
        username = models.CharField(max_length=256)
        password= models.TextField()
        img=models.ImageField(upload_to='images/')
        def __str__(self) -> str:
               return self.username

