from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)

urlpatterns =[
    #authentication url path
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #endpoint urls 
    path('', views.endpoints),
    path('advocates/', views.advocates_list, name="advocates" ),
    path('advocates/<str:username>/', views.advocte_details),
    #class based views url patterns 
    # path('advocates/<str:username>/', views.Advocatedetails.as_view()),
    #companies urls
    path('companies/', views.companies_list)
]