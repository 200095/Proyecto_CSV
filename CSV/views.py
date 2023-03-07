from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .models import Users
from .models import Contactar
from django.db import IntegrityError
# Create your views here.

def index(request):
    return render(request, "CSV/index.html")

def conocer(request):
    return render(request, "CSV/Conocenos.html")

def inicio(request):
    return render(request, "CSV/index.html")

def contactar(request):
    return render(request, "CSV/Contacto.html")

def iniciar(request):
    return render(request, "CSV/InicioDeSesion.html")

def soporte(request):
    return render(request, "CSV/Soporte_Remoto.html")

def registro(request):
    return render(request, "CSV/Registrarse.html")

def mensaje(request):
    return render(request, "CSV/Mensajes.html")


class FormularioCSV (forms.Form):
        csv = forms.CharField(label="Nueva CSV", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Usuario'}))
        csv_paswd = forms.CharField(label="Contra",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Contraseña'}))

class FormularioContacto (forms.Form):
        #us_contacto = forms.CharField(label="usuario_contacto", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Usuario_Contacto1'}))
        texto_contacto = forms.CharField(label="texto_contacto", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'texto_Contacto1'}))

        

def add(request):
        lista = ["ADRIAN","adrian"]
        usuarios = Users.objects.exclude(Usuario__in = lista)
        print(usuarios)
        return render(request, "CSV/add.html", {
            "usuarios": usuarios
        })

def login(request):
        if request.method == "POST":
                usuario = request.POST["usuario"]
                request.session["iniciado"] = usuario
                return render(request, "CSV/index.html", {"usuario" : usuario})
        else:
                if "iniciado" in request.session:
                        return render(request, "CSV/index.html", {"usuario" :  request.session["iniciado"]})
                else:
                        return render(request, "CSV/index.html")

def iniciar(request):
        if request.method == "POST":
                formulario = FormularioCSV(request.POST)
                if formulario.is_valid():
                   try:
                        usuario = formulario.cleaned_data["csv"]
                        contra = formulario.cleaned_data["csv_paswd"]
                        c_usuario = Users.objects.filter(Usuario__iexact=usuario).values().first()
                        print(c_usuario)
                        if (usuario == "adrian" or usuario == "ADRIAN") and contra == "root":
                                request.session["iniciado"] = usuario
                                return HttpResponseRedirect(reverse("CSV:add"))
                        elif c_usuario:
                                if c_usuario["Password"] == contra:
                                        request.session["iniciado"] = usuario
                                        return render(request, "CSV/index.html", {"usuario" : request.session["iniciado"]})
                                return render(request, "CSV/InicioDeSesion.html", {
                                        "form": formulario, "msg" : "El usuario no está registrado."
                                })
                        return render(request, "CSV/InicioDeSesion.html", {
                                        "form": formulario, "msg" : "El usuario no está registrado."
                                })
                   except TypeError:
                        return render(request, "CSV/InicioDeSesion.html", {
                                  "form": formulario, "msg" : "Datos no válidos."})
                else:   
                        return render(request, "CSV/InicioDeSesion.html", {
                                "form": formulario
                        })
        else:
                return render(request, "CSV/InicioDeSesion.html", {
                        "form":FormularioCSV()
                })

def borrar(request):
        if request.method == "POST":
                u = Users.objects.get(Usuario = request.POST["usuario"])
                u.delete()
                lista = ["ADRIAN","adrian"]
                usuarios = Users.objects.exclude(Usuario__in = lista)
                print(usuarios)
                return render(request, "CSV/add.html", {"usuarios": usuarios})
        
def ani(request):
     ahora =datetime.datetime.now()
     return render (request, "CSV/aniversario.html", {
             "aniversario": ahora.month == 10 and ahora.day == 15})

def registro(request):
        if request.method == "POST":
                   formulario = FormularioCSV(request.POST)
                   if formulario.is_valid():
                      try:
                          user = formulario.cleaned_data['csv']
                          passw = formulario.cleaned_data['csv_paswd']
                          crearuser = Users.objects.create(Usuario=user,Password=passw)
                          crearuser.save()
                          return render(request, "CSV/index.html")
                      except IntegrityError:
                          return render(request, "CSV/Registrarse.html", {
                                  "form": formulario, "msg" : "El usuario ya está registrado."})

                  
                        #      return render(request, "CSV/Registrarse.html", {
                        #          "form": formulario, "msg" : "El usuario ya está registrado."})
                             
                #    if [usuario]  in request.session["usuarios"]:
                #                 return render(request, "CSV/Registrarse.html", {
                #                 "form": formulario, "msg" : "El usuario no está registrado."})
                   
        else:
                formulario = FormularioCSV()
                return render(request, "CSV/Registrarse.html", {'form':formulario})

def contactar(request):
        if request.method == "POST":
                   
                          usert = request.session["iniciado"]
                          text = request.POST.get('introducir_mensaje')
                          texto = Contactar.objects.create(Usuario=usert, Mensaje=text)
                          texto.save()
                          return render(request, "CSV/index.html")

        else:
                form = FormularioContacto()
        return render(request, "CSV/Contacto.html", {"usuario":request.session["iniciado"] ,'form':form})