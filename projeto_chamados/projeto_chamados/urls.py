from django.contrib import admin
from django.urls import path
from aplicacao_chamados import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.abrir_chamado, name='abrir_chamado'),
    path('visualizar_todos_chamados/', views.visualizar_todos_chamados, name='visualizar_todos_chamados'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)