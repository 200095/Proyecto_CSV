from django.urls import path
from . import views
app_name = "CSV"
urlpatterns = [
    path("", views.index, name='index'),
    path("Conocenos.html", views.conocer, name='conocer'),
    path("Contacto.html", views.contactar, name='contactar'),
    path("index.html", views.inicio, name='inicio'),
    path("InicioDeSesion.html", views.iniciar, name='iniciar'),
    path("Soporte_Remoto.html", views.soporte, name='soporte'),
    path("add", views.add, name="add" ),
    path("borrar", views.borrar, name="borrar" ),
    path("login", views.login, name="login" ),
    path("aniversario.html", views.ani, name="aniversario"),
    path("Registrarse.html", views.registro, name="registro"),
    path("Mensajes.html", views.mensaje, name="mensaje")
    
]