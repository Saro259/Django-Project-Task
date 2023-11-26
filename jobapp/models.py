from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

# Create your models here.


# class Contact(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharFiled(max_length=100)
#     email_id = models.EmailField()
#     subject = models.CharField(max_length=100)
#     message = models.TextField()

JOB_TYPE = (
    ('Full-Time', 'Full-time'),
    ('Part-Time', 'Part-Time'),
    ('Contract', 'Contract'),
    ('Temporary', 'Temporary'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any', 'Any'),
)


class JobAdListing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, editable=False, blank=True)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_description = models.TextField()
    gender = models.CharField(choices=GENDER, max_length=20, null=True)
    experience = models.CharField(max_length=200)
    responsibilites = models.TextField()
    application_deadline = models.DateTimeField()
    salary_range = models.CharField(max_length=100, null=True, blank=True)
    job_location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=JOB_TYPE)
    published_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job_title
    
    def get_absolute_url(self):
        return reverse("jobs:job-single", args=[self.id])
    
    
class ApplyJob(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    resume_file = models.FileField(upload_to='resumes/')
    
    def __str__(self):
        return self.name









