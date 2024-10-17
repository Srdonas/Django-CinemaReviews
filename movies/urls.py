from django.urls import path
from . import views

urlpatterns = [
    # Movie-related URLs
    path('', views.list_movies, name='list_movies'),
    path('movie/<int:movie_id>/', views.movie_details, name='movie_detail'),
    path('movie/add/', views.create_movie, name='add_movie'),
    path('movie/<int:movie_id>/update/', views.update_movie, name='update_movie'),
    path('movie/<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),

    # Review-related URLs
    path('movie/<int:movie_id>/review/add/', views.create_review, name='add_movie_review'),
    # path('review/<int:review_id>/update/', views.update_review, name='update_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]
