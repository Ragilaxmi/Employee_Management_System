from django.db import models

# Create your models here.
class Base(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=30)
    class Meta:
        abstract=True
class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=20)
    def __str__(self):
        return self.deptname
class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=20)
    salary=models.IntegerField()
    department=models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
    profile_pic=models.ImageField(upload_to='images/',null=True)
    video=models.FileField(upload_to='videos/',null=True)
    def __str__(self):
        return self.empname
class Table1(Base):
    address=models.CharField(max_length=100)
class Table2(Base):
    mobile=models.CharField(max_length=30)
class Employee_dup(Employee):
    class Meta:
        proxy=True
        ordering=['empno']