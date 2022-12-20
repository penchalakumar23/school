
from django.urls import path
from .views import feeCollection,feeDuesReport,feeCollectionReport

urlpatterns = [

    path('fee/',feeCollection),
    path('feedues/',feeDuesReport),
    path('feeCR/',feeCollectionReport),

]