from django.urls import path

from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path('quiz/<int:student_id>/', views.quiz_form, name='quiz_form'),
]
