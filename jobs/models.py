from django.db import models
from django.utils import timezone


class Employer(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=100, default=None, null=True)
    companyname = models.CharField(max_length=100, default=None, null=True)
    address = models.CharField(max_length=200, default=None, null=True)
    pincode = models.CharField(max_length=20, default=None, null=True)
    location = models.CharField(max_length=200, default=None, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=30, default=None, null=True)
    fblink = models.URLField(max_length=100, default=None, null=True)
    email = models.EmailField(null=False, blank=False)

    def __char__(self):
        return self.ename


class Job(models.Model):
    jobid = models.AutoField(primary_key=True)
    eid = models.ForeignKey(Employer,
                            default=None,
                            null=True,
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=None, null=True)
    jobdesc = models.CharField(max_length=700, default=None, null=True)
    basicpay = models.CharField(max_length=50, default=None, null=True)
    salary_currency = models.CharField(max_length=3, default=None, null=True)
    salary_type = models.CharField(max_length=50, default="monthly", null=True)
    location = models.CharField(max_length=200, default=None, null=True)
    postdate = models.DateTimeField(default=timezone.now)
    jobtype = models.CharField(max_length=50, default="full_time")

    def __char__(self):
        return self.jobid