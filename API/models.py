from django.db import models

# Create your models here.
class UserApi(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class JobProfile(models.Model):

    job = models.CharField(max_length=100)

    def __str__(self):
        return self.job
    
class UserCompanyApiModel(models.Model):
    name = models.ForeignKey(UserApi,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    jobprofile = models.ForeignKey(JobProfile,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name.name