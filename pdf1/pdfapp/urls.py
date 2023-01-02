from django.urls import path
from . import views
urlpatterns=[
    path("pdf", views.pdf_gen, name="pdf_gen"),
    path('report', views.report_gen, name='report_gen')
]