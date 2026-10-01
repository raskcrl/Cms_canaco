from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
 return render(request, 'home/index.html')

def base(request):
 return render(request, 'home/base.html')

def categoria(request):
 return render(request, 'home/categoria.html') 

def contactanos(request):
 return render(request, 'home/contactanos.html')    

def crear_publicacion(request):
 return render(request, 'home/crear_publicacio.html')  

def crear_usuario(request):
 return render(request, 'home/crear_usuario.html')  

def crud_cambiar_contraseña(request):
 return render(request, 'home/crud_cambiar_contraseña.html') 

def crud_comentarios(request):
 return render(request, 'home/crud_comentarios.html')   

def crud_noticias(request):
 return render(request, 'home/crud_noticias.html')  

def crud_perfil(request):
 return render(request, 'home/crud_perfil.html') 

def crud_categoria(request):
 return render(request, 'home/crud_categoria.html') 

def crud_usuario(request):
 return render(request, 'home/crud_usuario.html')  

def editar_categoria(request):
 return render(request, 'home/editar_categoria.html')  

def login(request):
 return render(request, 'home/login.html') 

def noticia(request):
 return render(request, 'home/noticia.html') 

def perfil(request):
 return render(request, 'home/perfil.html')    

def sing_up(request):
 return render(request, 'home/sing_up.html')  