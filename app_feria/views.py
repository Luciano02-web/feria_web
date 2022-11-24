from unicodedata import decomposition
from django.shortcuts import render
from django.http import HttpResponse

from app_feria.models import *
from app_feria.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #se importa el AuthenticationForm para el inicio de sesion
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import CreateView

# Create your views here.

############
#  INICIO  #
############

def inicio(request):
    return render(request,'app_feria/inicio.html')


############
#  LOGIN  #
############

def InicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contra)
            if user:
                login(request, user)
                return render(request, "app_feria/inicio.html", {"mensaje":f"Bienvenido/a {user}"})
        else:
            return render(request, "app_feria/inicio.html", {"mensaje": "Datos incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "app_feria/login.html", {"f1":form})


def registro(request):
    if request.method == "POST":
        formu = FormularioRegistro(request.POST)
        if formu.is_valid():
            username = formu.cleaned_data["username"]
            formu.save()
            return render(request, "app_feria/inicio.html", {"mensaje": f"Usuario {username} creado."})
    else:
        formu = FormularioRegistro()
    return render(request, "app_feria/registro.html", {"f2":formu})





############
#  JEANS  #
############

@login_required
def jean(request):
    return render(request,'app_feria/jean.html')


#CREACION DE JEANS
@login_required
def formulariojean(request):
    if request.method=="POST":#si yo le doy al boton GO
        formulariojean = FormuJean(request.POST, request.FILES)
        if formulariojean.is_valid():
            info = formulariojean.cleaned_data
            jeanf = Jean(codigo = info["codigo"], talle = info["talle"], color = info["color"].capitalize(), precio = info["precio"], imagen = info["imagen"], genero = info["genero"].capitalize())#lee la informacion de las cajas de texto
            jeanf.save()#guardar en la base de datos
            return render(request,"app_feria/inicio.html")#despues de enviar salta esta pagina
    else:
        formulariojean = FormuJean()
    return render(request,"app_feria/FJean.html",{"formulario1":formulariojean})#cuando entro a la pagina web por primera vez sale este return

#BUSQUEDA DE JEANS
@login_required
def busquedaJeans(request):
    return render(request,"app_feria/busquedaJeans.html")

@login_required
def buscar(request):
    if request.GET["genero"]:
        busqueda = request.GET["genero"]
        jeans = Jean.objects.filter(genero=busqueda.capitalize())#puede ir tambien camada__icontains = busqueda
        return render(request,"app_feria/jean_b.html",{"jeans":jeans, "busqueda":busqueda})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando jeans para {busqueda}")
 

@login_required
#LEER JEANS
def leerJeans(request):
    fly = Jean.objects.all()
    contexto = {"fly":fly}
    return render(request,"app_feria/jean.html",contexto)


@login_required
#ELIMINAR JEANS
def eliminaJean(request, numJean):
    idcodigo= Jean.objects.get(codigo=numJean)
    idcodigo.delete()
    jeans = Jean.objects.all()
    contextov = {"fly":jeans}
    return render (request, "app_feria/jean.html", contextov)


#EDITAR JEANS
@login_required
def editaJean(request, numJean):
    idcodigo = Jean.objects.get(codigo=numJean)

    if request.method == "POST":
        formulariojean = FormuJean(request.POST,request.FILES)##,request.FILES
        if formulariojean.is_valid():
            
            info = formulariojean.cleaned_data
            
            idcodigo.imagen = info["imagen"]
            idcodigo.codigo = info["codigo"]
            idcodigo.talle = info["talle"]
            idcodigo.color = info["color"].capitalize()
            idcodigo.genero = info["genero"].capitalize()
            idcodigo.precio = info["precio"]

            idcodigo.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariojean = FormuJean(initial={"codigo":idcodigo.codigo,"talle":idcodigo.talle,
        "color": idcodigo.color, "precio": idcodigo.precio, "imagen": idcodigo.imagen, "genero": idcodigo.genero})
    return render(request,"app_feria/editarJean.html", {"formulario1":formulariojean, "idJean": numJean})



















############
# REMERA #
############

@login_required
def remera(request):
    return render(request,'app_feria/remera.html')


@login_required
#CREACION DE REMERA
def formularioremera(request):
    if request.method=="POST":
        formularioremera = FormuRemera(request.POST, request.FILES)
        if formularioremera.is_valid():
            info = formularioremera.cleaned_data
            remeraf = Remera(codigo = info["codigo"], talle = info["talle"], color = info["color"].capitalize(), precio = info["precio"], imagen = info["imagen"], genero = info["genero"].capitalize())
            remeraf.save()
            return render(request,"app_feria/inicio.html")
    else:
        formularioremera = FormuRemera()
    return render(request,"app_feria/FRemera.html",{"formulario2":formularioremera})


@login_required
#BUSQUEDA DE REMERA
def busquedaRemera(request):
    return render(request,"app_feria/busquedaRemera.html")


@login_required
def buscar_rem(request):
    if request.GET["genero"]:
        busqueda_rem = request.GET["genero"]
        remeras = Remera.objects.filter(genero = busqueda_rem.capitalize())#puede ir tambien camada__icontains = busqueda
        return render(request,"app_feria/remera_b.html",{"remeras":remeras, "busqueda_rem":busqueda_rem})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando remeras para {busqueda_rem}")


@login_required
#LEER REMERA
def leerRemera(request):
    persona = Remera.objects.all()
    contexto = {"persona":persona}
    return render(request,"app_feria/remera.html",contexto)


@login_required
#ELIMINAR REMERA
def eliminaRemera(request, generoRemera):
    generoPe= Remera.objects.get(codigo=generoRemera)
    generoPe.delete()
    remeraElim = Remera.objects.all()
    contextoPe = {"persona":remeraElim}
    return render (request, "app_feria/remera.html", contextoPe)


@login_required
#EDITAR REMERA
def editarRemera(request, generoRemera):
    codigo= Remera.objects.get(codigo=generoRemera)

    if request.method=="POST":
        formularioremera = FormuRemera(request.POST, request.FILES)
        if formularioremera.is_valid():
            
            info = formularioremera.cleaned_data
           
            codigo.codigo = info["codigo"]
            codigo.talle = info["talle"]
            codigo.color = info["color"]
            codigo.precio = info["precio"]
            codigo.genero = info["genero"]
            codigo.imagen = info["imagen"]
            codigo.save()
            return render(request,"app_feria/inicio.html")
    else:
        formularioremera = FormuRemera(initial={"codigo":codigo.codigo,"talle":codigo.talle,
        "color":codigo.color, "precio":codigo.precio, "genero":codigo.genero, "imagen":codigo.imagen})
    return render(request,"app_feria/editarRemera.html",{"formulario2":formularioremera, "generoRemera": generoRemera })  




############
# CAMISAS #
############

@login_required
def camisa(request):
    return render(request,'app_feria/camisa.html')


@login_required
# CREACION DE CAMISA
def formulariocamisa(request):
    if request.method=="POST":
        formulariocamisa = FormuCamisa(request.POST, request.FILES)
        if formulariocamisa.is_valid():
            info = formulariocamisa.cleaned_data
            editCamisa = Camisa(codigo = info["codigo"], talle = info["talle"], color = info["color"].capitalize(), precio = info["precio"], imagen = info["imagen"], genero = info["genero"].capitalize())
            editCamisa.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariocamisa = FormuCamisa()
    return render(request,"app_feria/FCamisa.html",{"formulario3":formulariocamisa})


@login_required
#BUSQUEDA DE CAMISA
def busquedaCamisa(request):
    return render(request,"app_feria/busquedaCamisa.html")

@login_required
def buscar_cami(request):
    if request.GET["genero"]:
        busqueda_cami = request.GET["genero"]
        camisas = Camisa.objects.filter(genero = busqueda_cami.capitalize())#puede ir tambien camada__icontains = busqueda
        return render(request,"app_feria/camisa_b.html",{"camisas":camisas, "busqueda_cami":busqueda_cami})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando camisa para {busqueda_cami}")


@login_required
#LEER CAMISA
def leerCamisa(request):
    pasa = Camisa.objects.all()
    contexto = {"pasa":pasa}
    return render(request,"app_feria/camisa.html",contexto)  


@login_required
#ELIMINAR CAMISA
def eliminaCamisa(request, generoCamisa):
    elimCamisa= Camisa.objects.get(genero=generoCamisa)
    elimCamisa.delete()

    camisaElim = Camisa.objects.all()
    contextoPa = {"pasa":camisaElim}
    return render (request, "app_feria/camisa.html", contextoPa)


@login_required
#EDITAR CAMISA
def editarCamisa(request, generoCamisa):
    genero= Camisa.objects.get(genero=generoCamisa)

    if request.method=="POST":
        formulariocamisa = FormuCamisa(request.POST, request.FILES)
        if formulariocamisa.is_valid():
            
            info = formulariocamisa.cleaned_data
           
            genero.codigo = info["codigo"]
            genero.talle = info["talle"]
            genero.color = info["color"]
            genero.precio = info["precio"]
            genero.genero = info["genero"]
            genero.imagen = info["imagen"]
            genero.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariocamisa = FormuCamisa(initial={"codigo":genero.codigo,"talle":genero.talle,
        "color":genero.color, "precio":genero.precio, "genero":genero.genero, "imagen":genero.imagen})
    return render(request,"app_feria/editarCamisa.html",{"formulario3":formulariocamisa, "generoCamisa": generoCamisa })  



#############
# BUSCADOR #
#############


@login_required
#BUSCADOR
def bus(request):
    return render(request,"app_feria/buscar.html")


#################
# EDITARUSUARIO #
#################

@login_required
def editarUsuario(request):
    usuarioConectado= request.user
    if request.method=="POST":
        miFormulario = FormularioEditarUsuario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            usuarioConectado.first_name = info["first_name"]
            usuarioConectado.last_name = info["last_name"]
            usuarioConectado.email = info["email"]
            usuarioConectado.password1 = info["password1"]
            usuarioConectado.password2 = info["password2"]
            usuarioConectado.save()
            return render(request,"app_feria/inicio.html")
    else:
        miFormulario = FormularioEditarUsuario(initial={
            "first_name": usuarioConectado.first_name,
            "last_name": usuarioConectado.last_name,
            "email": usuarioConectado.email,
            })
    return render(request,"app_feria/editarUsuario.html",{"miForm":miFormulario, "usuario": usuarioConectado })

##########
# About #
##########

def sobrenosotros(request):
    return render(request,'app_feria/sobrenosotros.html')

def jean_c(request):
    jean = Jean.objects.all()
    return render(request,'app_feria/jean_c.html',{'jean':jean})





"""

 
                {% if request.user.is_superuser %}
    
                <ol>
                    <button style="background-color:black; border-color: forestgreen">
                        <em>
                            <a href="{% url 'EliminaJean' v.codigo %}">Eliminar Jean</a>
                        </em>
                    </button>
                    
                    <button style="background-color:black; border-color: forestgreen">
                        <em>
                            <a href="{% url 'EditaJean' v.codigo %}">Editar Jean</a>
                        </em>
                    </button>
                    <h6>
                        ----------------------------
                    </h6>
                </ol>
                {% else %}
    
                ----------------------------
    
                {% endif %}




{% if request.user.is_superuser %}
<div>
        <ol>
            <button style="background-color:black; border-color: forestgreen">
                <em>
                    <a href="{% url 'Crear Jeans' %}"> Agregar otro Jean</a>
                </em>
            </button>
        </ol>
</div>

{% else %}

"""