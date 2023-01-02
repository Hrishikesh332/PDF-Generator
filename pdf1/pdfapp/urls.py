from django.urls import path
from . import views
from pdfapp.views import Home
urlpatterns=[
    path("pdf", views.pdf_gen, name="pdf_gen"),
    path('report', views.report_gen, name='report_gen'),
    path('', Home.as_view(), name='home')
]