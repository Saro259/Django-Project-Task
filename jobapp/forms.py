from django import forms
from jobapp.models import *


class JobAdListingForm(forms.ModelForm):
    class Meta:
        model = JobAdListing
        fields = ['job_title', 'job_description', 'responsibilites', 'application_deadline', 'salary_range', 'job_location', 'employment_type','published_on']
        labels = {'job_location': 'Job Location',
                  'published_on': 'Publish Date'
                }
        
        widgets = {
            'job_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title'}),
            'job_description':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Job Description'}), 
            'salary_range':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'job_location':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Job Location'}),
            'application_deadline':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Application Deadline'})
        }
class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = '__all__'
        labels = {
            'resume_file': 'CV (PDF format)',
            'name': 'Full Name'
        }
        