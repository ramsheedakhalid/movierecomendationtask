from . import views
from django . urls import path

app_name = 'credential'
urlpatterns=[
    path('registerationn',views.registerationn,name='registerationn'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout',views.logout,name='logout'),
    path('profile/<int:username_id>/', views.display_user, name='display_user'),
    path('profile/update/<int:username_id>/', views.update_profile, name='update_profile'),
    path('profile/delete/<int:username_id>/', views.delete_profile, name='delete_profile'),

]