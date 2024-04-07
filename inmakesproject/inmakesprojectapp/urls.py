from django.urls import path
from . import views


app_name='inmakesprojectapp'
urlpatterns = [

    path('',views.allMovieCat,name='allMovieCat'),
    path('category/<slug:c_slug>/', views.demo, name='demo'),
    path('usermovie/', views.user_movie, name='user_movie'),
    path('add/',views.add_movie,name='add_movie'),
    path('<slug:c_slug>/',views.allMovieCat,name='movie_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>/',views.movieDetail,name='movieCatdetail'),
    path('movie/<int:title_id>/review/', views.movie_review, name='movie_review'),
    path('movie/<int:id>/',views.delete,name='delete'),
    path('movie/<slug:movie_slug>/update/', views.update, name='update'),
    path('movie/<slug:movie_slug>/delete/', views.delete, name='delete'),



]