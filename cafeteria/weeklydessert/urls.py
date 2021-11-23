from django.urls import path, include

from . import views

urlpatterns = [
	path("", views.index, name="index"),
    path("account/", include("django.contrib.auth.urls")),
  
	path("signup/", views.SignUp.as_view(), name="signup"),

	# Add a path to your logout request below:

	path("polls/<int:pk>/", views.DetailsView.as_view(), name="detail"),
	path("polls/<int:pk>/results/", views.ResultsView.as_view(), name="results"),
	path("polls/<int:week_id>/vote/", views.vote, name="vote"),
]