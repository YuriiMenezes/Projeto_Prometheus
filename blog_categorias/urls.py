from django.urls import path
from blog_categorias import views

urlpatterns = [

    path('', views.CategoriasIndex.as_view(), name='categoria_index'),
    path('novidades/', views.novidades.as_view(), name='novidades'),
    path('windows/', views.windows.as_view(), name='windows'),
    path('linux/', views.linux.as_view(), name='linux'),
    path('desenvolvimento/', views.desenvolvimento.as_view(), name='desenvolvimento'),
    path('tutoriais/', views.tutoriais.as_view(), name='tutoriais'),
   

]