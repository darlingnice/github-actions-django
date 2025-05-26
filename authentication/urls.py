from django.urls import path
from . import views 


urlpatterns = [
    path('',views.signup,name="signup"),
    path('login/',views.login_page,name="login_page"),
    path('dashboard/',views.dashboard,name="dashboard")
]