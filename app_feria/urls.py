from django.urls import path
from app_feria.views import *
from django.contrib.auth.views import LogoutView
"""

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('vuelo/', vuelo),
    path('personal/', personal),
    path('pasajero/', pasajero),
    path('sobrenostros', sobrenosotros, name="Sobrenosotros"),

#URL DE CREACION
    path('formulario1/', formulariovuelo, name="Crear Vuelos"),
    path('formulario2/', formulariopersonal, name="Crear Personal"),
    path('formulario3/', formulariopasajero, name="Crear Pasajeros"),

#URL DE LEER
    path('leerVuelos/',leerVuelos, name="Leer Vuelos"),
    path('leerPersonal/',leerPersonal, name="Leer Personal"),
    path('leerPasajeros/',leerPasajero, name="Leer Pasajeros"),

#URL DE EDICION
    path('editaVuelo/<numVuelo>/', editaVuelo, name = "EditaVuelo"),
    path('editarPersonal/<profesionPersonal>/', editarPersonal, name = "EditarPersonal"),
    path('editarPasajero/<idvueloPasajero>/', editarPasajero, name = "EditarPasajero"),

#URL DE ELIMINACION
    path('eliminaVuelo/<numVuelo>/', eliminaVuelo, name = "EliminaVuelo"),
    path('eliminaPersonal/<profesionPersonal>/', eliminaPersonal, name = "EliminaPersonal"),
    path('eliminaPasajero/<idvueloPasajero>/', eliminaPasajero, name = "EliminaPasajero"),

#URL DE BUSQUEDAS
    path('bus/', bus, name="Buscar"),
    path('buscarVuelos/', busquedaVuelos, name="Buscar Vuelos"),
    path('buscarPersonal/', busquedaPersonal, name="Buscar Personal"),
    path('buscarPasajero/', busquedaPasajero, name="Buscar Pasajeros"),
##
    path('buscar_pasa/',buscar_pasa),
    path('buscar_per/',buscar_per),
    path('buscar/',buscar),

#URL DE LOGIN Y LOGOUT
    path('login/',InicioSesion, name="Login"),
    path('registro/',registro, name="Registrarse"),
    path('logout/', LogoutView.as_view(template_name="app_feria/logout.html"), name="Logout"),

#URL DE EDICIONUSUARIO
    path('editUser/',editarUsuario, name="Editar Usuario"),
    path('avatar/', agregarAvatar, name="Avatar"),

    ]

"""
urlpatterns = [
    path('', inicio, name="Inicio"),
    path('jean/', jean),
    path('remera/', remera),
    path('camisa/', camisa),
    path('sobrenostros/', sobrenosotros, name="Sobrenosotros"),
    path('jean_c/', jean_c, name="jean_c"),

#URL DE CREACION
    path('formulario1/', formulariojean, name="Crear Jeans"),
    path('formulario2/', formularioremera, name="Crear Remera"),
    path('formulario3/', formulariocamisa, name="Crear Camisa"),

#URL DE LEER
    path('leerJeans',leerJeans, name="Leer Jeans"),
    path('leerRemera/',leerRemera, name="Leer Remera"),
    path('leerCamisas/',leerCamisa, name="Leer Camisas"),

#URL DE EDICION
    path('editaJean/<numJean>/', editaJean, name = "EditaJean"),
    path('editarRemera/<generoRemera>/', editarRemera, name = "EditarRemera"),
    path('editarCamisa/<generoCamisa>/', editarCamisa, name = "EditarCamisa"),

#URL DE ELIMINACION
    path('eliminaJean/<numJean>/', eliminaJean, name = "EliminaJean"),
    path('eliminaRemera/<generoRemera>/', eliminaRemera, name = "EliminaRemera"),
    path('eliminaCamisa/<generoCamisa>/', eliminaCamisa, name = "EliminaCamisa"),

#URL DE BUSQUEDAS
    path('bus/', bus, name="Buscar"),
    path('buscarJeans/', busquedaJeans, name="Buscar Jeans"),
    path('buscarRemera/', busquedaRemera, name="Buscar Remera"),
    path('buscarCamisa/', busquedaCamisa, name="Buscar Camisa"),
##
    path('buscar_cami/',buscar_cami),
    path('buscar_rem/',buscar_rem),
    path('buscar/',buscar),

#URL DE LOGIN Y LOGOUT
    path('login/',InicioSesion, name="Login"),
    path('registro/',registro, name="Registrarse"),
    path('logout/', LogoutView.as_view(template_name="app_feria/logout.html"), name="Logout"),

#URL DE EDICIONUSUARIO
    path('editUser/',editarUsuario, name="Editar Usuario"),
    
    ]

