# novo arquivo experiencein/perfis/urls.py 

from django.urls import path
from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('senha/<int:id_senha>', views.exibir, name='exibir'),
	path('senha/<int:id_senha>/chamar', views.chamar, name='chamar')
]