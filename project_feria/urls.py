"""project_feria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_feria/', include("app_feria.urls"))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""

<div class="col-sm-6 align-items-center">

    {% for v in fly %}
    
    <ul>

        
        
        <ol>
            {% if v.imagen %}
            <img src="{{v.imagen.url}}">
            {% endif %}
            <h6>
                Jean: {{v.codigo}}--Talle: {{v.talle}}--Color: {{v.color}}--Para {{v.genero}}--Precio: ${{v.precio}}
            </h6>
        </ol>
                
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

    </ul>

    {% endfor %}

</div>
"""