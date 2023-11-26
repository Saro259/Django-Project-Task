from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import JobAdListingForm, ApplyJobForm
from .models import *
from django.template.loader import get_template
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.views.generic import ListView

# Create your views here.

def job_home(request):
    qs = JobAdListing.objects.all()
    jobs = JobAdListing.objects.all().count()
    user = User.objects.all().count()
    paginator = Paginator(qs, 5)
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    data = {
        'query':qs,
        'job_qs': jobs,
        'candidates': user
    }
    return render(request, "home.html", data)

def about_us(request):
    return render(request, "jobapp/about_us.html",{})


@login_required
def job_ad_listing(request):
    query = JobAdListing.objects.all().count()
    qs = JobAdListing.objects.all().order_by('-published_on')
    paginator = Paginator(qs, 3)
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    data = {
        'query': qs,
        'job_qs': query
    }
    return render(request, "jobapp/job_ad_listing.html", data)


@login_required
def job_post(request):
    form = JobAdListingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/jobapp/job-ad-listing/')
    data = {
        'form': form,

    }
    return render(request, "/job_post.html", data)


def job_single(request, id):
    job_query = get_object_or_404(JobAdListing, id=id)
    data = {
        'q':job_query,
    }
    return render(request, "jobapp/job_single.html", data)


@login_required
def apply_job(request):
    form = ApplyJobForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/')
    data = {
        'form':form,
    }
    return render(request, "jobapp/apply_job.html", data)


class SearchView(ListView):
    model = JobAdListing
    template_name = 'jobapp/search.html'
    context_object_name = 'jobapp'

    def get_queryset(self):
        return self.model.objects.filter(job_title__contains=self.request.GET['job_title'], job_location__contains=self.request.GET['job_location'], employment_type__contains=self.request.GET['employment_type'])
