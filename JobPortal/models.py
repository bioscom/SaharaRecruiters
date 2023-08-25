from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to="")
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
 
    def __str__(self):
        return self.user.first_name


class Company(models.Model):
    #user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="", null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    usertype = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    company_name=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.user.username
    
class CompanyOld(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    type=(('Full-Time','full-time'), ('Part-Time','part-time'), ('Temporary','temporary'), )
    JobType=models.CharField(max_length=200,null=True,choices=type)
    name=models.CharField(max_length=200,null=True)
    position=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=5000,null=True)
    salaryfrom=models.IntegerField(null=True)
    salaryto=models.IntegerField(null=True)
    terms=(
        ('month','month'),
        ('week','week'),
    )
    salaryterms=models.CharField(max_length=200,null=True,choices=terms)
    level=(
        ('Experienced','Experienced'),
        ('Intermediate','Intermediate'),
        ('Trainee','Trainee'),
    )
    experience=models.CharField(max_length=200,null=True,choices=level)
    Location=models.CharField(max_length=2000,null=True)
    
    def __str__(self):
        return self.user.username


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=200)
    salary = models.FloatField()
    image = models.ImageField(upload_to="")
    description = models.TextField(max_length=400)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    creation_date = models.DateField()
 
    def __str__ (self):
        return self.title

class Application(models.Model):
    company = models.CharField(max_length=200, default="")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    resume = models.ImageField(upload_to="")
    apply_date = models.DateField()
 
    def __str__ (self):
        return str(self.applicant)


class Candidates(models.Model):
    category=(
        ('Male','male'),
        ('Female','female'),
    )
    name=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True)
    gender= models.CharField(max_length=200,null=True,choices=category)
    mobile= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    resume=models.FileField(null=True)
    company=models.ManyToManyField(Company,blank=True)
    def __str__(self):
        return self.name