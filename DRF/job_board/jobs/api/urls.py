from django.urls import path
from jobs.api.views import JobDetailAPIView,JobListCreateAPIView

urlpatterns=[
    path("jobs/",JobListCreateAPIView.as_view(),name="jobs-list"),
    path("job/<int:pk>/",JobDetailAPIView.as_view(),name="job-detail")
]