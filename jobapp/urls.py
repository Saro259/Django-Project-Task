from django.urls import path
from .views import job_ad_listing, job_post, job_single, SearchView, apply_job

app_name = 'jobapp'

urlpatterns = [

    path('job-post/', job_post, name='job_post'),
    path('job-ad-listing/', job_ad_listing, name='job_ad_listing'),
    path('job-single/<int:id>/', job_single, name='job_single'),
    path('search/', SearchView.as_view(), name='search'),
    path('apply/', apply_job, name='apply_job'),
    
]