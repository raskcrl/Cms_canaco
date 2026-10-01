
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
 path("", views.index, name="index"),
 path("base/", views.base, name="base"),
 path("contactanos/", views.contactanos, name="contactanos"),
 path("categoria/", views.categoria, name="categoria"),
 path("", views.login, name="login"),
 path("", views.noticia, name="noticia"),
 path("", views.perfil, name="perfil"),
 path("", views.sing_up, name="sing_up"),
 path("", views.crear_publicacion, name="crear_publicacion"),
 path("", views.crear_usuario, name="crear_usuario"),
 path("", views.crud_cambiar_contraseña, name="crud_cambiar_contraseña"),
 path("crud_categoria/", views.crud_categoria, name="crud_categoria"),
 path("crud_comentarios", views.crud_comentarios, name="crud_comentarios"),
 path("crud_noticias", views.crud_noticias, name="crud_noticias"),
 path("crud_perfil", views.crud_perfil, name="crud_prefil"),
 path("crud_usuario", views.crud_usuario, name="crud_usuario"),
 path("editar_categoria", views.editar_categoria, name="editar_categoria"),
 
]