from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from .models import Week, Choice
# import the login_required decorator and the LoginRequiredMixin mixin below


# Import the logout function from django.contrib.auth below

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Add login_required decorator:
def index(request):
  latest_week_poll = Week.objects.get(pk=1)
  context = {
     "name": request.user,
    "week_poll": latest_week_poll
  }
  return render(request, "index.html", context)

# Create your class-based Signup view below:

class DetailsView(DetailView):
  model = Week
  template_name = "detail.html"

class ResultsView(DetailView):
  model = Week
  template_name = "results.html"

# Create your logout function, logout_request, below:

# Add login_required decorator:
def vote(request, week_id):
  try:
    week = Week.objects.get(pk=week_id)
    selected_choice = week.choice_set.get(pk=request.POST["choice"])
  except Week.DoesNotExist:
    raise Http404("Poll for said week does not exists")
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return redirect("results", week_id)
