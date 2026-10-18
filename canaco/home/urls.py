from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("contactanos/", views.contactanos, name="contactanos"),
    path("categoria/", views.categoria, name="categoria"),
    
    # Rutas de autenticación requeridas en el Laboratorio 10
    path("login/", auth_views.LoginView.as_view(template_name='home/login.html'), name="login"),
    path("logout/", LogoutView.as_view(next_page='home:login'), name="logout"),
    path("sign-up/", views.sing_up, name="sign_up"),
    
    path("noticia/", views.noticia, name="noticia"),
    path("perfil/", views.perfil, name="perfil"),
    path("crear-publicacion/", views.crear_publicacion, name="crear_publicacion"),
    
    # Gestión de perfiles y contraseñas
    path("crud_perfil/", views.crud_perfil, name="crud_perfil"),
    path("cambiar-contrasena/", views.crud_cambiar_contraseña, name="crud_cambiar_contraseña"),
    
    # CRUD de usuarios (incluyendo parámetros de PK y acciones del laboratorio)
    path("crud_usuario/", views.crud_usuario, name="crud_usuario"),
    path("crear-usuario/", views.crear_usuario, name="crear_usuario"),
    path("crud_usuarios/<int:pk>/editar", views.editar_usuario, name="editar_usuario"),
    path("crud_usuarios/<int:pk>/bloquear", views.bloquear_usuario, name="bloquear_usuario"),
    path("crud_usuarios/<int:pk>/eliminar", views.eliminar_usuario, name="eliminar_usuario"),
    
    # Otras secciones
    path("crud_categoria/", views.crud_categoria, name="crud_categoria"),
    path("crud_comentarios/", views.crud_comentarios, name="crud_comentarios"),
    path("crud_noticias/", views.crud_noticias, name="crud_noticias"),
    path("editar_categoria/", views.editar_categoria, name="editar_categoria"),
]