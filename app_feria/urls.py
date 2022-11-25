from django.urls import path
from app_feria.views import *
from django.contrib.auth.views import LogoutView
from app_feria import views
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


'''
{% for je in jean %}
            
        <ol>
            {% if v.imagen %}
            <img src="{{v.imagen.url}}"style="
            width: 200px;
            height: 200px;">
            {% endif %}
            Jean: {{codigo}}
            <h6>
                Jean: {{je.codigo}}--Talle: {{je.talle}}--Color: {{jean.color}}--Para {{jeans.genero}}--Precio: ${{Jeans.precio}}
            </h6>
        </ol>
        
        {% endfor %}
'''
urlpatterns = [
    path('', inicio, name="Inicio"),
    path('jean/', jean),
    path('remera/', remera),
    path('camisa/', camisa),
    path('todo100/', todo100),
    path('calzado/', calzado),
    path('sobrenostros/', sobrenosotros, name="Sobrenosotros"),
    path('jean_detail/<int:codigo>/', views.jean_detail, name="Detalle"),

#URL DE CREACION
    path('formulario1/', formulariojean, name="Crear Jeans"),
    path('formulario2/', formularioremera, name="Crear Remera"),
    path('formulario3/', formulariocamisa, name="Crear Camisa"),
    path('formulario4/', formulariotodo, name="Crear todo por 100"),
    path('formulario5/', formulariocalzado, name="Crear Calzado"),


    #path('jean_c/', jean_c, name="jean_c"),

#URL DE LEER
    path('leerJeans',leerJeans, name="Leer Jeans"),
    path('leerRemera/',leerRemera, name="Leer Remera"),
    path('leerCamisas/',leerCamisa, name="Leer Camisas"),
    path('leerTodo100/',leerTodo, name="Leer todo por 100"),
    path('leerCalzado/',leerCalzado, name="Leer Calzado"),


#URL DE EDICION
    path('editaJean/<numJean>/', editaJean, name = "EditaJean"),
    path('editarRemera/<generoRemera>/', editarRemera, name = "EditarRemera"),
    path('editarCamisa/<generoCamisa>/', editarCamisa, name = "EditarCamisa"),
    path('editarTodo/<generoTodo>/', editarTodo, name = "Editar todo por 100"),
    path('editarCalzado/<generoCalzado>/', editarCalzado, name = "EditarCalzado"),


#URL DE ELIMINACION
    path('eliminaJean/<numJean>/', eliminaJean, name = "EliminaJean"),
    path('eliminaRemera/<generoRemera>/', eliminaRemera, name = "EliminaRemera"),
    path('eliminaCamisa/<generoCamisa>/', eliminaCamisa, name = "EliminaCamisa"),
    path('eliminaTodo/<generoTodo>/', eliminaTodo, name = "Elimina todo por 100"),
    path('eliminaCalzado/<generoCalzado>/', eliminaCalzado, name = "EliminaCalzado"),


#URL DE BUSQUEDAS
    path('bus/', bus, name="Buscar"),
    path('buscarJeans/', busquedaJeans, name="Buscar Jeans"),
    path('buscarRemera/', busquedaRemera, name="Buscar Remera"),
    path('buscarCamisa/', busquedaCamisa, name="Buscar Camisa"),
    path('buscarCalzado/', busquedaCalzado, name="Buscar Calzado"),


##
    path('buscar_calzado/',buscar_calza),
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

