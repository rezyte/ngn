from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
	path('iau', views.view_score, name="view_score"),
	path('iau/login.d/home.do', views.single_page_cd, name="view_score"),
	path('iau/OnePageWorkBook.do', views.final_page, name="final_page"),
	path('', views.main_page, name="index"),
	path('iau/login.d/', views.verify),
]
