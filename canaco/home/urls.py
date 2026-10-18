from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("contactanos/", views.contactanos, name="contactanos"),
    path("categoria/", views.categoria, name="categoria"),
    path("login/", views.login, name="login"),
    path("noticia/", views.noticia, name="noticia"),
    path("perfil/", views.perfil, name="perfil"),
    path("sign-up/", views.sing_up, name="sign_up"),
    path("crear-publicacion/", views.crear_publicacion, name="crear_publicacion"),
    path("crear-usuario/", views.crear_usuario, name="crear_usuario"),
    path("cambiar-contrasena/", views.crud_cambiar_contraseña, name="crud_cambiar_contraseña"),
    path("crud_categoria/", views.crud_categoria, name="crud_categoria"),
    path("crud_comentarios/", views.crud_comentarios, name="crud_comentarios"),
    path("crud_noticias/", views.crud_noticias, name="crud_noticias"),
    path("crud_perfil/", views.crud_perfil, name="crud_prefil"),
    path("crud_usuario/", views.crud_usuario, name="crud_usuario"),
    path("editar_categoria/", views.editar_categoria, name="editar_categoria"),
]